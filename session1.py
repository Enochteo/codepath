# Problem 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

# Problem 2
def greeting(name):
    print("Welcome to The Hundred Acre Wood "+ name+"! My name is Christopher Robin.")

greeting("Samuel")

# Problem 3
def print_catchphrase(character):

    catchphrases = {

        "Pooh": "Oh bother!",

        "Tigger": "TTFN: Ta-ta for now!",

        "Eeyore": "Thanks for noticing me.",

        "Christopher Robin": "Silly old bear."

    }

    if character in catchphrases:

        print(catchphrases[character])

    else:

        print(f"Sorry! I don't know {character}'s catchphrase!")


character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

#Problem 4
def get_item(items, x):
    if x < len(items):
        return items[x]
    else:
        return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))

# Problem 5
def sum_honey(hunny_jars):
    sum = 0
    for i in range(0,len(hunny_jars)):
        sum += hunny_jars[i]
    return sum
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))