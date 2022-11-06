from main import count_spec, count_num, check_init
import getpass


def test_count():
	
	assert count_spec("pass#rd") == True, "Function count_spec fails to check special character count"

def test_num():
	assert count_num("pass2ord") == True, "Function count_spec fails to check number of Numbers in password"
	

if __name__ == "__main__":
    test_count()
    test_num()
    print("Everything passed")