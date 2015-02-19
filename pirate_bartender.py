import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def getInput():
    prefs = []
    for q in questions:
        a = raw_input(questions[q])
        if str.lower(a) == "y" or str.lower(a) == "yes":
            prefs.append(q)
    return prefs

def constructDrink(prefs):
    components = []
    for p in prefs:
        choice = random.choice(ingredients[p])
        components.append(choice)
    return components

if __name__ == '__main__':
    foo = getInput()
    print constructDrink(foo)
   