answer = 0
question2 = 0
question3 = 0 
score = 0

while answer < 1 or answer > 4:# allows me to set a conditon where I can ensure member enters vaild number
    answer = int(input("Enter a number between 1 and 4: "))
    
while question2 < 1 or question2 > 4:
    question2 = int(input("Any degree ? Enter a number between 1 and 4: "))

while question3 < 1 or question3 > 4:
    question3 = int(input("How do you approach responsibility? Please enter a number between 1–4: "))
#print(answer, question2, question3)


answers = [answer, question2, question3]

for value in answers:
    
    score += value
    print("Total score:", score)

if score <= 4:
    print("Beginner")
elif score <= 6:
    print("Intermediate")
else:
    print("Advanced")
