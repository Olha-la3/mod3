from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        words_dict = {}

        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    words.extend(line.split())
                    words_dict[file_name] = words
                return words_dict

    def find(self, word):
        word_positions = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word.lower() in words:
                word_positions[name] = words.index(word.lower())
        return word_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            word_counts[name] = words.count(word.lower())
        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего