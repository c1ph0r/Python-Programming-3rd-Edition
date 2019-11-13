# Geek Translator
# Demonstrates using dictionaries

import os

geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque" : "the collection of debris found in computer keyboards.",
        "Link Rot" : "the process by which web page links become obsolete.",
        "Percussive Maintenance" : "the act of striking an electronic device to make it work.",
        "Uninstalled" : "being fired.  Especially popular during the dot-bomb era."}

choice = None

while choice != "0":
    os.system('CLS')
    print(
    """
    Geek Translator
    
    0 - Quit
    1 - Look up a Geek Term
    2 - Add a Geek Term
    3 - Redefine a Geek Term
    4 - Delete a Geek Term
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        os.system('CLS')
        print("\nGoodbye!")

    # get a definition
    elif choice == "1":
        os.system('CLS')
        print("\n", geek.keys())
        term = input("\nWhat term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            os.system('CLS')
            print("\n", term, "means", definition)
            input("\n\nPress the enter key to continue.")
        else:
            os.system('CLS')
            print("\nSorry, I don't know", term)
            input("\n\nPress the enter key to continue.")

    # add a term-definition pair
    elif choice == "2":
        os.system('CLS')
        term = input("\nWhat term do you want to add?: ")
        if term not in geek:
            definition = input("\nWhat's the definition?: ")
            geek[term] = definition
            os.system('CLS')
            print("\n", term, "has been added.")
            input("\n\nPress the enter key to continue.")
        else:
            os.system('CLS')
            print("\nThat term already exists! Try redefining it.")
            input("\n\nPress the enter key to continue.")

    # redefine an existing term
    elif choice == "3":
        os.system('CLS')
        term = input("\nWhat term do you want me to redefine?: ")
        if term in geek:
            definition = input("What's the new definition?: ")
            geek[term] = definition
            os.system('CLS')
            print("\n", term, "has been redefine.")
            input("\n\nPress the enter key to continue.")
        else:
            os.system('CLS')
            print("\nThat term doesn't exist. Try adding it.")
            input("\n\nPress the enter key to continue.")

    # delete a term-definition pair
    elif choice == "4":
        os.system('CLS')
        term = input("\nWhat term do you want to delete?: ")
        if term in geek:
            del geek[term]
            os.system('CLS')
            print("\nOkay I deleted", term)
            input("\n\nPress the enter key to continue.")
        else:
            os.system('CLS')
            print("\nI can't do that!", term, "doesn't exist in the dictionary.")
            input("\n\nPress the enter key to continue.")

    # easter egg
    elif choice == "69":
        os.system('CLS')
        print("\nNice.")
        input("\n\nPress the enter key to continue.")

    # some unknown choice
    else:
        os.system('CLS')
        print("\nSorry, but", choice, "isn't a valid choice.")
        input("\n\nPress the enter key to continue.")

input("\n\nPress the enter key to exit.")