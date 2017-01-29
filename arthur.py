import string
import topnews_controller

class Arthur:

    def __init__(self):
        self.dict = {"uber": [self.do_uber, "From Where to Where?"], "news": [self.do_news,"What news source?"], "weather": [self.do_weather, "Where?"], "stock": [self.do_stock, "Company's ticker symbol?"]}

    def action(self,word,info):
        self.dict[word][0](info)


    def classify_input(self,msg):
        refine_msg = msg.translate(None, string.punctuation).lower()

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

    def do_uber(self, info):
        '''TODO: Ask user start and end locations [How do we ask the user?]
        '''
        print "uber"

    def do_news(self, info):
        print topnews_controller.get_top_news()

    def do_places(self, info):
        print "places"

    def do_stock(self, info):
        print "stock"

    def do_weather(self, info):
        print "weather"

if __name__ == '__main__':
    x = Arthur()
    prompt = raw_input("Prompt: ")
    msg = raw_input("Msg: ")
    x.action(prompt, msg)
