import os
from gtts import gTTS

class TextToSpeech:
    def __init__(self, outputDirectory):

        self.outputDirectory = outputDirectory

    def convertToMP3(self, text, language):
        textToSpeechModule = gTTS(text=text, lang=language, slow=False)
        textToSpeechModule.save(self.outputDirectory)

