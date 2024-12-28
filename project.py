import os
import pandas as pd
import glob


class PriceListAnalyzer:
    def __init__(self, directory):
        self.directory = directory
        self.data = pd.DataFrame()

    def load_prices(self):
        # Получаем все файлы с именем, содержащим "price"
        price_files = glob.glob(os.path.join(self.directory, '*price*.csv'))

        # Обрабатываем каждый файл
        for file in price_files:
            try:
                df = pd.read_csv(file, delimiter=',', encoding='utf-8')

                # Извлекаем нужные колонки
                product_col = self.get_column_name(df, ['название', 'продукт', 'товар', 'наименование'])
                price_col = self.get_column_name(df, ['цена', 'розница'])
                weight_col = self.get_column_name(df, ['фасовка', 'масса', 'вес'])

                # Игнорируем файл, если нет всех нужных колонок
                if product_col and price_col and weight_col:
                    df = df[[product_col, price_col, weight_col]]

                    # Переименовываем колонки
                    df.columns = ['Наименование', 'Цена', 'Вес']

                    # Добавляем информацию о файле
                    df['Файл'] = os.path.basename(file)

                    # Добавляем данные в общий DataFrame
                    self.data = pd.concat([self.data, df], ignore_index=True)
            except Exception as e:
                print(f"Ошибка обработки файла {file}: {e}")

    def export_to_html(self, filename='prices.html'):
        """Экспортирует данные в HTML файл."""
        self.data.to_html(filename, index=False)

    def find_text(self, text):
        """Ищет товары по тексту и возвращает отсортированные результаты по цене за килограмм."""
        if self.data.empty:
            print("Данные не загружены.")
            return []

        # Находим позиции по тексту
        filtered_data = self.data[self.data['Наименование'].str.contains(text, na=False, case=False)]

        # Рассчитываем цену за килограмм
        if not filtered_data.empty:
            filtered_data['Цена за кг'] = filtered_data['Цена'] / filtered_data['Вес']
            filtered_data = filtered_data.sort_values(by='Цена за кг').reset_index(drop=True)
            return filtered_data

        return []

    def get_column_name(self, df, possible_names):
        """Возвращает название колонки, если она существует в DataFrame."""
        for name in possible_names:
            if name in df.columns:
                return name
        return None


# Основной код для работы с анализатором
if __name__ == "__main__":
    analyzer = PriceListAnalyzer(directory='path_to_your_directory')
    analyzer.load_prices()

    print("Работа с анализатором прайс-листов.")
    while True:
        user_input = input("Введите текст для поиска или 'exit' для выхода: ").strip()
        if user_input.lower() == "exit":
            print("Работа закончена.")
            break

        results = analyzer.find_text(user_input)
        if not results.empty:
            print("Найденные позиции:")
            print(results[['Наименование', 'Цена', 'Вес', 'Файл', 'Цена за кг']])
        else:
            print("По вашему запросу ничего не найдено.")

    # Экспорт в HTML при завершении
    analyzer.export_to_html()
