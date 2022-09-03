import os


def clear_console() -> None:
    """
    Clears the console screen.
    """
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"

    os.system(command)


def get_user_input(message: str, choices: list[str] | list[int]) -> str | int:
    """
    Retrieves user input matching a list of choices.
    """
    response = None
    while True:
        response = input(message).lower()
        if response not in choices:
            print(f"A valid input would be {choices}")
            continue

        break

    return response


def get_user_integer(message: str, min: int, max: int) -> int:
    """
    Retrieves an integer from the user, ensuring it's within a range.
    """
    response = None
    while True:
        try:
            response = int(input(message))
        except ValueError:
            print("Invalid Input. Try again!")
            continue
        except:
            exit(1)

        if response >= min and response <= max:
            break

        print(f"Your number is not in range. Must be between {min} and {max}.")

    return response
