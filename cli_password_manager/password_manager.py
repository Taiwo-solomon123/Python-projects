from ast import Pass
import shelve
from urllib import response
import pyperclip


manager=shelve.open("manager")

def key_validation(key, db):
    if key in db:
        return True
    else:
        return False

            
    
def add_password():
    app_name=input("ENTER APP/SITE NAME: ").lower()
    if app_name in manager:
        print(f"{app_name.capitalize()} already in database should i go ahead and edit?(y/n)")
        while True:
            response=input(">>> ").lower()
            if response == "y":
                edit_password()
            elif response=="n":
                break
            else:
                print("wrong input...")
    else:
        password=input("ENTER PASSWORD: ")
        manager[app_name]=password
        print("\n", "PASSWORD SAVE AND SECURE")   
def edit_password():
    while True:
        app_name=input("ENTER APP/SITE NAME: ").lower()
        if key_validation(app_name, manager):
            pass
        else:
            print(f"KeyError.... {app_name} not in database")
            continue
        password=input("ENTER PASSWORD: ")
        manager[app_name]=password
        print("\n", "PASSWORD EDITED")
        break
def delete_password():
    while True:
        app_name=input("ENTER APP/SITE NAME: ").lower()
        if key_validation(app_name, manager):
            del manager[app_name]
            print("PASSWORD EDITED")
            break
        else:
            print(f"KeyError.... {app_name} not in database")
    
def show_passwords():
    if manager:
        for app_name, password in manager.items():
            print(f"{app_name.upper()}==>    {password}")
    else:
        print("\n", "NOTHING TO SHOW HERE")
def get_password():
    while True:
        app_name=input("ENTER APP/SITE NAME: ").lower()
        if key_validation(app_name, manager):
            print(f"{app_name} Password: {manager[app_name]}")
            break
        else:
            print(f"KeyError.... {app_name} not in database")
def copy_password():
    while True:
        app_name=input("ENTER APP/SITE NAME: ").lower()
        if key_validation(app_name, manager):
            password=manager[app_name]
            pyperclip.copy(password)
            print("\n", f"{app_name.upper()}'s has been added to your clipboard and is ready to paste!")
            break
        else:
            print(f"KeyError.... {app_name} not in database")
    
    
def password_manager():
    message= """
    COMMAND LINE PASSWORD MANAGER
    YOU CAN PERFORM THE OPERATIONS BY PASSING THE FOLLOWING COMMANDS:
    ADD: Toadd new password to database
    DEL: To delete an existing password from database
    EDIT: To edit an existing password in database
    SHOW: To show all password in database
    GET: To retrive a password from database
    COPY: To copy a site password to clipboard
    BREAK: To terminate program
    """
    commands=["add", "del", "edit", "show", "get", "break", "copy"]
    terminate=False
    print(message)
    while not terminate:
        print("Enter a command")
        command=input(">>> ")
        if command in commands:
            if command=="add":
                add_password()
            elif command=="del":
                delete_password()
            elif command=="edit":
                edit_password()
            elif command=="show":
                show_passwords()
            elif command=="get":
                get_password()
            elif command=="copy":
                copy_password()
            else:
                terminate=True
        else:
            print("input not a command")
            print()
        

def main():
    #Ask to enter master password
    while True:
        master_password="1234"
        print("Enter master Password")
        password = input(">>> ")
        if password == master_password:
            password_manager()
            break
        else:
            print("Wrong input!")

if "__main__"==__name__:
    main()
    

        
        
    