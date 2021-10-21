import random
from words import words
from hangman_visual import hangman_visual
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    lives = 7
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0 and lives > 0 :
        print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        print(hangman_visual[lives])
        print(f"You have {lives} lives left")
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Yay!")
            else:
                lives-=1
    
                print("Wrong!")

        elif user_letter in used_letters:
            print("You have already used that character m8!")

        else:
            print("Invalid character")
    if lives > 0:
        print("You won")
        print(f"Final word : {word}")
    else: 
        print(f"You lost m8, the word was: {word}")

    
hangman()

