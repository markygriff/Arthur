def greeting():
    print "Hello, I'm Arthur."
    fn = raw_input("Is there anything I can do for you?")
    init_fn(fn)

def init_fn(fn):
    a = fn_dict[fn]
    a()

def do_uber():
    print "uber"

def do_movies():
    print 'movies'

def do_weather():
    print "weather"

fn_dict = {"Uber": do_uber(), "Movies": do_movies, "Weather": do_weather}

if __name__ == '__main__':
    greeting()
