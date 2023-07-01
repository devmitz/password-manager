import csv
from random import choice
from time import sleep

def main():

    initial_message()

    c = input("Do you wanna read your passwords? (Y/N): ")
    print()

    if c == 'Y' or c == 'y':
        read_password()
    else:
        generate_password()
    
    exit = input("Press any key to exit...")

def initial_message():
    print("==================================")
    print("----Password Generator by Mitz----")
    print("==================================")

def generate_password():
    name_site = input("Site: ")
    name_site = name_site.title()

    login = input("E-Mail or Username: ")

    number_char =input("Number of lenght in the password: ")
    number_char = int(number_char)
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456790!@#$%&*'
    new_password = ''

    for i in range(number_char):
        num = choice(chars)
        new_password += num 
    
    print(f"\nSite: {name_site}\nLogin: {login}\nPassword: {new_password}")

    print("\nSaving...")

    with open('psswd.csv', 'a', newline='') as csv_file:
        fieldnames = ['name_site','login','password']
        csv_file = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_file.writerow({'name_site' : name_site, 'login' : login, 'password' : new_password})
    
    sleep(1)

def read_password():
    
    print("----------------------------------------")

    with open('psswd.csv', 'r', newline='') as csv_reader:
        csv_reader = csv.DictReader(csv_reader, delimiter=',')    
        for row in csv_reader:
            print(f"Site: {row['name_site']}")
            print(f"Username or E-Mail: {row['login']}")
            print(f"Password: {row['password']}")
            print("----------------------------------------")
    
    sleep(1)
        
if "__main__" == __name__:
    main()