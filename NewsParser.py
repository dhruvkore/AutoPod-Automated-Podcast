import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


class NewsParser:
    def getGoogleNews(self):
        gN = GoogleNews()
        return gN


class GoogleNews:
    def __init__(self):
        self.news_URL = "https://news.google.com/news/rss"
        self.pageText = ""
        self.description = ""
        self.headlines = []

    def getNews(self):
        Client = urlopen(self.news_URL)
        xml_page = Client.read()
        Client.close()

        soupPage = soup(xml_page, "xml")
        newsList = soupPage.findAll("item")

        # Pages Descriptions
        for news in newsList:
            self.description += news.title.text + "\n"
            self.description += news.link.text + "\n"
            self.description += news.pubDate.text + "\n"
            self.description += "-" * 60 + "\n"

            self.headlines.append(news.title.text)

        return self.headlines
