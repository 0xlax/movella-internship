import typer
import getpass
import re


def leasteight(word):
	if len(word) >= 8:
		return True



def count_spec(word):

	special_char = 0

	for i in range(0, len(word)):
		ch = word[i]

		if (word[i].isalpha()):
			continue

		elif (word[i].isdigit()):
			continue
		else:
			special_char += 1

	if special_char >= 2:
		return True
	else:
		return False


def count_num(word):
	number = 0

	for i in range(0, len(word)):
		ch = word[i]

		if (word[i].isdigit()):
			number+=1
		else:
			continue
	if number >= 2:
		return True
	else:
		return False

def check_init(word):
	 if (word[0].isdigit()):
	 	return True
	 else:
	 	return False






def main():
	strength = 0
	pswd = getpass.getpass('Password:')
	# password = input("Enter a password: ")
	print("Password Considered!")
	

	violations = []

	if leasteight(pswd) == True:
		strength += 25
		# print("passed string count")
		# print("Strength: ", strength)
	else:
		violations.append("Less than 8 characters")
		

	if count_spec(pswd) ==  True:
		strength += 30
		# print("passed special alpha count")
		# print("Strength: ", strength)
	else:
		violations.append("Less than 2 Special Characters")

	if count_num(pswd) == True:
		strength += 30
		# print("passed number count")
		# print("Strength: ", strength)
	else:
		violations.append("Less than 2 Numbers")

	if check_init(pswd) == False:
		strength +=15
		# print("passed init check")
		# print("Strength: ", strength)
	else:
		violations.append("Starts with a number")

	if strength < 50:
		print("Password Strength: LOW!")
	elif strength in range(50, 15):
		print("Password Strength: AVERAGE!")
	elif strength in range(75, 90):
		print("Password Strength: GOOD!")
	elif strength >= 90:
		print("Password Strength: VERY GOOD!")

	if strength < 75:
		print("")
		print(violations[0])
		print(violations[1])


		



if __name__ == "__main__":
	typer.run(main)