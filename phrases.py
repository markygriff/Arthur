# Dependencies:
#   sudo pip install textblob
#   python -m textblob.download_corpora

GREETINGS = ["hello","hi","hey","sup","greetings","howdy"]
GOODBYES = ["goodbye, bye", "cya"]
DEFAULT_RESPONSES = ["I'm sorry, I don't quite understand what you mean.", "huh...?", "I'm not that smart yet, sorry!", "*stares at you wantingly*"]
GREETING_RESPONSES = ["I. Am. Arthur.", "Hey buddy!", "Hey there, what can I do for ya?","Howdy!"]
RESPONSES_ABOUT_USER = ["Ok!","Swell!","I'm a meme!","Thanks...?"]

PRONOUNS = ["PRP","PRP$","WP","WP$"]
NOUNS = ["NN","NNS","NNP","NNPS"]
ADJECTIVES = ["JJ","JJR","JJS"]
# VERBS = ["VB","VBD","VBG","VBN","VBP","VBZ"]
VERBS = ["VB","VBD"]

from textblob import TextBlob
import random

def check_for_greeting(msg):
    for word in msg.split(" "):
        if word.lower() in GREETINGS:
            return random.choice(GREETING_RESPONSES)

def determine_response(msg):
    # clean = preprocess_text(msg)
    blob = TextBlob(msg)
    pronoun, noun, adjective, verb = find_candidate_parts_of_sentence(blob)
    print pronoun, noun, adjective, verb
    # check for comment directly targeted towards our bot
    # resp = check_for_direct_comment(pronoun, noun, adjective)
    resp = None
    if not resp:
        resp = check_for_greeting(blob)
    if not resp:
        # no pronoun
        if not pronoun:
            resp = random.choice(DEFAULT_RESPONSES)
        # user said something about the bot
        elif pronoun == "I" and not verb:
            resp = random.choice(RESPONSES_ABOUT_USER)
        else:
            # resp = construct_response(pronoun, noun, verb)
            resp = random.choice(DEFAULT_RESPONSES)
    if not resp:
        resp = random.choice(DEFAULT_RESPONSES)
    return resp

def check_for_direct_comment(pronoun, noun, adjective):
    return None

def construct_response(pronoun, noun, verb):
    return None

def find_candidate_parts_of_sentence(blob):
    pronoun = None
    noun = None
    verb = None
    adjective = None
    for sentence in blob.sentences:
        pronoun = find_pronoun(sentence)
        noun = find_noun(sentence)
        adjective = find_adjective(sentence)
        verb = find_verb(sentence)
    return pronoun,noun,adjective,verb

def find_pronoun(sent):
    pronoun = None
    for word, pos in sent.pos_tags:
        if pos == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        if pos == 'PRP' and word == 'I':
            pronoun = 'You'
    return pronoun

def find_noun(sent):
    noun = None
    for word, pos in sent.pos_tags:
        if pos in NOUNS:
            noun = word
            if random.choice([0,1]) == 0:
                return noun
    return noun

def find_adjective(sent):
    for word, pos in sent.pos_tags:
        if pos in ADJECTIVES:
            return word

def find_verb(sent):
    for word, pos in sent.pos_tags:
        if pos in VERBS:
            return word

if __name__ == '__main__':
    msg = raw_input()
    print determine_response(msg)
