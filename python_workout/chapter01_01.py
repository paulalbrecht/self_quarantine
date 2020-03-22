# Take a number input as a guess to the predefined number and print three options, correct, higher, lower

from random import randrange

number = randrange(0, 101)

while True:
    guess = int(input("Please enter a number 1-100: "))

    if number < guess:
        print("Your guess was too high")
    elif guess < number:
        print("Your guess was too low")
    else:
        print("Your guess was correct")
        break
    