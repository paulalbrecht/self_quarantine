import random

number = random.randint(10, 30)
name = input("Enter your name: ")
guess = int(input("Enter your guess: "))

while True:
    if guess > number:
        print(f"{guess} is too high")
    elif guess < number:
        print(f"{guess} is too low")
    else:
        print(f"{guess} is correct")
        break
