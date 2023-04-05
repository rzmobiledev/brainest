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

word = ["_", "_", "_", "_"]
guessed_word = ["_", "_", "_", "_"]

letters = ["j", "a", "v", "a"]
used_letters = list()

while count < 6:
    try:
        print("You have {} tries left".format(count_balance))
        print("Used letters: {}".format(" ".join(used_letters)))
        print("Word: {}".format("_ ".join(word)))
        guess = str(input("Guess a letter: "))
        
        # start to count every loop
        count += 1

        # We start to minus 1 each count balance
        count_balance = count_balance - 1

        # Check index of letters
        for i in range(len(letters)):
            if letters[i] == guess:
                # add used letters to list
                used_letters.append(guess)

                guessed_word[i] = letters[i]
                word[i] = letters[i]

        if guessed_word == letters:
            print("You guessed the word {} !".format("".join(guessed_word)))
            break
        
        # if above condition does not meet,
        # we need to continue the program
        continue
    
    except Exception as e:
        print(str(e))

# check if guessed word is false
if guessed_word != letters:
    print("Wrong Guess!")
    
print("You have exited the game")