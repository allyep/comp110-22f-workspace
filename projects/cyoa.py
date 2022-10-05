"""EX06 -- Choose Your Own Adventure"""


player: str = ""

def greet() -> None:
    global player
    print("Welcome to the game! ")
    player = input("What is your name? ")
    


def main() -> None:
    """The entrypoint of the program."""
    points: int = 0
    greet()
    where_to_next: int = input(f"Hi {player}! Where would you like to go next? Enter 1 to (), 2 to (), or 3 to end the game: ")
    if where_to_next == 3:
        print(f"Thanks for playing {player}! /n You got a total of {points} adventure points! Come back soon!")


if __name__ == "__main__":
    main()