class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding = "utf-8") as file:
                words = file.read().lower()
                for i in words:
                    if i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        words = words.replace(i, "")
                words_list = words.split()
                all_words[file_name] = words_list
        return all_words

    def find(self, word):
        found_words = {}
        for file_name, words in self.get_all_words().items():
            try:
                found_words[file_name] = words.index(word.lower()) + 1
            except ValueError:
                continue
        return found_words

    def count(self, word):
        count_words = {}
        for file_name, words in self.get_all_words().items():
            count_words[file_name] = words.count(word.lower())
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


