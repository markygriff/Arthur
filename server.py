from flask import Flask, request
from arthur import Arthur

arthur = Arthur()

app = Flask(__name__)

from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAACZBlPXesb0BALRYMeooVhYbScAAJFXd3ZBAJHxZCrD3ZAK5sGyrkeD8WnI3Mck5fr98AHryCJC8lBE9VfQqTWsU9oPSqQpeNxrDhlXTd4Br4ewyzOfLXB3e03eRrzFvSuA6pyFVTw6AukSjh4a5Jfe8XrhlAYXxFGrHnoZAiwZDZD"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply_msg = arthur.input_handler(message)
    reply(sender, reply_msg)
    return "ok"

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
