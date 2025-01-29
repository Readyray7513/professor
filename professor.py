import random
import sys

def get_level():
    while True:
        try:
            level = int(input("Level (1-3): "))  # User inputs the level
            if 1 <= level <= 3:  # Accept only levels between 1 and 3
                return level
            else:
                print("Invalid level. Please enter a number between 1 and 3.")
        except ValueError:  # Handle invalid inputs (e.g., letters or symbols)
            print("Invalid input. Please enter a number between 1 and 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3.")


def play_game(level):
    s = 0
    for _ in range(10):  # Ask 10 questions
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0
        while attempts < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == x + y:
                    s += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        if attempts == 3:
            print(f"The correct answer is: {x + y}")
    print(f"{s}")  # Print the final score in the expected format
    sys.exit(0)  # Exit the program cleanly


def main():
    level = get_level()  # Get the level from the user
    play_game(level)  # Play the game at the selected level


if __name__ == "__main__":
    main()