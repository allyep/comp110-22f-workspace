"""EX02 - One-Shot Wordle"""

__author__ = "730389484"

secret_word = str("python")
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_check: int = 0
box_result: str = ""
character_exists: bool = False
alt_index: int = 0 
while len(word_guess) != len(secret_word):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
   
while index_check < len(secret_word):
    if word_guess[index_check] == secret_word[index_check]:
        box_result = box_result + GREEN_BOX
    else:
        while character_exists != True and alt_index < len(secret_word):
            if word_guess[index_check] == secret_word[alt_index]:
                character_exists = True  
            else:
                alt_index += 1
        if character_exists == True:
            box_result = box_result + YELLOW_BOX
        else: 
            box_result = box_result + WHITE_BOX 
    index_check += 1 
print(box_result)
while len(word_guess) == len(secret_word):
    if word_guess == secret_word:
        word_guess = input("Woo! You got it! ")
    else: 
        word_guess = input("Not quite. Play again soon! ")


