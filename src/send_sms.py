# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
# from dotenv import load_dotenv
import os

# load_dotenv(verbose=True)


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ.get('JASON_SID')
auth_token = os.environ.get('JASON_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
         from_="+17864813303",
         to='+17867044247'
     )

print(account_sid)