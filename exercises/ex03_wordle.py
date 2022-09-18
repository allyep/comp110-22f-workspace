"""EX03 --- Example of a wordle with limited attempts."""

__author__ = "730389484"


def contains_char(param_search: str, char_search: str) -> bool:
    """Returns truth value of single character of second string existing at any index of first string."""
    assert len(char_search) == 1
    index_check: int = 0
    alt_index: int = 0 
    while char_search in param_search:
        if param_search[index_check] == char_search[alt_index]:
            return True    
        else: 
            index_check += 1
    return False   


def emojified(guess: str, secret: str) -> str:
    """Returns a colored emoji string using previous function to test code for yellow or white boxes."""
    box_result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    ind_check: int = 0 
    while ind_check < len(secret):
        if guess[ind_check] == secret[ind_check]:
            box_result = box_result + GREEN_BOX
        elif contains_char(secret, guess[ind_check]):
            box_result = box_result + YELLOW_BOX
        else:
            box_result = box_result + WHITE_BOX
        ind_check += 1
    return box_result


def input_guess(expected_length: int) -> str:
    """Prompts user to continue providing a word guess until they provide one with correct length."""
    word_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(word_guess) != expected_length:
        word_guess = input(f"That wasn't {expected_length} characters! Try again: ")
    if len(word_guess) == expected_length:
        return word_guess
    return word_guess 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 0
    win: bool = False 
    while turns < 6 and win is False:
        turns += 1
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret_word))  
        print(emojified(guess, secret_word))  
        if guess == secret_word:
            win = True 
    if win is True:   
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()