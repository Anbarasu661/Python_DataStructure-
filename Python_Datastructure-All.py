"""
=====================================================================
  PYTHON DATA STRUCTURES FOR BEGINNERS  -  "The Magic Village of Pyville"
=====================================================================

THE STORY
---------
Once upon a time there was a small village called Pyville.
A young boy named Ravi lived there and he loved to organise things.

  * He kept his friends in a TRAIN with numbered seats      -> LIST
  * He locked his treasure in a SEALED CHEST                -> TUPLE
  * He kept a PHONE BOOK (name -> number)                   -> DICTIONARY
  * He collected UNIQUE stickers in a bag (no duplicates)   -> SET
  * His plates were piled one on top of another             -> STACK
  * Customers waited in line at his shop                    -> QUEUE
  * His name and his letters, written on a ribbon           -> STRING

Each part of the story = one Python data structure.

HOW TO RUN (use these commands in your terminal / command prompt)
-----------------------------------------------------------------
  python python_data_structures_story.py            -> run EVERYTHING
  python python_data_structures_story.py list       -> only the LIST part
  python python_data_structures_story.py tuple      -> only the TUPLE part
  python python_data_structures_story.py dict       -> only the DICTIONARY part
  python python_data_structures_story.py set        -> only the SET part
  python python_data_structures_story.py string     -> only the STRING part
  python python_data_structures_story.py stack      -> only the STACK part
  python python_data_structures_story.py queue      -> only the QUEUE part
  python python_data_structures_story.py nested     -> nested structures
  python python_data_structures_story.py summary    -> the cheat sheet
  python python_data_structures_story.py --help     -> show help

Tip for your video: run one topic at a time, explain the output,
then move on to the next topic.
"""

import argparse                      # lets us read commands typed in the terminal
from collections import deque        # deque = a fast queue (built into Python)


