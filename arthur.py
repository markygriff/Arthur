import string
import topnews_controller
import phrases
import uber_controller


class Arthur:

    def __init__(self):

        self.dict = {"uber": [self.do_uber, "From Where to Where?"], "news": [self.do_news,"WWhich news source?"], "weather": [self.do_weather, "Where?"], "stock": [self.do_stock, "Company's ticker symbol?"], "restaurant": [self.do_places, "Bar or Dine?"]}
        self.quest_word = None
        self.questing = False

    def respond_to(self, msg):
        result = self.dict[self.quest_word][0](msg)
        string = "Here's what I got for ya pal!\n\n"
        for i in result:
            string += "> " + i + "\n\n"
        return string



    def handle_input(self,msg):
        refine_msg = msg.lower()
        for word in refine_msg.split(" "):
            if word in self.dict:
                self.quest_word = word
                self.questing = True
                return [self.dict[word][1], word][0] # follow up question
        self.quest_word = None
        self.questing = False
        return phrases.determine_response(msg)


    def do_uber(self, route):
        '''TODO: Ask user start and end locations [How do we ask the user?]
        '''
        # Hardcoded Input: "Start" to "End"
        route = route.split(" to ")
        return uber_controller.get_prices(route[0], route[1]);



    def do_news(self, news_source):
        return topnews_controller.get_top_news(news_source)


    def do_places(self,category):
        print "places"

    def do_stock(self, ticker_symbol):
        print "stock"

    def do_weather(self, location):
        print "weather"

if __name__ == '__main__':
    x = Arthur()
    prompt = raw_input("Prompt: ")
    msg = raw_input("Msg: ")
    x.action(prompt, msg)
