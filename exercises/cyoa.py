"""EX06 -- Choose Your Own Adventure"""

__author__ = "730389484ß"

player: str = ""
points: int = 0
LEVEL_ONE: str = "go"
LEVEL_TWO: str = "yes"
END_GAME: str = "stop"
CHECK_EMOJI: str = "\U00002705"
X_EMOJI: str = "\U0000274C"
FACE_EMOJI: str = "\U0001F974"


def greet() -> None:
    """Inroduction to game, greet user."""
    global player
    print("Welcome to the game! Here, you will play take lucky guesses at guessing a number! Earn points by playing, and even more for guessing correctly! ")
    player = input("What is your name? ")
    

def main() -> None:
    """The entrypoint of the program."""
    global points
    greet()
    points = 3
    print("Congrats! You earned 3 adventure points!")
    while points > 0:
        where_to_next: str = input(f"Hi {player}! You have a total of {points} adventure points! \n What would you like to do next? \n Enter the word 'go' to play and guess a number 1-5. \n Enter the word 'yes' to play and guess a number between one and your current amount of adventure points! \n Enter the word 'stop' to end the game: \n ")
        if where_to_next == END_GAME:
            print(f"Thanks for playing, {player}! While playing, you earned a total of {points} points! ")
            quit()
        elif where_to_next == LEVEL_ONE:
            one_to_5()
        elif where_to_next == LEVEL_TWO:
            one_to_points(points)


def one_to_5() -> None:
    """Prompts user to continue providing guess of number until guess is correct and returns points."""
    global points
    i: int = 0
    from random import randint
    rand_number: int = randint(1, 5)
    user_guess: int = input(f"Welcome {player}! Please enter a number 1-5: ")
    while int(user_guess) != rand_number:
        if int(user_guess) > 5 or int(user_guess) < 1:
            user_guess = input("That isn't a number from 1-5! Try again: ")
        if int(user_guess) >= 1 and int(user_guess) <= 5:
            print("Sorry, not quite!")
            points += 1
            user_guess = input(f"You now have {points} total adventure points. Guess again!! ")
    if int(user_guess) == rand_number:
        points += 5
        print(f"Congrats {player}! You guessed the right number!")
        print(f"You now have {points} total adventure points! Great job!")
        

def one_to_points(points_current: int) -> int:
    """Prompts user to continue providing a guess of number 1-current points until guesss is correct and returns new points."""
    global points 
    from random import randint 
    number: int = randint(1, points_current)
    guess: str = input(f"Welcome {player}! Your current number of adventure points is {points_current}! Guess a number 1-{points_current}: ")
    while int(guess) != number:
        if int(guess) > points_current or int(guess) < 1:
            guess = input(f"{FACE_EMOJI} That isn't a number from 1-{points_current}! Try again: ")
        if int(guess) >= 1 and int(guess) <= points_current:
            print(f"{X_EMOJI} Sorry, not quite!")
            points += 1
            guess = input(f"You now have {points} total adventure points. Guess again!! ")
    if int(guess) == number:
        points += 5
        print(f"{CHECK_EMOJI} Congrats {player}! You guessed the right number!")
        print(f"You now have {points} total adventure points! Great job!")
    return points 
        
    
    




if __name__ == "__main__":
    main()