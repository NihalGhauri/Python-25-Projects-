import random

def main():
    print("================================================")

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

    number = int(input('Amount of Passwords to generate: '))
    length = int(input('Input length of password: '))

    print("================================================")
    print('\tHere are your passwords:')

    for i in range(number):
        password = ''
        for a in range(length):
            password += random.choice(chars)
        print(password)  

    print("================================================")

if __name__ == '__main__':
    main()
