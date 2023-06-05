import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wikipedia as wiki
from googlesearch import search
import warnings
import pickle
import os
import requests
from time import ctime

warnings.filterwarnings('ignore')
nltk.download("punkt", quiet=True)

# Set your OpenAI API key
api_key = "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"

with open('intents.json') as file:
    data = json.load(file)

def greeting_response(text):
    text = text.lower()
    bot_greetings = ['Hi', 'Hello! How can I assist you as a student?', 'Hey there!', 'Hi, how can I help you with your studies?']
    user_greetings = ['hi', 'hello', 'hey', 'hy', 'halo', 'hi there']
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index

def bot_reply(message, sentence_list):
    message = message.lower()
    sentence_list.append(message)
    bot_reply = ' '
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_score = cosine_similarity(cm[-1], cm)
    similarity_score_list = similarity_score.flatten()
    index = index_sort(similarity_score_list)
    index = index[1:]
    reply_flag = 0
    j = 0
    for i in range(len(index)):
        if similarity_score_list[index[i]] > 0.0:
            bot_reply = bot_reply + " " + sentence_list[index[i]]
            reply_flag = 1
            j = j + 1
        if j > 4:
            break
    if reply_flag == 0:
        bot_reply = bot_reply + " " + "Sorry, I don't have an answer"
    sentence_list.remove(message)
    return bot_reply

def getText(message):
    i = 0
    response = search(message)
    token_list1 = []
    token_list2 = []
    for link in response:
        try:
            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            sentence_list = article.text
            token_list1.extend(nltk.sent_tokenize(sentence_list))
        except Exception:
            i = i + 1
        finally:
            i = i + 1
            if i > 1:
                break
    try:
        sentence_list = wiki.summary(message)
        sentence = nltk.sent_tokenize(sentence_list)
        if sentence is not None:
            token_list2.extend(sentence)
    except wiki.PageError:
        print("Error occurred")
    finally:
        return token_list1 + token_list2

def generate_openai_response(message):
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

def getMessage(message):
    close_chat = ['bye', 'goodbye', 'exit', 'quit']
    if message.lower() in close_chat:
        return "See you later, bye !!"
    else:
        if greeting_response(message) is not None:
            return greeting_response(message)
        elif any(map(str.isdigit, message)):
            return eval(message)
        else:
            sentence = getText(message)
            reply = bot_reply(message=message, sentence_list=sentence)

            # Use OpenAI for generating response
            openai_response = generate_openai_response(message)
            if openai_response:
                reply += " " + openai_response

            return reply

model = keras.models.load_model('chat_model')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)
max_len = 20

while True:
    user_input = input("User: ")
    result = model.predict(pad_sequences(tokenizer.texts_to_sequences([user_input]),
                                         truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    for i in data['intents']:
        if tag == ['questions']:
            print(getMessage(user_input))
        elif tag == ["time"]:
            print(ctime())
        elif i['tag'] == tag:
            print(random.choice(i['responses']))
            break
    else:
        print(generate_openai_response(user_input))