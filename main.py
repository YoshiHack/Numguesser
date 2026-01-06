import random
print("Hello, welcome to my number guessing game!")
print("1 Easy (1-10)")
print("2 Medium (1-50)")
print("3 Hard (1-100)")
difficulty = input("Choose a difficulty level (1, 2, or 3): ")
if difficulty == '1':
    number_to_guess = random.randint(1, 10)
    print("You have chosen Easy mode.")
    guess = input("what is your guess?:")
    if guess == number_to_guess: 
        print("You win!")
    else:
        print("You lose")
elif difficulty == '2':
    number_to_guess = random.randint(1, 50)
    print("You have chosen Medium mode.")
    guess = input("what is your guess?:")
    if guess == number_to_guess: 
        print("You win!")
    else:
        print("You lose")
elif difficulty == '3':
    number_to_guess = random.randint(1, 100)
    print("You have chosen Hard mode.")
    guess = input("what is your guess?:")
    if guess == number_to_guess: 
        print("You win!")
    else:
        print("You lose")
else:
    print("Invalid difficulty level selected.")