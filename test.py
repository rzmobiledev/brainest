from random import randint

WORDS = ["tree", "car", "lordoftherings", "godzilla", "disestablishmentarianism", "kapow", "java", "foobar"]

def get_indices(letter: str, word: str):
    indices = []
    for i in range(len(word)):
        if word[i] == letter:
            indices.append(i)
    return indices


word = WORDS[randint(0, len(WORDS))]

guess = ["_"] * len(word)

tries_left = 6
used_letters = set()
    
while tries_left > 0:
    print("You have", tries_left, "tries left.")
    print("Used letters:", " ".join(used_letters))
    print("Word:", " ".join(guess))
    print()
    
    user_letter = input("Guess a letter: ")
    used_letters.add(user_letter)
    guessed = get_indices(user_letter, word)
    if not guessed:
        tries_left -= 1
        continue
        
    for i in guessed:
        guess[i] = user_letter
    
    if "".join(guess) == word:
        print("You guessed the word " + word + "!")
        break
        
if "".join(guess) != word:
    print("You didn't guess the word :/")
    print("It was:", word)