def chatbot():
    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello there!",
        "how are you": "I'm doing great!",
        "what is ai": "AI stands for Artificial Intelligence.",
        "your name": "I am a simple chatbot.",
        "bye": "Goodbye! Have a nice day."
    }

    print("ChatBot Started (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        found = False

        for key in responses:
            if key in user_input:
                print("Bot:", responses[key])
                found = True

                if key == "bye":
                    return

                break

        if not found:
            print("Bot: Sorry, I don't have a response for that.")

chatbot()
