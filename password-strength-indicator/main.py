import typer
import getpass



def main():
	pswd = getpass.getpass('Password:')
	# password = input("Enter a password: ")
	print("Password Considered!")
	print(pswd)

if __name__ == "__main__":
	typer.run(main)