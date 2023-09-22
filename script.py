import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_or_no = input(
            f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no. ").lower()
        if yes_or_no == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_or_no == 'n':
            return f"The word {word} does not exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return f"The word {word} does not exist. Please double check it."


word = input("Enter a word: ").lower()

output = translate(word)

index = 1
if type(output) == list:
    for definition in output:
        print(f"{index}. {definition}")
        index += 1
else:
    print(output)
