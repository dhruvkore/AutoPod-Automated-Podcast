from WordsAndPhrases import WordsAndPhrases
import datetime
import random


class Podcast:
    def __init__(self, podcastTitle):
        self.podcastTitle = podcastTitle
        self.dateTime = datetime.date.today().strftime("%B %d, %Y")
        self.podcastDescription = ""  # Optional
        self.wordsandphrases = WordsAndPhrases()

        self.fullPodcast = ""

    def createNewsPodcast(self, headlines):

        # Add Intro
        self.addIntro()

        # Add Headlines
        self.addHeadlines(headlines)

        # Add Outro
        self.addOutro()

        return self.fullPodcast

    def addIntro(self):
        intro = "Welcome to the " + \
                self.podcastTitle + " " \
                + self.podcastDescription + " ... \n"

        intro += " This podcast was created on " + self.dateTime + " \n"

        self.fullPodcast += intro

    def addHeadlines(self, headlines):
        bodyContent = ""

        for h in headlines:
            putTransition = random.randint(0, 2)
            if putTransition == 1:
                bodyContent += " " + self.wordsandphrases.getTrasitionWord() + " \n"

            bodyContent += " " + h + " \n"

        self.fullPodcast += bodyContent + " \n"

    def addOutro(self):
        outro = " Thank you for listening to this podcast. " \
                "Subscribe to " + self.podcastTitle + "on your podcast streaming service today. "

        self.fullPodcast += outro
