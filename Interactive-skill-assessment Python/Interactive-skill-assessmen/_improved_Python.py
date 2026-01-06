


answer = 0
question2 = 0
question3 = 0 
score = 0

def get_valid_input(question):
    value = 0                     # 1️⃣ start invalid
    while value < 1 or value > 4: # 2️⃣ validate the ANSWER
        value = int(input(question))  # 3️⃣ ask question
    return value                  # 4️⃣ return clean value

questions = [
    "Rate your technical skill (1–4): ",
    "Any degree? (1–4): ",
    "How do you approach responsibility? (1–4): "
]
answers = []

for q in questions:
    value = get_valid_input(q)
    answers.append(value)



score = sum(answers)# this is very clean 

print("Total score:", score)

if score <= 4:
    print("Beginner")
elif score <= 6:
    print("Intermediate")
else:
    print("Advanced")
