import string
import topnews_controller

class Arthur:

    def __init__(self):
        self.fn_dict = {"uber": self.do_uber, "news": self.do_news, "weather": self.do_weather}
        self.questing = False

    def input_handler(self, msg):
        '''
        params:
            msg - input string for arthur to handle
        returns:
            reply - reply to recipient
        '''
        refine_msg = msg.translate(None, string.punctuation).lower()
        #Scan input -> run function

        for word in refine_msg.split(" "):
            if word in self.fn_dict:
                self.questing = True
                self.fn_dict[word]();
                break
            else: self.question = False
        return


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
    x.input_handler(prompt)
    
