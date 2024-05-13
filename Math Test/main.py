import random
import time

operations = ["+", "-", "*"]
min_digit = 5
max_digit = 15
max_questions = 10
wrong_answers = 0
time_taken = 0

input("Press enter too start")

start_time = time.time()
while max_questions != 0:
    current_operation = random.choice(operations)
    current_num1 = random.randint(min_digit, max_digit)
    current_num2 = random.randint(min_digit, max_digit)
    expr = f"{current_num1} {current_operation} {current_num2}"
    ans = input(f"What is {expr}: ")
    correct_ans = eval(expr)
    max_questions -= 1
    if ans != correct_ans:
        wrong_answers += 1
end_time = time.time()
time_taken = end_time - start_time

print(f"The number of wrong answers are: {wrong_answers}")
print("The time taken is %d sec." % time_taken)
