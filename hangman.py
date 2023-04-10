import random
'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

count = 0
count_balance = 6

all_letters = ("java", "python", "flutter", "dart", "javascript", "html", "css")
letter = tuple(random.choice(all_letters),)
word = ["_"] * len(letter)


def word_clue() -> str:
    wd = ["_ "] * len(letter)
    wd[0] = letter[0]
    wd[-1] = letter[-1]
    return wd


def append_word(guess: str) -> None:
    for i in range(len(letter)):
        if letter[i] == guess:
            # add used letters to list
            word[i] = guess


def all_words(w: str) -> str:
    return "".join(w)


while count_balance > 1:
    print("Word clue: {}".format(word_clue()))
    print("You have {} tries left".format(count_balance))
    print("Used letters: {}".format("_".join(word)))
    print("Word: {}".format("_ ".join(word)))
    guess = input("Guess a letter: ")

    if len(guess) > 1:
        print("Only one char is allowed!")
        continue

    elif guess not in letter:
        # We start to minus 1 each count balance
        count_balance -= 1

    # Start to append every correct word
    # to a list
    append_word(guess)

    if all_words(word) == "".join(letter):
        print("You guessed the word {} !".format("".join(word)))
        break

if all_words(word) != "".join(letter):
    print("Wrong Guess!")
    print("The correct word is: {}".format("".join(letter)))

print("You have exited the game")
