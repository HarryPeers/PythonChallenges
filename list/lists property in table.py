from os import system

system("")

top = ["List", "Array", "Tuple"]
side = ["Is it mutable?", "Can we change the size after creation?", "Can items in the list be changed?", "How many different types of data can be stored?"]


#0 = list, 1 = array, 2 = tuple

answers = [["Yes", "Yes", "No"],["Yes", "No", "No"],["Yes", "Yes", "No"],["3", "1", "1"]]

largest_answer = 0

for answer in answers:
    if len(answer) > largest_answer:
        largest_answer = len(answer)

largest_answer += 1

left_margin = 0

for question in side:
    if len(question) > left_margin:
        left_margin = len(question)

left_margin += 1

index = 0
for header in top:
    top[index] = header + " "*(largest_answer-len(header))
    index += 1

index = 0
for row in answers:
    sub_index = 0
    for ans in answers[index]:
        end = "|"
        adt = 0
        if sub_index == len(answers[index])-1:
            end = ""
        if sub_index > 0:
            adt = sub_index
        answers[index][sub_index] = ans + " "*(largest_answer+1+adt-len(ans)) + end
        sub_index += 1
    index += 1
    

print("\033[33;1;4m"+f" "*left_margin+"| "+" | ".join(top))

index = 0
for question in side:
    print(question+" "*(left_margin-len(question))+"| "+" ".join(answers[index]))
    index += 1

input()
