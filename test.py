# from random import randint

# WORDS = ["tree", "car", "lordoftherings", "godzilla", "disestablishmentarianism", "kapow", "java", "foobar"]

# def get_indices(letter: str, word: str):
#     indices = []
#     for i in range(len(word)):
#         if word[i] == letter:
#             indices.append(i)
#     return indices


# word = WORDS[randint(0, len(WORDS))]

# guess = ["_"] * len(word)

# tries_left = 6
# used_letters = set()
    
# while tries_left > 0:
#     print("You have", tries_left, "tries left.")
#     print("Used letters:", " ".join(used_letters))
#     print("Word:", " ".join(guess))
#     print()
    
#     user_letter = input("Guess a letter: ")
#     used_letters.add(user_letter)
#     guessed = get_indices(user_letter, word)
#     if not guessed:
#         tries_left -= 1
#         continue
        
#     for i in guessed:
#         guess[i] = user_letter
    
#     if "".join(guess) == word:
#         print("You guessed the word " + word + "!")
#         break
        
# if "".join(guess) != word:
#     print("You didn't guess the word :/")
#     print("It was:", word)

import json
from json import JSONEncoder

data = dict(name="Rizal Safril", age=39, wife="Iva Izazaya", marry=True, kids=["Nasywah Azkia", "Keyra Almira"])
new_data = json.dumps(data)


class Profile:

    def __init__(self, name: str, age: int, wife: str, kids: list[str], marry: bool):
        self.name = name
        self.age = age
        self.wife = wife
        self.kids = kids
        self.marry = marry


class Occupation:

    def __init__(self, name: str, age: int, position: str, condition: bool):
        self.name = name
        self.age = age
        self.position = position
        self.condition = condition


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, Profile):
            return {
                "name": o.name,
                "age": o.age,
                "wife": o.wife,
                "kids": o.kids,
                "marry": o.marry,
                o.__class__.__name__: True
            }
        
        elif isinstance(o, Occupation):
            return {
                "name": o.name,
                "age": o.age,
                "position": o.position,
                "condition": o.condition,
            }

        return JSONEncoder.default(self, o)


profile = Profile(name="Rizal Safril", age=39, wife="Iva Izazaya", kids=["Nasywah Azkia", "Keyra Almira"], marry=True)
occupation = Occupation(name="Rizal Safril", age=39, position="Backend Engineer", condition=True)

cv = json.dumps(profile, cls=UserEncoder, indent=2) # convert to json
cd = json.dumps(occupation, cls=UserEncoder)
print(cv)
print(json.loads(cd))


# with open("file.json", "r") as file:
#     data = json.load(file)
#     print(json.dumps(data, indent=4))