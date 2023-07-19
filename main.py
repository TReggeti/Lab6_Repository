# Lab 6 done by Thomas Reggeti and Shashank Navale
def encode(password):
    """
    since we are only dealing with 1 character numbers, I simply put 7-9 to change to the correct number rather than
    bother with actually adding like the rest
    """
    new_password = ""
    for i in range(len(password)):
        if password[i] == "7":
            new_password += "0"
        elif password[i] == "8":
            new_password += "1"
        elif password[i] == "9":
            new_password += "2"
        else:
            char = str(int(password[i]) + 3)
            new_password += char
    return new_password


def decode(password):
    decoded = ""  # initializes an empty decoded string variable

    for element in password:
        if element == "0":
            decoded += "7"

        elif element == "1":
            decoded += "8"

        elif element == "2":
            decoded += "9"
        # above portion of code replaces necessary characters

        else:
            decoded += str(int(element) - 3)  # shifts down rest of the elements by 3

    return decoded  # returns the decoded string


def main():
    global encoded_password
    old_password = ""
    while True:
        # for option 1 I kept the old password and encoded password separate so that they can be called in option 2
        print()
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            print("Please enter your password to encode: ", end="")
            old_password += input()
            encoded_password = encode(old_password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            if len(old_password) == 0:  # checks if old password is empty
                print("No password encoded yet. Please use Option 1.")  # prompts user to use Option 1
                continue # continues the loop
            decoded_password = decode(encoded_password)  # decodes the previously encoded password
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif option == 3:
            break  # exits out of the program

        else:
            print("This isn't a valid option! Please try again.\n")  # prompts user to enter valid option


if __name__ == '__main__':
    main()
