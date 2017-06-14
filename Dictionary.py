# MENU
import json

slovnik = {}

with open("slovnik.txt") as data:
	slovnik = json.load(data)

def menu():
	user_input = input("\nWhat do you want?\n 'T' to Translate EN -> CZ\n 'A' to Add or Edit word\n 'V' to View dictionary\n 'R' to Remove\n 'X' to Exit\nYour choise: ")
		
	if user_input.lower() == "t":
		preklad()

	elif user_input.lower() == "a":
		pridat()

	elif user_input.lower() == "x":
		exit()
	
	elif user_input.lower() == "v":
		ukazka()
	
	elif user_input.lower() == "r":
		smazat()
	
	else:
		print("\nIncorrect option! Hit Enter to continue.")
		input()
		menu()

def preklad():
	user_input2 = input("\nWrite name of the animal in english: ")
	if user_input2 in slovnik:
		print(user_input2, "=>", slovnik.get(user_input2))
		input()
		menu()	
	else:
		print("\nIt is not in the dictionary!")
		user_input5 = input("Do you want to go back to translate (type T) or to go back (type B): ")
		if user_input5.lower() == "t":
			preklad()
		elif user_input5.lower() == "b":
			menu()
		else:
			print("\nIncorrect option! Hit Enter to continue.")
			input()
			menu()	


def pridat():
	user_input3 = input("\nType name of the animal in english: ")
	user_input4 = input("Type name of the animal in czech: ")
	slovnik[user_input3] = user_input4
	print("\nDictionary:\n")
	for k, v in slovnik.items():
		print(k, v)
	with open("slovnik.txt", "w") as data:
		data.write(json.dumps(slovnik))
	input("\nHit Enter to continue. \n")
	menu()

def ukazka():
	print("\nDictionary:\n")
	for k, v in slovnik.items():
		print(k, v)
	input("\nHit Enter to continue.")
	menu()

# správná varianta

# for k, v in a.items():
#	print(k, v)

	
# špatná varianta
	
#for k in a:
#	 print(k, a[k])	

def smazat():
	for k, v in slovnik.items():
		print(k, v)
	user_input6 = input("\nType name of the animal you want to delete: ")
	if user_input6 in slovnik:
		print("Do you really want to delete: ",user_input6,"?")
		user_input7 = input("Type 'Y' or 'N': ")
		if user_input7.lower() == "y":
			del slovnik[user_input6]
			print("\nDictionary:\n")
			for k, v in slovnik.items():
				print(k, v)
			with open("slovnik.txt", "w") as data:
				data.write(json.dumps(slovnik))
		elif user_input7.lower() == "n":
			menu()
		else:
			print("\nIncorrect option! Hit Enter to continue.")
			input()
			menu()	
	else:
		print("\n", user_input6, " is not in the dictionary! Hit Enter to continue.")
	input("\nHit Enter to continue. \n")
	menu()


menu()



