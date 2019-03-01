import os

class TextToSpeech:
    def __init__(self, outputDir):

        script_dir = os.path.dirname(__file__)
        relativePath = "resources/words/transitionWords.txt"
        self.transitionWordsFile = os.path.join(script_dir, relativePath)

    def convertToMP3(self, text):


