import random
import string

def passwordgenerate(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    pwd = ''.join(random.choice(characters) for i in range(length))
    return pwd

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the length of your desired password: "))
    # Generate the password
    pwd = passwordgenerate(length)
    # Display the password
    print("The Generated password is :", pwd)

if __name__ == "__main__":
    main()
