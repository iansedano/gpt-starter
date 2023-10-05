from secret import key
import openai

openai.api_key = key

def chat():
    """Creates a conversation with openai api."""
    
    chatbot_conversation = []

    while True:
        user_input = input ("User: ")
        if user_input.lower() == "exit":
            break

        chatbot_conversation.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chatbot_conversation
        )

        chatbot_repsonse = response["choices"][0]["message"]["content"]
        print(f"Chatbot: {chatbot_repsonse}")
        chatbot_conversation.append({"role": "assistant", "content": chatbot_repsonse})

if __name__ == "__main__":
    print("Welcome! Let's start a new chat...(Type 'exit' to quit)")
    chat()


