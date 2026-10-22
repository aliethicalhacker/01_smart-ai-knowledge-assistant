
"""
Smart AI Knowledge Assistant
Part 1 of 10: Python Foundations
Author: Ali Naeem
"""

def show_welcome():
    print("=" * 45)
    print("   SMART AI KNOWLEDGE ASSISTANT")
    print("   Part 1: Python Foundations")
    print("=" * 45)
    print("Type 'help' to see commands.")
    print("Type 'exit' to quit.")


def get_response(question):
    question = question.strip().lower()

    if not question:
        return "Please enter a question."

    elif question in ("hello", "hi", "hey"):
        return "Hello! How can I help you today?"

    elif question in ("help", "commands"):
        return (
            "Available commands:\n"
            "- hello: Greet the assistant\n"
            "- about: Learn about the project\n"
            "- name: Get a personalized greeting\n"
            "- help: Show commands\n"
            "- exit: Close the assistant"
        )

    elif question == "about":
        return (
            "I am a Python-based assistant prototype.\n"
            "Future versions will use machine learning "
            "and language models."
        )

    elif question == "name":
        name = input("Assistant: What is your name? ").strip()

        if name:
            return f"Nice to meet you, {name}!"

        return "You didn't enter a name."

    else:
        return (
            "I don't know how to answer that yet.\n"
            "We'll add real AI capabilities in later parts!"
        )


def main():
    show_welcome()

    while True:
        question = input("\nYou: ")

        if question.strip().lower() == "exit":
            print("Assistant: Goodbye! Keep learning AI.")
            break

        response = get_response(question)
        print(f"\nAssistant: {response}")


if __name__ == "__main__":
    main()
