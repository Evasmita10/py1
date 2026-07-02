import random

print("🎯 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!\n")

play_again = "yes"

while play_again == "yes":

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too Low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too High! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Please enter a valid number.\n")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("\n👋 Thanks for playing! Goodbye!")