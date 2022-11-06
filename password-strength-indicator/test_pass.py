from main import count_spec, count_num, check_init
import getpass


def test_count():
	word = getpass.getpass('Password:')
	assert count_spec(word) == True


if __name__ == "__main__":
    test_count()
    print("Everything passed")