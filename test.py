stored_letters = list("java")  # converts string to list
guessed_word = len(stored_letters) * ["_"]
used_letters = list()


count_balance = 6

while count_balance <= 6:
    try:
        print("\nYou have {} tries left.".format(count_balance))
        print("Used letters: {}".format(" ".join(used_letters)))
        print("word: {}".format(" ".join(guessed_word)))
        guess = input("Guess a letter: ")

        # if input is multiple character, it returns warrning message with no change in count_balance
        if len(guess) > 1:
            print("Only one char is allowed")
            continue

        # decrements the no.of tries if the guess is wrong
        if guess not in stored_letters:
            count_balance -= 1
            if count_balance < 1:
                break
            used_letters.append(guess)

        # checks each letter in stored letters with the guessed letter
        else:
            used_letters.append(guess)

            for i in range(len(stored_letters)):

                # accepts both lowercase and uppercase inputs
                if (
                    stored_letters[i] == guess
                    or stored_letters[i] == guess.upper()
                    or stored_letters[i] == guess.lower()
                ):
                    
                    guessed_word[i] = stored_letters[i]

        if guessed_word == stored_letters:
            print("You guessed the word {} !".format("".join(guessed_word)))
            break

    except Exception as e:
        print(str(e))


# return the messeage if the guess is incorrect
if guessed_word != stored_letters:
    print("Wrong Guess")

print("You have exited the game")