import random
import time

#Welcome banner.
print()
print("-------------------------")
print("Welcome to Dice Roller!")
print("-------------------------")
print()

#List of dice choices
dice_options = ('d%', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20')

while True:
	#User Dice Selection
	print("*** Dice Options ***")
	print("D%\nD4\nD6\nD8\nD10\nD12\nD20")

	#Line breaks for visual breakup
	print()
	print("-------------------------")
	print()

	dice_selection = input("Select a dice to roll: ").lower()

	if dice_selection in dice_options:
		print(f"You selected {dice_selection.upper()}.")
	else:
		print("That is not a dice option.")

	if dice_selection == "d20":
		print (f"Rolling {dice_selection.upper()}......")
		print()
		roll = random.randint(1,20)
		print(f"Roll result: {roll}\n")

	elif dice_selection == "d12":
		print(f"Rolling {dice_selection.upper()}.....")
		print()
		roll = random.randint(1,12)
		print(f"Roll result: {roll}\n")

		print("-------------------------")
		print()

	elif dice_selection == "d10":
                print(f"Rolling {dice_selection.upper()}.....")
                print()
                roll = random.randint(1,10)
                print(f"Roll result: {roll}\n")

                print("-------------------------")
                print()

	elif dice_selection == "d8":
                print(f"Rolling {dice_selection.upper()}.....")
                print()
                roll = random.randint(1,8)
                print(f"Roll result: {roll}\n")

                print("-------------------------")
                print()
	elif dice_selection == "d6":
                print(f"Rolling {dice_selection.upper()}.....")
                print()
                roll = random.randint(1,6)
                print(f"Roll result: {roll}\n")

                print("-------------------------")
                print()

	elif dice_selection == "d4":
                print(f"Rolling {dice_selection.upper()}.....")
                print()
                roll = random.randint(1,4)
                print(f"Roll result: {roll}\n")

                print("-------------------------")
                print()


	roll_again = input ("Would you like to roll again [Y/n]: ") or "Y".lower()
	if roll_again == "y":
		print()

	else:
		print("Thanks for rolling the dice!")
		break
