import typer
import getpass

def leasteight(word):
	if len(word) >= 8:
		return True


def main():
	pswd = getpass.getpass('Password:')
	# password = input("Enter a password: ")
	print("Password Considered!")
	print(pswd)

	if leasteight(pswd) == True:
		print("passed string count")

if __name__ == "__main__":
	typer.run(main)