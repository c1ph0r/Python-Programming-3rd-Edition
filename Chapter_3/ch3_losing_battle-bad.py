# Doug's Losing Battle
# Demonstrates the dreaded infinite loop

print("The lone Doug is surrounded by a massive army of trolls.")
print("Their non-Dougness, offending him with the anger of 1000 suns.")
print("Your Doug unsheathes his keyboard for his final showdown.\n")

health = 10
trolls = 0
damage = 3

while health != 0:
    trolls += 1
    health -= damage

    print("Doug unleashes hell on the next troll, " \
          "but takes" , damage, "damage points.\n")

print("Doug has fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")