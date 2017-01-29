#pip install urllib2
#pip install json

import urllib2
import json

def get_top_news(news_source):
    '''Returns list of top news stories. Powered by News API

        TODO: select news source [or categories such as sports, tech etc]
        Possible TODO: allow user to click link and go to the article

        News API Key: d1159719ec474bf1b82575b5b8478bef
        Default GET: https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey={API_KEY}
        API has two options: source, sortBy [to change these options you can modify the GET URL]

    '''
    articles = []
    news_source = news_source.strip().lower()
    news_source = news_source.replace(" " , "-")
    response = urllib2.urlopen("https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=d1159719ec474bf1b82575b5b8478bef")
    data = json.load(response)

    for i in range(3):
        articles.append(data["articles"][i]["title"] + "\n" + data["articles"][i]["url"])
    return articles

if __name__ == '__main__':
    print(get_top_news("cnn"))
