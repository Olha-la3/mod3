import os
import pandas as pd


class PriceAnalyzer:
    def __init__(self, directory):
        self.directory = directory
        self.data = []
        self.search_results = []  # Список для хранения всех результатов поиска

    def load_prices(self):
        for filename in os.listdir(self.directory):
            if 'price' in filename and filename.endswith('.csv'):
                filepath = os.path.join(self.directory, filename)
                df = pd.read_csv(filepath)

                # Определение названий колонок
                product_col = next(
                    (col for col in df.columns if col.lower() in ['название', 'продукт', 'товар', 'наименование']),
                    None)
                price_col = next((col for col in df.columns if col.lower() in ['цена', 'розница']), None)
                weight_col = next((col for col in df.columns if col.lower() in ['фасовка', 'масса', 'вес']), None)

                # Если все необходимые колонки найдены
                if product_col and price_col and weight_col:
                    for _, row in df.iterrows():
                        product = row[product_col]
                        price = row[price_col]
                        weight = row[weight_col]

                        # Обработка и добавление только если цена и вес корректны
                        if pd.notna(price) and pd.notna(weight) and weight > 0:
                            price_per_kg = price / weight
                            self.data.append({
                                'product': product,
                                'price': price,
                                'weight': weight,
                                'file': filename,
                                'price_per_kg': price_per_kg
                            })

    def find_text(self, search_text):
        # Находим продукты, содержащие search_text
        filtered_data = [item for item in self.data if search_text.lower() in item['product'].lower()]
        # Сортируем по цене за килограмм
        filtered_data.sort(key=lambda x: x['price_per_kg'])
        return filtered_data

    def export_to_html(self, data, output_file):
        # Создаем HTML-таблицу
        html_content = """
        <html>
        <head>
        <title>Price List</title>
        </head>
        <body>
        <h1>Price List</h1>
        <table border="1">
        <tr>
        <th>№</th>
        <th>Наименование</th>
        <th>Цена</th>
        <th>Вес</th>
        <th>Файл</th>
        <th>Цена за кг</th>
        </tr>
        """

        for idx, item in enumerate(data, 1):
            html_content += f"""
            <tr>
            <td>{idx}</td>
            <td>{item['product']}</td>
            <td>{item['price']}</td>
            <td>{item['weight']}</td>
            <td>{item['file']}</td>
            <td>{item['price_per_kg']:.2f}</td>
            </tr>
            """

        html_content += """
        </table>
        </body>
        </html>
        """

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)


def main():
    analyzer = PriceAnalyzer(directory='D:\_Практическое задание _Анализатор прайс-листов._\Прайсы')
    analyzer.load_prices()

    while True:
        search_text = input("Введите название товара для поиска (или 'exit' для выхода): ")
        if search_text.lower() == 'exit':
            if analyzer.search_results:
                output_file = 'output.html'
                analyzer.export_to_html(analyzer.search_results, output_file)
                print(f"Данные экспортированы в файл {output_file}")
            print("Работа закончена.")
            break

        results = analyzer.find_text(search_text)
        if results:
            print(f"{'№':<3} {'Наименование':<30} {'Цена':<5} {'Вес':<5} {'Файл':<15} {'Цена за кг':<10}")
            for idx, item in enumerate(results, 1):
                print(
                    f"{idx:<3} {item['product']:<30} {item['price']:<5} {item['weight']:<5} {item['file']:<15} {item['price_per_kg']:.2f}")

            # Сохраняем найденные товары в общий список
            analyzer.search_results.extend(results)
        else:
            print("Товары не найдены.")


if __name__ == '__main__':
    main()
