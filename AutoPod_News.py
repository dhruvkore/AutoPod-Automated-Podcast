from NewsParser import NewsParser
from Podcast import Podcast

if __name__ == '__main__':

    #Get News
    np = NewsParser()
    gn = np.getGoogleNews()
    headlines = gn.getNews()

    #HeadLines to Podcast
    podcast = Podcast(" Autopod News")
    podcast.podcastDescription = " The Automated News Podcast. "
    fullPodcastText = podcast.createNewsPodcast(headlines)

    #Text to Speech



    #Upload to Host
