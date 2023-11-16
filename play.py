import random

def choose_word():
    words = ["snake", "cherry", "elephant", "banana", "computer", "python", "giraffe", "orange", "jungle", "zebra"]
    return random.choice(words)

def display_clues(word):
    print("Clues:")
    print(f"- The word has {len(word)} letters.")
    print(f"- The first letter is '{word[0]}'.")
    print(f"- The word rhymes with '{word[-2:]}'.")  # You can add more clues here.

def play_game():
    word_to_guess = choose_word()
    attempts_left = 3

    print("Welcome to Mystery Word!\n")

    while attempts_left > 0:
        display_clues(word_to_guess)
        print(f"\nAttempts left: {attempts_left}")
        guess = input("Guess the word: ").lower()

        if guess == word_to_guess:
            print(f"Congratulations! You guessed the word '{word_to_guess}'! Well done!\n")
            break
        else:
            attempts_left -= 1
            print("Incorrect! Try again.\n")

    if attempts_left == 0:
        print(f"Sorry, you're out of attempts. The correct word was '{word_to_guess}'.\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes"

def main():
    while True:
        if not play_game():
            print("Thanks for playing Mystery Word! Goodbye.")
            break

if __name__ == "__main__":
    main()
