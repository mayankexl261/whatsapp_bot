from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()  # this loads variables from your .env file into the environment

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")

print("SID:", TWILIO_SID)
print("Token:", TWILIO_AUTH_TOKEN)
print("Number: ", TWILIO_WHATSAPP_NUMBER)


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
print(client.api.accounts.list(limit=1))