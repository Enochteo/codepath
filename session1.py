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