from ai import get_answer

continue_conversation = True
total_questions = 0

while continue_conversation:
    display_message = "Hello I am your local AI Assistant. How may I help you?" if total_questions == 0 else "What else would you like to know?"
    print(display_message, end="\n")
    question = input()
    total_questions += 1

    respone = get_answer(question)
    print(respone, end="\n")
    print("-"*50, end="\n")

    print("Do you have any other question? (yes/no)", end="\n")
    answer = input()

    if answer.lower() == "no":
        continue_conversation = False