import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return f"Did you mean {get_close_matches(word, data.keys())[0]} instead"

    else:
        return f"The word {word} does not exist. Please double check it"


word = input("Enter a word: ")

print(translate(word))
