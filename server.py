from flask import Flask, request
from arthur import Arthur
import requests
import json

app = Flask(__name__)

ACCESS_TOKEN = "EAACZBlPXesb0BALRYMeooVhYbScAAJFXd3ZBAJHxZCrD3ZAK5sGyrkeD8WnI3Mck5fr98AHryCJC8lBE9VfQqTWsU9oPSqQpeNxrDhlXTd4Br4ewyzOfLXB3e03eRrzFvSuA6pyFVTw6AukSjh4a5Jfe8XrhlAYXxFGrHnoZAiwZDZD"
VERIFY_TOKEN = 'secret'

arthur = Arthur()

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
    if request.args.get('hub.verify_token', '') == 'VERIFY_TOKEN':
        print "Verification successful!"
        return request.args.get('hub.challenge', '')
    else:
        print "Verification failed!"
        return 'Error, wrong validation token'

if __name__ == '__main__':
    app.run(debug=True)
