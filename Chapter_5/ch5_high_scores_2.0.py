# High Scores 2.0
# Demonstrates nested sequences
import os
scores = []

choice = None

while choice != "0":

    print(
    """
    High Score Menu 2.0
    
    0 - Quit
    1 - List Scores
    2 - Add a Score
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye.\n")
        input("Press enter to close")

    # display high score table
    elif choice == "1":
        os.system('CLS')
        print("\nHigh Scores:\n")
        print("NAME\t SCORE\n")
        for entry in scores:
            score, name = entry
            print(name,"\t",score)

    # add a score
    elif choice == "2":
        os.system('CLS')
        name = input("\nWhat is the player's name?: \n\n")
        score = int(input("\nWhat score did the player get?: \n\n"))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]     #keep only top 5 scores
        os.system('CLS')

    # some unknown choice
    else:
        os.system('CLS')
        print("Sorry, but", choice, "isn't a valid choice.")