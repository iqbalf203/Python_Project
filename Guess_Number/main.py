import random

def guess(num1, num2, try_i):
    random_number = random.randint(num1, num2,)
    while try_i>0:
        guess = int(input(f"Guess a Number between {num1} and {num2}: "))
        try_i-=1
        if guess > random_number:
            print("Sorry, Guess is too high.")
        elif guess < random_number:
            print("Sorry, Guess is too low.")
        else:
            print(f"Congratulations, You have guessed the number {guess} correct.")
            break
    else:
        print("Maximum Try Reached.")

num1 = int(input("Enter the number you want to guess from: "))
num2 = int(input("Enter the number you want to guess till: "))
try_i  = int(input("Enter the maximum number of try: "))
guess(num1, num2, try_i)