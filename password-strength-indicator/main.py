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


def main():
	strength = 0
	pswd = getpass.getpass('Password:')
	# password = input("Enter a password: ")
	print("Password Considered!")
	print(pswd)

	if leasteight(pswd) == True:
		strength += 25
		print("passed string count")
		print("Strength: ", strength)
	else:
		print("failed string count")

	if count_spec(pswd) ==  True:
		strength += 25
		print("passed special alpha count")
		print("Strength: ", strength)
	else:
		print("failed special alpha")



if __name__ == "__main__":
	typer.run(main)