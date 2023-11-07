import pathlib

from openai import OpenAI

client = OpenAI()

def system_msg(message):
    return {
        "role": "system",
        "content": message,
    }

def user_msg(message):
    return {
        "role": "user",
        "content": message,
    }

def completion(messages):
    return client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    ).choices[0].message.content
    

