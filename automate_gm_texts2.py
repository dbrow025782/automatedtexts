##import twilio client, schedule api, & random library
from twilio.rest import Client
import random, schedule

##save messages into strings
good_morning_quotes = [
"Grand rising",
"Bless up everybody",
"Rise and grind family"
]

#your twilio # comes from the twilio website
cellphone = #enter your recipient's # here
twilio_number = #enter your twilio #


#your account sid & token both come from twilio
def send_message(quote):
	account: #enter account number here
	token: #enter token here
	client: Client(account,token)

	client.messages.create(to=cellphone,from_=twilio_number,body=quote)

random_quote = good_morning_quotes[random.randint(0, len(good_morning_quotes))]
schedule.every().day.at("12:22").do(send_message,random_quote)