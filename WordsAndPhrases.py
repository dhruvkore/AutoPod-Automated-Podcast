import random
import os


class WordsAndPhrases:
    def __init__(self):
        self.transitionWords = []

        script_dir = os.path.dirname(__file__)
        relativePath = "resources/words/transitionWords.txt"
        self.transitionWordsFile = os.path.join(script_dir, relativePath)
        self.initializeTransitionWords()

    def initializeTransitionWords(self):
        with open(self.transitionWordsFile) as f:
            fileContents = f.readlines()

        for x in fileContents:
            self.transitionWords.append(x.strip())

    def getTrasitionWord(self):
        index = random.randint(0, len(self.transitionWords))
        return self.transitionWords[index]
