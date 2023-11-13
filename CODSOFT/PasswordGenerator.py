import random
import string

def passwordGenerator(length, letter,number, punctuation):
    chars = ''
    if letter:
        chars += string.ascii_letters
    elif number:
        chars += string.digits
    elif punctuation:
        chars += string.punctuation

    elif not chars:
        return "No characters selected. Please choose at least one character type."

    password = ''.join(random.choice(chars) for i in range(length))
    return password

while True:
    try:
        length = int(input("Enter the password length: "))
        print("Anwer the following questions\n Type (Y/Yes) for yes Or type (N/No) for N0 \t DEFAULT [N/NO]")

        letter = input("Do you want to include letters : ").lower() in ['y', 'yes']

        number = input("Do you want to include numbers: ").lower() in ['y', 'yes']
        
        punctuation = input("Do you want to include punctuation: ").lower() in ['y', 'yes']
        
        if length <= 0:
            print("Enter a valid length.")
        
        else:
            break
    except Exception as e:
        print("Please enter a valid number")

print(f"\nGenerated Password:\t{passwordGenerator(length, letter, number, punctuation)}")