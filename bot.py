import os
import json
import numpy as np
import requests
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from time import ctime
import colorama

colorama.init()
from colorama import Fore, Style, Back

import random
import main as bot
import pickle

# Set your OpenAI API key
api_key = "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"

with open("intents.json") as file:
    data = json.load(file)

def generate_response(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": message,
        "max_tokens": 50
    }

    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers=headers,
        json=data
    )

    response_data = response.json()
    if "choices" in response_data:
        choices = response_data["choices"]
        if len(choices) > 0 and "text" in choices[0]:
            return choices[0]["text"]

    return ""

def chat(message):
    # Load your OpenAI API key
    openai.api_key = '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'

    # Define the list of tags with empty responses
    empty_response_tags = ["time", "questions"]

    if message.lower() == "random question":
        # Generate a random question here
        random_question = "What is the capital of France?"

        # Process the random question and generate a response
        response = generate_response(random_question)
        return response
    else:
        for i in data['intents']:
            if i['tag'] in empty_response_tags:
                response = generate_response(message)
                return response
            elif i['tag'] == ['questions']:
                return bot.getMessage(message)
            elif i['tag'] == api_key:
                return generate_response(message)
            elif i['tag'] == ['time']:
                return ctime()
            else:
                return np.random.choice(i['responses'])

# Usage example
response = chat("Hello")
print(response)