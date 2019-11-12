# Hero's Inventory 3.0
# Demonstrates lists

# create a list with some items and display with a for loop
inventory = ["sword",
             "armor",
             "shield",
             "healing potion"]
print("\nYour items:\n")
for item in inventory:
    print(item)
input("\nPress the enter key to continue.")

# get the length of a list
print("\nYou have", len(inventory), "items in your possession.")
input("\nPress the enter key to continue.")

# test for membership with in
if "healing potion" in inventory:
    print("\nYou will live to fight another day.")

# display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("\nAt index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("\nEnter the index number to end the slice: "))
print("\ninventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])
input("\nPress the enter key to continue.")

# concatenate two lists
chest = ["gold", "gems"]
print("\nYou find a chest. It contains:\n")
print(chest)
print("\nYou add the contents of the chest to your inventory.")
inventory += chest
print("\nYou inventory is now:\n")
print(inventory)
input("\nPress the enter key to continue.")

# assign by index
print("\nYou trade your sword for a crossbow.")
inventory[0]= "crossbow"
print("\nYour inventory is now:\n")
print(inventory)
input("\nPress the enter key to continue.")

# assign by slice
print("\nYou use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("\nYour inventory is now:\n")
print(inventory)
input("\nPress the enter key to continue.")

# delete an element
print("\nIn a great battle , your shield is destroyed.")
del inventory[2]
print("\nYour inventory is now:\n")
print(inventory)
input("\nPress the enter key to continue.")

# delete a slice
print("\nYour crossbow and armor are stolen by thieves.")
del inventory[:2]
print("\nYour inventory is now:\n")
print(inventory)
input("\nPress the enter key to continue.")