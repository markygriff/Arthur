# Arthur

You👏Don't👏Know👏ChatBots👏Unless👏You👏Know👏Arthur. 

## Dependencies

    $ pip install -r requirements.txt

## Description

Arthur is a Facebook messenger ChatBot that'll help you have that wonderful kind of day ☀️
> Having fun isn't hard when you've got a library card 

## Setting up a Facebook app for Facebook messenger

* You're going to need a publicly routed https address. We used [ngrok](https://ngrok.com/) to create a tunnel to our local machine.
* The server will need to be started for you to verify the webhook.

        $ python server.py
     
* Follow the instructions provided in the [Facebook quickstart tutorial](https://developers.facebook.com/docs/messenger-platform/quickstart) for creating a page and an app.
* Set the `ACCESS_TOKEN` and `VERIFY_TOKEN` environment variables to the values you get from following the tutorial.

## Authors

Mark Griffith.

Jordan Lane.
