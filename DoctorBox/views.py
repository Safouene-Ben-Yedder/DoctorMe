from django.http import HttpResponse
from django.shortcuts import render
import wikipedia
import json
import re
import nltk 
from newspaper import Article
import requests
import feedparser





def Home(request):
    return render(request, 'Home.html')

def DoctorBox(request):
    return render(request, 'DoctorBox.html')


def resultDB(request):
    search = str(request.GET['n1'])
    result1 = wikipedia.summary(search)
    return render(request, 'DoctorBoxResult.html', {"resultDB2":result1})

def resultDB1(request):
    search1 = str(request.GET['n2'])
    ALL_NEWS_FEED_URL = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"


    def call_url(url):
        response = None
        user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 " \
                    "(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

        try:
            response = requests.get(
                url, headers={"User-Agent": user_agent})
        except requests.HTTPError as e:
            print("\nError accessing '{}': {} [{}]".format(url, e.reason, e.code),
                "\n")
        except Exception as e:
            print("\nError accessing '{}'\n".format(url), e, "\n")

        if response and response.status_code == 200:
            return response.text


    def parse_article_from_url(url):
        article = Article("")
        source_html = call_url(url)

        if source_html:
            article.set_html(source_html)
            article.parse()
            if article.text:
                article_dict = dict(title=article.title, article=article.text)
                return article_dict


    def parse_news(keyword=None, include_related_coverage=False):
        if (keyword is not None and keyword.strip() != ""):
            keyword = keyword.strip()
            print("\n Please wait... Fetching news article links"
                " about '{}' on Google News...\n".format(keyword))
        else:
            print("\n Please wait... Fetching recent news articles links...\n")

        keyword_url = "https://news.google.com/news/rss/search/section/" \
                    "q/{0}/{0}?hl=en&gl=US&ned=us".format(keyword)
        url = keyword_url if keyword else ALL_NEWS_FEED_URL

        xml_news_feed = call_url(url)
        parsed_feed = feedparser.parse(xml_news_feed)
        news_links = [news_item["link"] for news_item in parsed_feed["entries"]]

        if include_related_coverage:
            xml_news_links = [news_item["summary"]
                            for news_item in parsed_feed["entries"]]
            news_links = []

            for related_news_links in xml_news_links:
                all_related_links = re.findall(
                    r'(?<=\shref=")http\S+(?=")', related_news_links
                    )
                del all_related_links[-1]
                news_links.extend(all_related_links)

        print("\nArticle Links acquired:\n\n", news_links,
            "\n\nTotal no. of links:", len(news_links), "\n")

        print("\n...Fetching and parsing articles from acquired links.\n")
        formatted_response = [parse_article_from_url(link)
                            for link in news_links
                            if not link.endswith((".mp4", ".mp3"))]
        articles_json = json.dumps(
            [article for article in formatted_response if article is not None],
            ensure_ascii=False
            )

        print("\nDone!\n\n")

        return articles_json

    result1=parse_news(search1)
      # Test search
    return render(request, 'DoctorBoxResult.html', {"resultDB2":result1})