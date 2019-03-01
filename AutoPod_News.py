import datetime
import os

from NewsParser import NewsParser
from Podcast import Podcast
from TextToSpeech import TextToSpeech

if __name__ == '__main__':

    language = 'en'

    #Get News
    np = NewsParser()
    gn = np.getGoogleNews()
    headlines = gn.getNews()

    podcastName = " Autopod News"

    #HeadLines to Podcast
    podcast = Podcast(podcastName)
    podcast.podcastDescription = " The Automated News Podcast. "
    fullPodcastText = podcast.createNewsPodcast(headlines)

    today = datetime.date.today().strftime("%Y_%m_%d")
    outputFileName = podcastName.replace(' ', '') + "_" + language + "_" + today + ".mp3"

    script_dir = os.path.dirname(__file__)
    relativePath = "AutopodNews/" + outputFileName
    outputDirectory = os.path.join(script_dir, relativePath)

    #Text to Speech
    tts = TextToSpeech(outputDirectory)
    tts.convertToMP3(fullPodcastText, language)


    #Upload to Host
