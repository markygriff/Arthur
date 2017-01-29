import string
import topnews_controller

class Arthur:

    def __init__(self):
        self.dict = {"uber": [self.do_uber, "From Where to Where?"], "news": [self.do_news,"What type of news?"], "weather": [self.do_weather, "Where?"], "stock": [self.do_stock, "Company's ticker symbol?"]}
        self.questing = False

    def action(self,msg):
        self.dict[word][0]()


    def classify_input(self,msg):
        refine_msg = msg.translate(None, string.punctuation).lower()

        follow_up = None
        word = None

        for word in refine_msg.split(" "):
            if word in self.dict:
                return [self.dict[word][1], word]

        return [None, None]

    def greeting(self):
        print "Hello, I'm Arthur."
        fn = raw_input("Is there anything I can do for you?")
        init_fn(fn)

    def init_fn(self, fn):
        a = fn_dict[fn]
        a()

    def do_uber(self):
        '''TODO: Ask user start and end locations [How do we ask the user?]
        '''
        print "uber"

    def do_news(self):
        print topnews_controller.get_top_news()

    def do_places(self):
        print "places"

    def do_stock(self):
        print "stock"

    def do_weather(self):
        print "weather"

if __name__ == '__main__':
    x = Arthur()
    prompt = raw_input("Prompt: ")
    x.classify_input(prompt)
