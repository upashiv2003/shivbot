import nltk
from nltk.chat.util import Chat, reflections
import requests
import random

# Download the necessary NLTK data files

# Define pairs of patterns and responses
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
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Alright, that's good to know!",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["I was created by a developer called Shiv Upadhyay",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am not tied to any specific location.",]
    ],
    [
        r"how is the weather in (.*)",
        ["I don't have real-time data, but you can check a weather app for the current conditions in %1.",]
    ],
    [
        r"(.*) help (.*)",
        ["I can help with general information and answering questions. What do you need help with?",]
    ],
    [
        r"(.*) (hungry|food) ?",
        ["I don't eat, but I can suggest some recipes if you're hungry!",]
    ],
    [
        r"(.*) (sleepy|tired) ?",
        ["Maybe you should take a nap or get some rest.",]
    ],
    [
        r"(.*) (happy|joyful) ?",
        ["That's great to hear! What's making you happy?",]
    ],
    [
        r"(.*) (sad|unhappy) ?",
        ["I'm sorry to hear that. Is there anything I can do to help?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Can you please rephrase?",]
    ]
]

# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    api_key = "066328aa5a264a03a8f976d6112b2977"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    else:
        return "Sorry, I couldn't fetch the weather data."

# Create the chatbot
def shivbot():
    print("Hi, I'm ShivBot. How can I help you today?")
    chat = Chat(pairs, reflections)
    
    while True:
        user_input = input("> ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print(random.choice(["Bye, take care. See you soon :) ", "It was nice talking to you. See you!"]))
            break
        
        # Check for weather query
        if "weather" in user_input.lower():
            city = user_input.split("in")[-1].strip()
            response = get_weather(city)
            print(response)
        else:
            response = chat.respond(user_input)
            if response:
                print(response)
            else:
                print("I'm not sure how to respond to that. Can you please rephrase?")

if __name__ == "__main__":
    shivbot()