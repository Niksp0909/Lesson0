class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = [*file_names]
        # self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        words = []
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for p in punctuation:
                        if p in line:
                            line = line.replace(p, ' ')
                    split_line = line.split()
                    words.extend(split_line)
            all_words[file_name] = words
        return all_words

    # print(get_all_words('test_file.txt'))
    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            word = word.lower()
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            word = word.lower()
            result[file_name] = words.count(word)
        return result
    # print(find('TEXT'))


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
