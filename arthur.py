import string
import topnews_controller
import phrases
import uber_controller

class Arthur:

    def __init__(self):

        self.dict = {"uber": [self.do_uber, "From Where to Where?"], "news": [self.do_news,"What type of news?"], "weather": [self.do_weather, "Where?"], "stock": [self.do_stock, "Company's ticker symbol?"], "restaurant": [self.do_places, "Bar or Dine?"]}
        self.quest_word = None
        self.questing = False

    def respond_to(self, msg):
        return self.dict[self.quest_word][0](msg)


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
        print(route)
        print "uber"


    def do_news(self, type_of_news):
        print topnews_controller.get_top_news()

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
