import csv
import os
import random
import string

from passwordmeter import test

# Dictionary of all Websites and their stored passwords
passwords = {}


# Generates a random password
def generate_Password(num=4):
    password = []

    for x in range(num):
        up = random.choice(string.ascii_uppercase)
        low = random.choice(string.ascii_lowercase)
        sym = random.choice(string.punctuation)
        num = random.choice(string.digits)
        password.append(up)
        password.append(low)
        password.append(sym)
        password.append(num)

    gen = ''.join(str(x) for x in password)

    return gen


# Stores a given password for a given site then stores it as a dictionary in a file
def store_Password(key, password):
    r = csv.reader(open("passwords.csv"))  # reads in passwords.csv

    for row in r:
        passwords[row[0]] = row[1]  # sets the dictionary = to all the values in the passwords.csv file

    # Checks to see if the given key (Website / app) is already stored in the dictionary
    if str(key) in passwords:
        print('A Password for ' + key + ' already exists')
        print("You can find the password using the Get password function or option 4")
    else:
        passwords[str(key)] = encrypt(str(password))
        # checks to see if the file is empty
        if os.stat('passwords.csv').st_size == 0:
            w = csv.writer(open("passwords.csv", 'w'))  # opens a csv writer
            for key, val in passwords.items():
                w.writerow([key, val])  # writes all of the values in the passwords dictionary into the password.txt
                # file

            r = csv.reader(open("passwords.csv"))  # reads in passwords.csv

            for row in r:
                passwords[row[0]] = row[1]  # sets the dictionary = to all the values in the passwords.csv file

            print("Password has been saved")
        else:
            w = csv.writer(open("passwords.csv", 'a+', newline=''))  # opens a csv writer that appends to the end of
            # the file
            w.writerow([key, encrypt(password)])  # appends the value of the given key in the passwords dictionary into the
            # password.txt file


            print("Password has been saved!")


# Returns the password of the given website
def get_Password(key):
    r = csv.reader(open("passwords.csv"))  # reads in passwords.csv

    for row in r:
        passwords[row[0]] = row[1]  # sets the dictionary = to all the values in the passwords.csv file

    # Checks to see if the given key(Website / app) is already stored in the dictionary
    if str(key) in passwords:
        decrypted_pass = decrypt(passwords[str(key)])
        print("Your password for " + key + " is: " + decrypted_pass)
    else:
        print("\nyou don't have a pass word for", str(key))
        print("you can store one for " + key + " by selecting option 2")


# Tests the strength of a given password
def test_Password(password):
    print("\n0 is not secure at all and 100 is extremely secure")
    print(test(password)[0] * 100)


# Changes the stored password of the given key (Website/ app)
def change_Password(key, password):
    r = csv.reader(open("passwords.csv"))  # reads in passwords.csv

    for row in r:
        passwords[row[0]] = row[1]  # sets the dictionary = to all the values in the passwords.csv file

    # Checks to see if the given key(Website / app) is already stored in the dictionary
    if str(key) in passwords:

        del passwords[str(key)]  # delete the current stored key and password
        passwords[str(key)] = password  # set the same key equal to the new given password
        w = csv.writer(open("passwords.csv", 'w'))  # opens a csv writer
        for key, val in passwords.items():
            w.writerow([key, val])  # writes all of the values in the passwords dictionary into the password.txt
            # file
    else:
        print("No password exits for this site/ app. Please Store a password using the "
              "Store password function(Option 2)")


def delete_Password(key):
    r = csv.reader(open("passwords.csv"))  # reads in passwords.csv

    for row in r:
        passwords[row[0]] = row[1]  # delete the current stored key and password

    # Checks to see if the given key(Website / app) is already stored in the dictionary
    if str(key) in passwords:

        # confirms if ghe user wants to delete the pass word fo the given key (Website/ app)
        confirm = input("Are you sure you want to delete the password for " + key + "\nEnter 1 for yes or 0 for no: ")

        if confirm == 1:

            del passwords[str(key)]  # delete the current stored key and password

            w = csv.writer(open("passwords.csv", 'w'))  # opens a csv writer
            for key, val in passwords.items():
                w.writerow([key, val])  # writes all of the values in the passwords dictionary into the password.txt
                # file

            print("Password Deleted")
        else:
            print("Deletion Canceled!")

    else:
        print("No password exits for this site/ app. Please Store a password using the "
              "Store password function(Option 2)")

