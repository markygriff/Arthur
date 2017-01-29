class Arthur:

    def __init__(self):
        self.fn_dict = {"Uber": self.do_uber, "Movies": self.do_movies, "Weather": self.do_weather}
        self.questing = False
        self.

    def input_handler(self, msg):
        '''
        params:
            msg - input string for arthur to handle
        returns:
            reply - reply to recipient
        '''

        reply_msg = "Sorry, I don't quite understand you."
        # first figure out whether arthur is required to carry out a quest
        for word in msg.split(" "):
            if word in trigger_words:
                self.questing = True
                trigger_word = word
                break
            else: self.question = False
        return reply_msg


    def greeting(self):
        print "Hello, I'm Arthur."
        fn = raw_input("Is there anything I can do for you?")
        init_fn(fn)

    def init_fn(self, fn):
        a = fn_dict[fn]
        a()

    def do_uber(self):
        print "uber"

    def do_movies(self):
        print 'movies'

    def do_weather(self):
        print "weather"

if __name__ == '__main__':
    greeting()
