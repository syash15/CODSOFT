import random

# Game options
options = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

print("🪨 📄 ✂️  Welcome to Rock-Paper-Scissors! ✂️ 📄 🪨")

while True:
    print("\nChoose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in options:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win! 🎉"
        user_score += 1
    else:
        result = "Computer wins! 🤖"
        computer_score += 1

    # Show result
    print(f"\n👉 {result}")
    print(f"Score — You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        break

print("\nThanks for playing! 👋")
input("\nPress Enter to exit...")
