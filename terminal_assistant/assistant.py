from ai import get_answer

continue_conversation = True
is_first_question = True

while continue_conversation:
    display_message = "Hello I am your local AI Assistant. How may I help you?" if is_first_question else "What else would you like to know?"
    print(display_message, end="\n")
    question = input()
    is_first_question = False

    response = get_answer(question)
    print(response, end="\n")
    print("-"*50, end="\n")

    print("Do you have any other question? (yes/no)", end="\n")
    answer = input()

    if answer.lower() == "no":
        continue_conversation = False