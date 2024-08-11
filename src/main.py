import sys
from datetime import datetime


def greet(name: str) -> str:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    greeting = f"Hello, {name}! Welcome to our program. Current time is {current_time}."
    return greeting


def main() -> None:
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = input("Enter your name: ")

    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
