import random
import time

OPERATORS = ["+", "-", "*"]
MIN_VAL = 3
MAX_VAL = 13
TOTAL_PROBLEMS = 10

def generate():
    left = random.randint(MIN_VAL, MAX_VAL)
    right = random.randint(MIN_VAL, MAX_VAL)        
    op = random.choice(OPERATORS)

    expr = str(left) + " " + op + " " + str(right)
    ans = eval(expr)
    return expr, ans
    
wrong = 0
input("Press Any Key to Start the Math Challenge!")
print("------------------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, ans = generate()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(ans):
            print("Right Answer!")
            break
        else:
            wrong += 1
            print("Wrong Answer!")

end_time = time.time()
time_taken = round(end_time - start_time, 2)

print("------------------------------------------")
print(f"Congrats! You are Done. You took {wrong} wrong guesses and finished the challenge in {time_taken} seconds!")
