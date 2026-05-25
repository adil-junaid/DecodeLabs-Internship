print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm doing great!",
    "what is your name": "I'm DecodeBot.",
    "help": "You can say hello, ask my name, or type bye.",
    "good morning": "Good morning! ☀️",
    "good night": "Good night! 🌙",
    "thanks": "You're welcome!",
    "who created you": "I was created by Adil during DecodeLabs Internship.",
    "what can you do": "I can answer simple predefined questions.",
    "bye": "Goodbye! Have a nice day!"
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", reply)