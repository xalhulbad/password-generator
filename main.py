import secrets
import string
from random import shuffle, randint

SPECIAL = "!@#$%"


def generate_password() -> str:
    """
    Return a randomly-generated 14-16 character password containing at least one
    uppercase letter, one lowercase letter, one digit, and one special
    character.
    :return: str
    """

    # Determine password length and number of each character type
    num_letters = randint(14, 16)
    num_lowercase = randint(1, num_letters - 3)
    num_uppercase = randint(1, num_letters - num_lowercase - 2)
    num_digits = randint(1, num_letters - num_lowercase - num_uppercase - 1)
    num_special = randint(1, num_letters - num_lowercase - num_uppercase - num_digits)

    password_characters = []
    for i in range(num_lowercase):
        password_characters.append(secrets.choice(string.ascii_lowercase))
    for i in range(num_uppercase):
        password_characters.append(secrets.choice(string.ascii_uppercase))
    for i in range(num_digits):
        password_characters.append(secrets.choice(string.digits))
    for i in range(num_special):
        password_characters.append(secrets.choice(SPECIAL))

    shuffle(password_characters)
    return "".join(password_characters)


if __name__ == "__main__":
    print(generate_password())
