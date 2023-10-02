import random


num_1 = random.randint(1,10)
num_2 = random.randint(1,10)
operator_num = random.randint(4,4)
correct_remainder = 0
#correct_ans
amt_wrong = 0
#streak



if operator_num == 1:
    operator = "+"
    correct_ans = num_1 + num_2
elif operator_num == 2:
    operator = "-"
    correct_ans = num_1 - num_2
elif operator_num == 3:
    operator = "*"
    correct_ans = num_1 * num_2
elif operator_num == 4:
    operator = "/"
    correct_ans = num_1 // num_2
    correct_remainder = num_1 % num_2
    
print("CALCULATOR\n\n")
print("Correct Answer:", correct_ans)
print("Correct Remainder:", correct_remainder)

print()
print(num_1,operator,num_2)
user_ans = float(input("Answer: "))

while user_ans != correct_ans:
    amt_wrong = amt_wrong + 1
    print("Whoops, try again.")
    user_ans = float(input("Answer: "))
if user_ans == correct_ans:
        
    if amt_wrong == 0:
        print("NICE! FIRST TRY!")

    else:
       print("Correct! Took", amt_wrong + 1, "attempts")


amt_wrong = 0

while user_remainder_ans != correct_remainder & operator_num == 4:
    amt_wrong = amt_wrong + 1
    print("Whoops, try again.")
    if operator_num == 4: ###  IF DIVISION
        user_remainder_ans = float(input("Remainder: "))
        if user_remainder_ans == correct_remainder:
                print("Correct!")
