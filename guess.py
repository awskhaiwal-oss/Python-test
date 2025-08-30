import random

system_generated_number = random.randrange(1, 10)
print("system_generated_number:", system_generated_number)
print("You have to guess the right number in 5 attempts and you can choose number in between 1 to 10 range.")
user_input = int(input("Enter the guess number: "))
number_of_attempts = 5
count = 1
while count <= number_of_attempts:
    if user_input < system_generated_number:
        print("Your number is less than the correct number.")
    elif user_input > system_generated_number:
        print("Your number is greater than the correct number.")
    elif user_input == system_generated_number:
        print("You won!!!")
        break
    user_input = int(input("Please guess again: "))
    if count == number_of_attempts:
        print("You exceed the limit. You failed!!!")
        break
    count += 1
