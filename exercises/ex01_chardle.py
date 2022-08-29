"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730389484"

word: str = (input("Enter a 5-character word: "))

if len(word) != 5:
    print( "Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print( "Error: Character must be a single character.")
    exit()
else:
    print("Searching for " + character + " in " + word)

character_count = 0

if character == word[0]:
    print (character + " found at index 0 ")
    character_count = character_count + 1
     

if character == word[1]:
    print (character + " found at index 1 ")
    character_count = character_count + 1
    

if character == word[2]:
    print (character + " found at index 2 ")
    character_count = character_count + 1
   

if character == word[3]:
    print (character + " found at index 3 ")
    character_count = character_count + 1
    

if character == word[4]:
    print (character + " found at index 4 ") 
    character_count = character_count + 1

if character_count > 1:
    print (str(character_count) + " instances of " + character + " found in " + word)

if character_count == 1: 
    print (str(character_count) + " instance of " + character + " found in " + word)

if character_count < 1:
    print ("No instances of " + character + " found in " + word)
