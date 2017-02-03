from flask import Flask, request
from arthur import Arthur
import requests
import json
from nltk.corpus import brown

app = Flask(__name__)

ACCESS_TOKEN = "EAACZBlPXesb0BAPlCChQCOYSBO687GxNdET6MduVZAs7F1zazZB4qym4qmgHRsrKMTryw3JTZCw4LhVVw4Hz9z2L06OkWiO8zzTE4wr0IuZBN7x81kx5f4iLtNraeVpAcVMCH77lKMKvEbYZAWPoIgPfUaG7wnJVipXxbT7jEH0gZDZD"
VERIFY_TOKEN = 'secret'

arthur = Arthur(brown.words())

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')

def messaging_events(payload):
    '''
    Generate tuples of (sender_id, message_text) from the payload.
    '''
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"]

def send_message(recipient, text):
    '''
    Send the message text to recipient.
    '''
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": ACCESS_TOKEN},
        data=json.dumps({
            "recipient": {"id": recipient},
            "message": {"text": text}
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    payload = request.get_data()
    for sender, message in messaging_events(payload):
        print "Incoming from %s: %s" % (sender, message)
        if arthur.questing == False:
            response = arthur.handle_input(message)
        else:
            print "MESSAGE <", message, ">"
            response = arthur.respond_to(message)
            arthur.questing = False
        print "Outgoing to %s: %s" % (sender, response)
        send_message(sender, response)
        break
    return "ok"

# @app.route('/', methods=['POST'])
# def greeting():
#     # "Content-Type": "application/json" {
#     # "setting_type":"greeting",
#     # "greeting":{ "text": "Arthur Is Your Friend."}
#
#     r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings",
#         params={"access_token": ACCESS_TOKEN},
#         data=json.dumps({
#             "setting_type": "greeting",
#             "greeting":{ "text": "ARTHUR."}
#         }),
#         headers={'Content-type': 'application/json'})
#     if r.status_code != requests.codes.ok:
#         print r.text

@app.route('/', methods=['GET'])
def handle_verification():
    print "Handling Verification."
    if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
        print "Verification successful!"
        return request.args.get('hub.challenge', '')
    else:
        print "Verification failed!"
        return 'Error, wrong validation token'

if __name__ == '__main__':
    app.run(debug=True)
