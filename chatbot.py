import nltk # To import the Natural Language Toolkit library
from nltk.chat.util import Chat, reflections # To import Chat and reflections from nltk.chat.util

nltk.download('punkt')  # Downloading the 'punkt' tokenizer data ( It is commonly used for tasks such as text processing, natural language understanding, and text analysis.) 
# # Defining pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a bot created by you. You can call me Chato.",]
    ],
    [
        r"who|Who is younas|Younas?",
        ["Younas is a Python Programming developer and a Data Scientist in Pakistan.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that!", "How can I help you today?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon.",]
    ],
    [   r"what (.*) want?",
        ["I want to help you with your queries.", "I'm here to assist you with anything you need.",]
    ],
    [
        r"(.*) created you?",
        ["I was created by a Younas the python developer.", "I'm a creation of a skilled programmer using Python.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual assistant, I don't have a physical location.",]
    ],
    [
        r"how is the weather in (.*)?",
        ["I'm not sure, but you can check a weather website.",]
    ],
    [
        r"(.*) (help|support)",
        ["Sure, I'm here to help! What do you need assistance with?",]
    ],
    [
        r"(.*) (movie|actor)?",
        ["I'm a bot, but I can look up information for you if you'd like.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon.", "Goodbye! Have a great day!",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Happy to help!",]
    ],
    [
        r"(.*) (sports|game)",
        ["I'm not into sports, but I can find some information for you if you'd like.",]
    ],
    [
        r"who are you?",
        ["I'm your friendly chatbot here to assist you.", "I'm a virtual assistant created to help you with your queries.",]
    ],
    [
        r"(.*) music",
        ["I love all kinds of music! What about you?",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you get if you cross a snowman and a vampire? Frostbite.",]
    ],
    [
        r"goodbye|bye",
        ["Goodbye! Have a great day!", "Bye! Take care!",]
    ],
    [
        r"how old are you?",
        ["I'm timeless!", "Age is just a number. I'm as old as the internet!",]
    ],
    [
        r"(.*) hobby?",
        ["I love chatting with people like you!", "My hobby is learning new things and helping users.",]
    ],
    [
        r"(.*) favorite color?",
        ["I like all colors, but I think blue is calming and what is your favorite color?", "Colors are beautiful, aren't they? I think green is refreshing.",]
    ],
    [
        r"what is your purpose?",
        ["My purpose is to assist you with any questions you have.", "I'm here to make your life easier by providing information and support.",]
    ]
]
# Reflections dictionary to swap pronouns
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

def chatbot():
    print("Hi, I am your chatbot created by Younas the Python Developer. You can type 'quit' to exit.") # Greeting message
    chat = Chat(pairs, reflections) # Creating a Chat object with pairs and reflections
    chat.converse() # Starting the conversation with the chatbot

if __name__ == "__main__": # Main entry point of the script
    chatbot() # Calling the chatbot function to start the chatbot
