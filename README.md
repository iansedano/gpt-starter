# OpenAI Chatbot

This script provides a simple interface to chat with OpenAI's GPT-3.5-turbo model. It allows users to have a conversation with the model and quit the conversation by typing "exit".

## Prerequisites

You need to have Python installed.
Install openai Python library using pip:

```
pip install openai
```

## Setup

Make sure you have an OpenAI API key.
Store your API key in a secret.py file as key = 'YOUR_API_KEY'.

## How to Run

Execute the script using Python:

```
python chat_bot.py
```

Once you run the script, it will prompt you with User: . You can then start typing and the chatbot will respond. To exit the conversation, simply type exit.

## Usage Example

```
Welcome! Let's start a new chat...(Type 'exit' to quit)
User: Hello!
Chatbot: Hello! How can I help you today?
User: What's the weather like?
Chatbot: I'm sorry, I cannot check real-time weather. Would you like information on how weather systems work instead?
User: exit
```

## Feedback and Contributions

For any feedback or contributions to this script, please open a pull request or raise an issue in this repository.

