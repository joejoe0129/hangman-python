import random

word_list = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote",
             "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat", "goose", "hawk", "lion",
             "lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", "otter", "owl", "panda", "parrot",
             "pigeon", "python", "rabbit", "ram", "rat", "raven", "rhino", "salmon", "seal", "shark", "sheep", "skunk",
             "sloth", "snake", "spider", "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel",
             "whale", "wolf", "wombat", "zebra"]
word = random.choice(word_list)
letter_list = list(word.lower())
starline = list((len(word) * "*"))
guesses_left = 5
guessed_letters = []

while guesses_left > 0:

    print("Guess an animal")
    print("Here's what you have: " + ("".join(starline)))
    print("you have " + str(guesses_left) + " guesses left")
    print("you have guessed: " + str(guessed_letters))
    guess = input("put a letter: ")
    print("-------------------------------------------------")

    guess = guess.lower()
    guessed_letters.append(guess)
    found_match = False
    char_index = 0
    for char in letter_list:
        if char == guess:
            found_match = True
            starline[char_index] = guess
        char_index = char_index + 1

    if found_match:
        print("correct")
    if not found_match:
        guesses_left = guesses_left - 1
        print("wrong")

    if "".join(starline) == "".join(letter_list):
        print("the animal was ")
        print(word)
        print("you win")
        print("-------------------------------------------------")
        break

    if guesses_left == 5:
        print(
            '''
       +---+
       |   |
           |
           |
           |
           |
     =========
        ''')
    if guesses_left == 4:
        print(
            '''        
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''')
    if guesses_left == 3:
        print(
            '''        
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
        ''')
    if guesses_left == 2:
        print(
            ''''        
                +---+
                |   |
                O   |
               /|\\  |
                    |
                    |
                =========
                ''')
    if guesses_left == 1:
        print(
            ''''        
                +---+
                |   |
                O   |
               /|\\  |
               /    |
                    |
                =========
                ''')
    if guesses_left == 0:
        print(
            ''''        
                +---+
                |   |
                O   |
               /|\\  |
               / \\  |
                    |
                =========
                ''')
        print("".join(starline))
        print("you lost")
        print("the animal was " + str(word))
        print("-------------------------------------------------")
