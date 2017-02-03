import string
import topnews_controller
import phrases
import uber_controller
import places_controller
import stock_controller

import nltk
import re


class Arthur:

    '''

        Currently our code is working great, we are able to interact with Arthur and
            get information from our supported APIs.

        MINOR TODOS:

            - Have smaller version of the arthurlogo.png for the README
            - Expand the README to explan how to interact with Arthur's functionality

        BIG TODOS:

            - Clean up our code. Although our code works, it is currently very
            choppyand not very clean. This is a large task, but I believe that it
            is important before adding on anymore funcitonality.

            - Expand converation ability

            - Add-on new APIs

    '''

    def __init__(self, data):
        self.dict = {"uber": [self.do_uber, "From Where to Where?"], "news": [self.do_news,"Which news source?"], "weather": [self.do_weather, "Where?"], "stock": [self.do_stock, "Company's ticker symbol?"], "restaurant": [self.do_places, "Bar or Dine?"]}
        self.quest_word = None
        self.questing = False
        #tokens = nltk.word_tokenize(data)
        self._model = nltk.model.ngram.NgramModel(3, data)
        #self._model = None

    def respond_to(self, msg):
        result = self.dict[self.quest_word][0](msg)
        string = "Here's what I got for ya pal!\n\n"
        for i in result[:5]:
            string += "> " + i + "\n\n"
        return string

    def determine_response(self, message):
        # Pick a random word from the incoming message
        input_tokens = nltk.word_tokenize(message)
        keyword = random.choice(input_tokens)

        # Use keyword and input length to seed a response
        input_length = len(input_tokens)
        num_response_words = int(random.gauss(input_length, input_length / 2)) + 1
        print "Basing response on keyword %s and length %d" % (keyword, num_response_words)
        content = self._model.generate(num_response_words, (keyword,))
        return self._format_response(content)

    def _format_response(self, content):
        def to_unicode(x):
            if isinstance(x, str):
                return x.decode('utf-8')
            return x

        s = u' '.join([to_unicode(c) for c in content])
        s = re.sub(r' ([\?,\.:!])', r'\1', s)  # Remove spaces before separators
        return s

    def handle_input(self,msg):
        refine_msg = msg.lower()
        for word in refine_msg.split(" "):
            if word in self.dict:
                self.quest_word = word
                self.questing = True
                return [self.dict[word][1], word][0] # follow up question
        self.quest_word = None
        self.questing = False
        return determine_response(msg)


    def do_uber(self, route):
        '''TODO: Ask user start and end locations [How do we ask the user?]
        '''
        # Hardcoded Input: "Start" to "End"
        route = route.split(" to ")
        return uber_controller.get_prices(route[0], route[1]);


    def do_news(self, news_source):
        return topnews_controller.get_top_news(news_source)


    def do_places(self,category):
        places_fn = getattr(places_controller,'get_places_'+category.lower())
        return places_fn()

    def do_stock(self, ticker_symbol):
        return stock_controller.get_latest_price(ticker_symbol)


    def do_weather(self, location):
        print "weather"

if __name__ == '__main__':
    x = Arthur()
    #prompt = raw_input("Prompt: ")
    msg = raw_input("Msg: ")
    x.quest_word = "stock"
    result = x.respond_to(msg)
    print(result)
