import random

choices = ['rock', 'paper', 'scissors']

def win(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    return "Computer wins!"

while True:
    print("Welcome to the Rock-Paper-Scissors game!")
    print("Choose one of the following options:\n Rock, Paper Or Scissor \n")
    user_choice = input("your choice: ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer choice:  {computer_choice}")
    result = win(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again  in ['yes', 'y']:
        continue
    else:
        print("Thanks for playing! Goodbye!")
        break
