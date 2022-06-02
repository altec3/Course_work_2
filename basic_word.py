class BasicWord:
    def __init__(self, root_word: str, subwords: list):
        self.root_word = root_word
        self.subwords = subwords

    def is_correct(self, word: str) -> bool:
        return word in self.subwords

    def counts_subwords(self) -> int:
        return len(self.subwords)
