import random
import artwork
from utils import clear_console, get_user_input, get_user_integer

GUESSES_BY_DIFFICULTY = {"easy": 10, "hard": 5}
MIN_NUMBER = 1
MAX_NUMBER = 100


def main():
    clear_console()
    print(artwork.logo)

    difficulty = get_user_input(
        'Select "easy" or "hard" difficulty: ',
        ["easy", "hard"],
    )
    user_guesses = GUESSES_BY_DIFFICULTY[difficulty]

    target_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")

    game_running = True
    while game_running:
        print("-" * 40)
        print(f"You have {user_guesses} remaining to guess the number")
        user_guess = get_user_integer(f"What is your guess: ", MIN_NUMBER, MAX_NUMBER)

        user_guesses -= 1
        if user_guess != target_number:
            if user_guesses == 0:
                print("You ran out of guesses. You lose!")
                game_running = False
            elif user_guess < target_number:
                print("You guess is too low.")
            else:
                print("Your guess is too high.")

        else:
            print("You win!")
            game_running = False

    if get_user_input("Play Again? [y|n] ", ["y", "n"]) == "y":
        main()


if __name__ == "__main__":
    main()
