'''Returns info on top news stories
        Powered by News API

        News API Key: d1159719ec474bf1b82575b5b8478bef
        Default GET: https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey={API_KEY}
        API has two options: source, sortBy [to change these options you can modify the GET URL]
        '''
        
import urllib2
import json

response = urllib2.urlopen("https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=d1159719ec474bf1b82575b5b8478bef")
data = json.load(response)

for i in range(len(data["articles"])):
    print data["articles"][i]["title"]
