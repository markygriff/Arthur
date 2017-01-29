from flask import Flask, request
from arthur import Arthur
import requests
import json
arthur = Arthur()

app = Flask(__name__)

ACCESS_TOKEN = "EAACZBlPXesb0BALRYMeooVhYbScAAJFXd3ZBAJHxZCrD3ZAK5sGyrkeD8WnI3Mck5fr98AHryCJC8lBE9VfQqTWsU9oPSqQpeNxrDhlXTd4Br4ewyzOfLXB3e03eRrzFvSuA6pyFVTw6AukSjh4a5Jfe8XrhlAYXxFGrHnoZAiwZDZD"

# def reply(user_id, msg):
#     data = {
#         "recipient": {"id": user_id},
#         "message": {"text": msg}
#     }
#     resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
#     print(resp.content)

# @app.route('/', methods=['POST'])
# def handle_incoming_messages():
#     data = request.json
#     sender = data['entry'][0]['messaging'][0]['sender']['id']
#     message = data['entry'][0]['messaging'][0]['message']['text']
#     if ACTION_WORD == None:
#         reply_msg, ACTION_WORD = arthur.classify_input(message) # returns None if not action prompt
#         if ACTION_WORD == None:
#             reply_msg = phrases.determine_response(message)
#     else:
#         reply_msg = arthur.action(ACTION_WORD,message)
#     reply(sender, reply_msg)
#     return 'ok'



def messaging_events(payload):
    """Generate tuples of (sender_id, message_text) from the
    provided payload.
    """
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"]

def send_message(recipient, text):
    """Send the message text to recipient with id recipient.
    """
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
    if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
    # if request.args.get('hub.verify_token', '') == 'secret':
        print "Verification successful!"
        return request.args.get('hub.challenge', '')
    else:
        print "Verification failed!"
        return 'Error, wrong validation token'

if __name__ == '__main__':
    app.run(debug=True)
