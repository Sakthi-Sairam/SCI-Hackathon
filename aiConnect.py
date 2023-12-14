import speech_recognition as sr
import os
import webbrowser
import openai
from constants import apikey
import datetime
import random
import pyttsx3
import numpy as np

engine = pyttsx3.init()
chatStr = ""
r = sr.Recognizer()
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"USER: {query}\n Science BOT: "
    response = openai.completions.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    engine.say(response.choices[0].text)
    engine.runAndWait()
    print(response.choices[0].text)
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        print("Not found")
        pass

if __name__ == '__main__':
    print('Welcome to Science BOT')
    say("Science Bot")
    i=0
    while i<1:
        i+=1
        print("Listening...")
        query = takeCommand()
        print("Chatting...")
        chat(query)