# ---------------------------------------------------------------------
# Small helper functions so the output looks neat on screen
# ---------------------------------------------------------------------
def title(text):
    """Print a big heading for each topic."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def say(text):
    """Print a story line."""
    print(f"\n[STORY] {text}")


def show(label, value):
    """Print a label and a value, like:  After append -> [1, 2, 3]"""
    print(f"   {label:<28} -> {value}")


# =====================================================================
# 1. LIST  -  "The Friends Train"
# =====================================================================
def learn_list():
    title("1. LIST  -  The Friends Train")
    say("Ravi has a train. Every friend sits on a numbered seat starting from 0.\n"
        "        Friends can get in, get out, or change seats. The train is flexible!")

    # A list is written with square brackets [ ]
    # It is ORDERED (keeps order) and MUTABLE (we can change it).
    friends = ["Arun", "Bala", "Charu"]
    show("Our train", friends)

    # --- Access items using INDEX (position). Index starts from 0! ---
    show("First friend  friends[0]", friends[0])
    show("Last friend   friends[-1]", friends[-1])   # -1 means from the end

    # --- Slicing: take a part of the list  [start : stop]  (stop not included) ---
    show("Slice friends[0:2]", friends[0:2])

    # --- Add items ---
    friends.append("Deepa")             # add at the END
    show("After append('Deepa')", friends)

    friends.insert(1, "Eswar")          # add at a POSITION (index 1)
    show("After insert(1,'Eswar')", friends)

    # --- Change an item ---
    friends[0] = "Arjun"                # lists are mutable, so this works
    show("After friends[0]='Arjun'", friends)

    # --- Remove items ---
    friends.remove("Bala")              # remove by VALUE
    show("After remove('Bala')", friends)

    last = friends.pop()                # remove & give back the LAST item
    show("pop() gave us", last)
    show("List after pop()", friends)

    # --- Useful tools ---
    numbers = [5, 2, 9, 1]
    show("len(numbers)", len(numbers))          # how many items
    numbers.sort()                              # sort small -> big
    show("After sort()", numbers)
    numbers.reverse()                           # reverse the order
    show("After reverse()", numbers)
    show("sum(numbers)", sum(numbers))
    show("'Charu' in friends ?", "Charu" in friends)   # membership check

    # --- Loop through a list ---
    print("\n   Looping through the train:")
    for seat, name in enumerate(friends):       # enumerate gives index + value
        print(f"      Seat {seat}: {name}")

    # --- List comprehension: build a list in ONE line (very Pythonic!) ---
    squares = [n * n for n in range(1, 6)]
    show("Squares of 1 to 5", squares)


# =====================================================================
# 2. TUPLE  -  "The Sealed Treasure Chest"
# =====================================================================
def learn_tuple():
    title("2. TUPLE  -  The Sealed Treasure Chest")
    say("Ravi puts his treasure in a chest and SEALS it.\n"
        "        Once sealed, nothing inside can be changed. That is a tuple!")

    # A tuple is written with round brackets ( )
    # It is ORDERED but IMMUTABLE (cannot be changed after creation).
    treasure = ("gold coin", "diamond", "ruby")
    show("Our chest", treasure)
    show("treasure[1]", treasure[1])            # indexing works like a list

    # Trying to change it gives an ERROR. We catch it so the program continues.
    try:
        treasure[0] = "silver coin"
    except TypeError as error:
        show("Trying to change it", f"ERROR: {error}")

    # A tuple with ONE item needs a comma!
    single = ("gold",)
    show("One-item tuple", single)

    # --- Unpacking: take values out into separate variables ---
    gold, gem, stone = treasure
    show("Unpacked", f"{gold} | {gem} | {stone}")

    # --- Why use a tuple? ---
    # 1) Safe data that should not change (e.g. a location)
    # 2) Slightly faster than a list
    # 3) Can be used as a dictionary KEY (lists cannot)
    location = (13.0827, 80.2707)               # latitude, longitude of Chennai
    show("Fixed location", location)


# =====================================================================
# 3. DICTIONARY  -  "The Phone Book"
# =====================================================================
def learn_dict():
    title("3. DICTIONARY  -  The Phone Book")
    say("Ravi keeps a phone book. He does not search by page number,\n"
        "        he searches by NAME and instantly gets the number. KEY -> VALUE!")

    # A dictionary uses curly brackets { } with key: value pairs.
    phone_book = {"Arun": "98400", "Bala": "98401", "Charu": "98402"}
    show("Phone book", phone_book)

    # --- Get a value using its KEY ---
    show("phone_book['Arun']", phone_book["Arun"])
    # .get() is SAFER: it does not crash if the key is missing
    show("get('Zara')", phone_book.get("Zara"))
    show("get('Zara','Not found')", phone_book.get("Zara", "Not found"))

    # --- Add or update ---
    phone_book["Deepa"] = "98403"               # new key -> adds
    phone_book["Arun"] = "99999"                # existing key -> updates
    show("After add + update", phone_book)

    # --- Delete ---
    del phone_book["Bala"]
    show("After del 'Bala'", phone_book)

    # --- keys(), values(), items() ---
    show("keys()", list(phone_book.keys()))
    show("values()", list(phone_book.values()))

    print("\n   Looping through the phone book:")
    for name, number in phone_book.items():     # items() gives key AND value
        print(f"      {name} -> {number}")

    show("'Charu' in phone_book ?", "Charu" in phone_book)   # checks KEYS

    # --- Dictionary comprehension ---
    cubes = {n: n ** 3 for n in range(1, 5)}
    show("Cubes dictionary", cubes)


# =====================================================================
# 4. SET  -  "The Unique Sticker Bag"
# =====================================================================
def learn_set():
    title("4. SET  -  The Unique Sticker Bag")
    say("Ravi collects stickers. If he gets the same sticker twice,\n"
        "        the bag keeps only ONE. No duplicates allowed!")

    # A set uses curly brackets { } with single values.
    # It is UNORDERED and has NO DUPLICATES.
    stickers = {"star", "heart", "moon", "star", "heart"}
    show("Stickers (duplicates gone)", stickers)

    # --- Add / remove ---
    stickers.add("sun")
    show("After add('sun')", stickers)
    stickers.discard("moon")                    # discard = no error if missing
    show("After discard('moon')", stickers)

    # --- Remove duplicates from a list - the most popular use! ---
    marks = [90, 85, 90, 70, 85]
    show("List with duplicates", marks)
    show("Unique values", list(set(marks)))

    # --- Math with sets ---
    mine = {"star", "heart", "sun"}
    friend = {"sun", "tree", "heart"}
    show("Both have (intersection)", mine & friend)
    show("All stickers (union)", mine | friend)
    show("Only mine (difference)", mine - friend)

    # Note: because sets are unordered, you cannot use set[0].


# =====================================================================
# 5. STRING  -  "The Ribbon of Letters"
# =====================================================================
def learn_string():
    title("5. STRING  -  The Ribbon of Letters")
    say("Ravi writes his name on a ribbon. Each letter has a position,\n"
        "        just like a list. But once written, the ribbon cannot be edited!")

    # A string is a sequence of characters. It is IMMUTABLE like a tuple.
    name = "Pyville"
    show("name", name)
    show("name[0]", name[0])
    show("name[-1]", name[-1])
    show("name[0:2]", name[0:2])
    show("len(name)", len(name))

    # --- Handy string methods (they return a NEW string) ---
    sentence = "  python is fun  "
    show("strip()", sentence.strip())           # remove spaces at the ends
    show("upper()", sentence.upper())
    show("title()", sentence.strip().title())
    show("replace('fun','easy')", sentence.replace("fun", "easy"))

    # split() turns a string into a LIST, join() turns a list into a string
    words = "apple,banana,cherry".split(",")
    show("split(',')", words)
    show("' - '.join(words)", " - ".join(words))

    # f-string: put variables inside text
    age = 10
    show("f-string", f"Ravi is {age} years old")


# =====================================================================
# 6. STACK  -  "The Plate Pile"   (Last In, First Out)
# =====================================================================
def learn_stack():
    title("6. STACK  -  The Plate Pile  (LIFO)")
    say("Ravi washes plates and piles them up. He can only take the plate\n"
        "        from the TOP. The last plate placed is the first one taken!")

    # Python has no special 'stack' - we simply use a LIST.
    # push = append(),  pop = pop()
    plates = []
    for plate in ["Plate 1", "Plate 2", "Plate 3"]:
        plates.append(plate)                    # PUSH on top
        show("Push", f"{plate}  -> stack = {plates}")

    show("Top plate (peek)", plates[-1])        # look at the top without removing

    while plates:
        taken = plates.pop()                    # POP from top
        show("Pop", f"{taken}  -> stack = {plates}")

    # Real-life uses: Undo button, browser Back button.


# =====================================================================
# 7. QUEUE  -  "The Shop Line"   (First In, First Out)
# =====================================================================
def learn_queue():
    title("7. QUEUE  -  The Shop Line  (FIFO)")
    say("Customers stand in a line at Ravi's shop. The FIRST person to arrive\n"
        "        is served FIRST. Fair and simple!")

    # We use deque (say 'deck'). It is fast at removing from the FRONT.
    line = deque()
    for person in ["Arun", "Bala", "Charu"]:
        line.append(person)                     # ENQUEUE = join at the back
        show("Joined", f"{person}  -> queue = {list(line)}")

    while line:
        served = line.popleft()                 # DEQUEUE = leave from the front
        show("Served", f"{served}  -> queue = {list(line)}")

    # Real-life uses: printer jobs, ticket counters, call centres.


# =====================================================================
# 8. NESTED  -  "Ravi's Whole Village"
# =====================================================================
def learn_nested():
    title("8. NESTED STRUCTURES  -  Ravi's Whole Village")
    say("Real life is not one box. Ravi's village has houses, and each house\n"
        "        has people. We can put structures INSIDE other structures!")

    # A list of dictionaries - extremely common in real projects (e.g. JSON data)
    students = [
        {"name": "Arun", "marks": [80, 90, 85]},
        {"name": "Bala", "marks": [70, 75, 60]},
    ]
    show("First student", students[0])
    show("Arun's name", students[0]["name"])
    show("Arun's 2nd mark", students[0]["marks"][1])

    print("\n   Average marks of each student:")
    for student in students:
        average = sum(student["marks"]) / len(student["marks"])
        print(f"      {student['name']}: {average:.1f}")


# =====================================================================
# 9. SUMMARY  -  The Cheat Sheet
# =====================================================================
def learn_summary():
    title("9. CHEAT SHEET  -  Which one should I use?")
    print("""
   Structure   Brackets   Ordered?   Changeable?   Duplicates?   Story
   ---------   --------   --------   -----------   -----------   --------------
   List        [ ]        Yes        Yes           Yes           Friends Train
   Tuple       ( )        Yes        No            Yes           Sealed Chest
   Dictionary  { k:v }    Yes*       Yes           Keys: No      Phone Book
   Set         { }        No         Yes           No            Sticker Bag
   String      " "        Yes        No            Yes           Ribbon
   Stack       list       LIFO       Yes           Yes           Plate Pile
   Queue       deque      FIFO       Yes           Yes           Shop Line

   * Dictionaries remember insertion order in Python 3.7+

   Quick rules:
     - Need an ordered collection you will change?   -> LIST
     - Data must never change?                       -> TUPLE
     - Need to look up by a name/key?                -> DICTIONARY
     - Need only unique items?                       -> SET
     - Last in, first out?                           -> STACK
     - First in, first out?                          -> QUEUE

   THE END - Ravi's village is now perfectly organised. Happy coding!
""")


# ---------------------------------------------------------------------
# Connect the command-line words to the functions above
# ---------------------------------------------------------------------
TOPICS = {
    "list": learn_list,
    "tuple": learn_tuple,
    "dict": learn_dict,
    "set": learn_set,
    "string": learn_string,
    "stack": learn_stack,
    "queue": learn_queue,
    "nested": learn_nested,
    "summary": learn_summary,
}


def main():
    # argparse reads what you type after the file name in the terminal
    parser = argparse.ArgumentParser(
        description="Python Data Structures story for beginners - The Magic Village of Pyville"
    )
    parser.add_argument(
        "topic",
        nargs="?",                              # optional: can be left empty
        default="all",
        choices=["all"] + list(TOPICS),
        help="which topic to run (default: all)",
    )
    args = parser.parse_args()

    if args.topic == "all":
        for function in TOPICS.values():        # run every topic in order
            function()
    else:
        TOPICS[args.topic]()                    # run just the chosen topic


# This line means: run main() only when we run THIS file directly.
if __name__ == "__main__":
    main()