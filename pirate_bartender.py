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

adjectives = {
    "strong": ["Able-bodied", "Athletic", "Hardened"],
    "salty": ["Briny", "Saline", "Raspy"],
    "bitter": ["Acrid", "Harsh", "Astringent"],
    "sweet": ["Syrupy", "Saccharine", "Cloying"],
    "fruity": ["Mellow", "Pleasant", "Fruitalicious"]
}

nouns = {
    "strong": ["Anvil", "Hammer", "Gunshot"],
    "salty": ["Salt Box", "Salt Lick", "Saltine"],
    "bitter": ["Pisser", "Old Man", "Old Cuss"],
    "sweet": ["Sweetheart", "Pollyanna", "Dollface"],
    "fruity": ["Cobbler", "Orchard", "Fruitcake"]
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

def splainDrink(components):
    print "Ye take the following ingredients:"
    for c in components:
        print c
    print "And ye mix them thoroughly, and serve over ice.  Yarr, thar ye be."
    return True

def nameDrink(prefs):
    adj = random.choice(adjectives[random.choice(prefs)])
    noun = random.choice(nouns[random.choice(prefs)])
    name = "The " + adj + " " + noun
    return name

def makeDrink():
    prefs = getInput()
    components = constructDrink(prefs)
    splainDrink(components)
    print "I call it " + nameDrink(prefs)


if __name__ == '__main__':
    print "Oh hello there.  Let me get ye a drink.  It's all I can offer ye, besides the scurvy."
    makeDrink()
    will_have_another = raw_input("Would ye like another? Type y or yes if so.  ")
    while will_have_another == "y" or will_have_another == "yes":
        makeDrink()
        will_have_another = raw_input("Would ye like another?  Type y or yes if so.  ")
