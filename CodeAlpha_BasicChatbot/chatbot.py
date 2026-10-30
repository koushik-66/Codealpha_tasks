
# CodeAlpha Internship
# Project: Basic Chatbot

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! Welcome. How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input in ["i am fine", "i'm fine", "fine"]:
        return "That's great! How can I help you today?"

    elif user_input in ["what is your name", "who are you"]:
        return "I'm CodeBot, your friendly Python chatbot!"

    elif user_input in ["what can you do", "help"]:
        return "I can chat with you. Try saying hello, how are you, or bye."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! Happy to help."

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a wonderful day!"

    else:
        return "Sorry, I don't understand that. Please try something else."


def start_chatbot():

    print("=" * 45)
    print("       WELCOME TO CODEBOT")
    print("          BASIC CHATBOT")
    print("=" * 45)

    print("\nCodeBot: Hello! I'm CodeBot.")
    print("CodeBot: Type 'bye' to end the conversation.")

    while True:

        user_input = input("\nYou: ")

        if not user_input.strip():
            print("CodeBot: Please enter something.")
            continue

        response = chatbot_response(user_input)

        print("CodeBot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break

    print("\nChat session ended. Thank you!")


if __name__ == "__main__":
    start_chatbot()
