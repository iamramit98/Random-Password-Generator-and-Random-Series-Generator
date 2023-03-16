# necessary imports
import secrets
import string
import random
import numpy

def password_dt(ln):
    letters = string.ascii_letters
    digits = numpy.array([1, 2, 3, 4, 5])
    special_chars = string.punctuation

    digits = random.choice(string.digits)

    alphabet = letters + digits + special_chars

    pwd_length = int(ln)

    if pwd_length>= 6 and pwd_length<= 64:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        while True:
            pwd = ''
            for i in range(pwd_length):
                pwd += ''.join(secrets.choice(alphabet))

            if (any(char in special_chars for char in pwd) and
                    sum(char in digits for char in pwd) >= 2):
                break
    else:
        print("Password Not between 6 and 64 Characters")
    return pwd


#password_dt()
