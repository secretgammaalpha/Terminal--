import random

def Generate():
    PasswordLength = int(input("Password Length: "))

    UpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LowerCase = "abcdefghijklmnopqrstuvwxyz"
    Numbers = "0123456789"
    SpecialCharacters = "!@#$%&*."

    touse = UpperCase + LowerCase + Numbers + SpecialCharacters

    password = "".join(random.sample(touse,PasswordLength))
    print('\n\nPassword Generated!\n\n')
    return password