def get_valid_input(question): #this helps me get input from member and hold it in the value 
    value = 0
    while value < 1 or value > 4:
        try:
            value = int(input(question + " "))
            if value < 1 or value > 4:# does it meet the criteria 
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")# error handing 
    return value



def load_questions(filename):
    questions = []
    with open(filename, "r") as file:
        for line in file:
            clean_line = line.strip()#Strip is important given that python is space sensetive it removes any space after a line
            if clean_line:          # only add if NOT empty
                questions.append(clean_line)
    return questions


def take_assessment():
    questions = load_questions("questions.txt")
    answers = []

    print("\n--- Skill Assessment ---")

    for q in questions:
        answers.append(get_valid_input(q))

    score = sum(answers)
    average = score / len(answers)

    print("\n--- Results ---")
    print("Total score:", score)
    print("Average score:", round(average, 2))

    if average < 2:
        print("Level: Beginner")
    elif average < 3:
        print("Level: Intermediate")
    else:
        print("Level: Advanced")


def show_instructions():
    print("\n--- Instructions ---")
    print("• Answer each question using numbers from 1 to 4")
    print("• 1 = Very Low")
    print("• 4 = Very High")
    print("• Your average score determines your level\n")


# ===== MAIN MENU =====
while True:
    print("\n=== MAIN MENU ===")
    print("1. Take Skill Assessment")
    print("2. View Instructions")
    print("3. Exit")

    choice = input("Choose an option (1–3): ")

    if choice == "1":
        take_assessment()

    elif choice == "2":
        show_instructions()

    elif choice == "3":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
