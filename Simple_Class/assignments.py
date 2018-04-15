class MaxSizeList(object):

    def __init__(self, val):
        self.max = val
        self.wordList = []

    def push(self, val):
        wordList = self.wordList
        if len(wordList) >= self.max:
            wordList.pop(0)
        wordList.append(val)

    def get_list(self):
        return self.wordList