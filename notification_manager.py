from twilio.rest import Client
import os
import requests

TWILIO_SID = os.environ.get("TWILIO_ACNT_ID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "+15345444344"
TWILIO_VERIFIED_NUMBER = "+15206390031"
class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)