class Player:

    def __repr__(self):
        return self.name

    def __init__(self, name: str):
        self.name = name
        self.used_words = []

    def get_words_count(self) -> int:
        return len(self.used_words)

    def set_used_word(self, word: str):
        """
        Adds a word to the list of used words

        :param word: word to add
        :return: None
        """
        self.used_words.append(word)

    def is_used_word(self, word: str) -> bool:
        return word in self.used_words
