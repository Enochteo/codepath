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

#question 6: 
def doubled(hunny_jars):

    doubled_list = []

    for jar in hunny_jars:

        doubled_list.append(jar * 2)

    return doubled_list

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

# Question 7
def count_less_than(race_times, threshold):
    counts = 0
    for count in race_times:
        if count < threshold:
            counts += 1
    return counts

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

#Problem 8
def print_todo_list(tasks):
    print("Pooh's To Dos:\n")
    for i in range(0,len(tasks)):
        print(f"{i+1}. {tasks[i]}\n")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

#question9: 
def can_pair(item_quantities):

    for qty in item_quantities:

        if qty % 2 != 0:

            return False

    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

#Problem 10
def split_haycorns(quantity):
    splits = []
    for i in range(1, quantity+1):
        if quantity % i == 0:
            splits.append(i)
    return splits

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))

#Problem 11
def tiggerfy(s):
    result = ""
    list = ['t','i','g','e','r']
    for letter in s:
        if letter.lower() not in list:
            result += letter
    return result
s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

# Problem 12
def locate_thistles(items):

    indices = []

    for i in range(len(items)):

        if items[i] == "thistle":

            indices.append(i)

    return indices

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))

## Advanced
 # Problem 1
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))

def final_value_after_operations(operations):
    tigger = 1
    operands = {"bouncy": 1, "trouncy":-1, "flouncy": 1, "pouncy": -1}
    for item in operations:
        tigger += operands[item]
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
#Looks good thanks. Hopping off the liveshare now
# Cool catch you next time