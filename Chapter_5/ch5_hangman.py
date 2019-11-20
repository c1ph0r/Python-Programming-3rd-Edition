# Hangman Game
#
# The classic game of Hangman.  The computer picks a random word
# and the player tries to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports
import random
import os

# constants
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("GALAGA", "TETRIS", "ZELDA", "MINECRAFT", "FORTNITE")

# initialize variables
word = random.choice(WORDS)  # the word to be guessed
so_far = "-" * len(word)  # one dash for each letter in word to be guessed
wrong = 0  # number of wrong guesses player has made
used = []  # letters already guessed

print("\n\tWelcome to Gamer Hangman.")
print("\n\tGood Luck Nerds!")
print(
  """

\t      |_______________``|
\t       [/]           [  ]
\t       [\]           | ||
\t       [/]           |  |
\t       [\]           |  |
\t       [/]           || |
\t      [---]          |  |
\t      [---]          |@ |
\t      [---]          |  |
\t     oOOOOOo         |  |
\t    oOO___OOo        | @|
\t   oO/|||||\Oo       |  |
\t   OO/|||||\OOo      |  |
\t   *O\ x x /OO*      | ||
\t   /*|  c  |O*\      |  |
\t  /   \_O_/    \     |  |
\t  |    \#/     |     | ||

"""
)

input("\n\n\tPress the enter key to begin.\n\t\t      ")

while wrong < MAX_WRONG and so_far != word:
    os.system('CLS')
    print(HANGMAN[wrong])
    print("\n\tYou've used the following letters:\n\t", used)
    print("\n\tSo far, the word is:\n\t", so_far)

    guess = input("\n\n\t\tEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("\tYou've already guessed the letter", guess)
        guess = input("\t\tEnter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\n\n\tYes!", guess, "is in the word!")
        input("\n\tPress the enter key to continue.")

        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\n\n\tSorry,", guess, "isn't in the word.")
        input("\n\tPress the enter key to continue.")
        wrong += 1

if wrong == MAX_WRONG:
    os.system('CLS')
    print(
        """
               ______
            .-"      "-.
          /             '
         |              |
         |,  .-.  .-.  ,|
         | )(__/  \__)( |
         |/     /\     \|
         (_     ^^     _)
          \__|IIIIII|__/
           | \IIIIII/ |
           \          /
            `--------`
                       """
    )
    print("\n\n\tYou've been hanged!")
else:
    os.system('CLS')
    print(
  """
\t                                                         ,jf
\t                                                        ,jf)
\t   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
\t ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
\t 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
\tjK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
\t NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
\t                         ,gF',@'
\t                        :8K  j8
\t                         "*w*"
                         """
    )
    print("\n\tYou guessed it!")

print("\n\n\tThe word was", word)

input("\n\n\tPress the enter key to exit.")
