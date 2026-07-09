import json
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "intents.json"), "r") as file:
    intents = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."