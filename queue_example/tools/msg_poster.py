from random import choice
import requests
from datetime import datetime


URL = "http://127.0.0.1:5000/messages"
GREETINGS = [
    "Hello",
    "Wsup",
    "What's Happening",
    "What's going on",
    "You Good",
    "Hola"
]

def post_greeting():
    greeting ={"message": ""}
    greeting["timestamp"] = datetime.now().strftime("%F %H:%M:%S")
    greeting = choice(GREETINGS)
    repsonse =requests.post(URL, json=greeting)
    if repsonse.status_code == 204:
        print("Message posted.")
    else:
        print("Error received.")

if __name__ == "__main__":
    for _ in range(100):
        post_greeting()