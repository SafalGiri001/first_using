# import random

# print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

# low = int(input("Enter the Lower Bound: "))
# high = int(input("Enter the Upper Bound: "))

# print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

# num = random.randint(low, high) 
# ch = 7                        # Total allowed chances
# gc = 0                        # Guess counter

# while gc < ch:
#     gc += 1
#     guess = int(input('Enter your guess: '))

#     if guess == num:
#         print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
#         break

#     elif gc >= ch and guess != num:
#         print(f'Sorry! The number was {num}. Better luck next time.')

#     elif guess > num:
#         print('Too high! Try a lower number.')

#     elif guess < num:
#         print('Too low! Try a higher number.')

import random

print("Hi welcome to the number guessing game developed by sandesh giri. You have 7 chances to guess it. \n Lets Start")

low = int(input("Enter the lowest number:"))
high = int(input("Enter the highest number:"))

print(f"You have 7 chances to guess the number between {low} and {high}. Let's Start")

num = random.randint(low, high)
chances = 7
guess = 0

while guess <7:
    guess += 1
    guesses = int(input("Enter your guess:"))

    if guesses == num:
        print(f"Correct! The number is {num}. You guessed it in {guess} attempts.")
        break

    elif guess >= chances and guesses != num:
            print(f"Sorry! The number was {num}. Better luck next time.")

    elif guesses>num:
         print("Too high! Try a lower number.")

    elif guesses<num:
         print("Too low! Try a higher number.")
         