def encrypt(password):
    encrypted = ""
    r = random.randrange(0, 100)
    identifier = chr(r + 100)
    string = password[::-1]
    for s in string:
        encrypted = encrypted + chr(ord(s) + r)
    encrypted = encrypted + identifier
    return encrypted

def decrypt(password):
    decrypted = ""
    key = password[len(password) - 1:]
    key = ord(key) - 100
    encrypted = password[0: len(password) - 1]
    for e in encrypted:
        decrypted = decrypted + chr(ord(e) - key)
    decrypted = decrypted[::-1]
    return decrypted




def _main_():
    run = True
    print("Welcome to Spencer Prentiss' Password Manager!")
    while run:
        print("\n1. Generate a new password")
        print("2. Store a password for a site/ app")
        print("3. Test the strength of your passwords")
        print("4. Get the password for a particular site/ app")
        print("5. Change the password for a particular site/ app")
        print("6. Delete the password for a particular site/ app")

        case = input("\nSelect 1, 2, 3, 4, 5 or 6: ")

        # Generates a random password when option 1 is selected
        if int(case) == int(1):
            gen_Pass = generate_Password()
            print("your generated password is " + gen_Pass)
            choice = input("Would you like to store this password for a site/ app?\nEnter 1 for yes or 0 for no: ")
            if int(choice) == 1:
                key = input("Please enter a website or app:")
                print("Are you sure this is the password you want for " + key + "?  [" + gen_Pass + "] ")
                confirm = input("Enter 1 for yes and 0 for no: ")
                if int(confirm) == 1:
                    store_Password(key, gen_Pass)
                    reRun = input("Would you like to continue? 1 for yes 0 for no: ")
                    if int(reRun) == 0:
                        print("\nThank you for using Spencer Prentiss's Password Manager")
                        break
                    else:
                        continue
            elif int(choice) == 0:
                reRun = input("Would you like to continue? 1 for yes 0 for no: ")
                if int(reRun) == 0:
                    print("\nThank you for using Spencer Prentiss's Password Manager")
                    break
                else:
                    run = True

        # Stores the the given password for th given key ( Website/ app) when option 2 is selected
        elif int(case) == int(2):
            key = input("Please enter a website or app: ")
            password = input("Please enter your desired password: ")
            print("Are you sure this is the password you want for " + key + "?  [" + password + "] ")
            confirm = input("Enter 1 for yes and 0 for no: ")
            if int(confirm) == 1:
                store_Password(key, password)
                reRun = input("Would you like to continue? 1 for yes 0 for no: ")
                if int(reRun) == 0:
                    print("\nThank you for using Spencer Prentiss's Password Manager")
                    break
                else:
                    run = True

        # Tests Password strength when option 3 is selected
        elif int(case) == 3:
            tested_Pass = input("Type the password you'd like to test: ")
            test_Password(tested_Pass)
            reRun = input("Would you like to continue? 1 for yes 0 for no: ")
            if int(reRun) == 0:
                print("\nThank you for using Spencer Prentiss's Password Manager")
                break
            else:
                run = True

        # Returns the password for the given key (Website / app) when option 4 is selected
        elif int(case) == 4:
            key = input("Enter in a website name or app name: ")
            get_Password(key)
            reRun = input("Would you like to continue? 1 for yes 0 for no: ")
            if int(reRun) == 0:
                print("\nThank you for using Spencer Prentiss's Password Manager")
                break
            else:
                run = True

        # Changes the password of the given key when option 5 is selected
        elif int(case) == 5:
            key = input("Enter in a website name or app name who's password yo want to change: ")
            new_Pass = input("Type the new password you'd like to store")
            change_Password(key, new_Pass)
            reRun = input("Would you like to continue? 1 for yes 0 for no: ")
            if int(reRun) == 0:
                print("\nThank you for using Spencer Prentiss's Password Manager")
                break
            else:
                run = True
        # Changes the password of the given key when option 6 is selected
        elif int(case) == 6:
            key = input("Enter in a website name or app name who's password you want to delete: ")
            delete_Password(key)
            reRun = input("Would you like to continue? 1 for yes 0 for no: ")
            if int(reRun) == 0:
                print("\nThank you for using Spencer Prentiss's Password Manager")
                break
            else:
                run = True
        # Occurs when any other option is typed other than the 6 listed
        else:
            print("That's not a valid input")
            run = False


_main_()
