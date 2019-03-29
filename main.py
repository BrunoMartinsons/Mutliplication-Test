"""Main file where the program is run"""
from classes.database import Database as db

def login_screen():
    """Displays the login screen to users"""
    logged_in = False  # User is not logged in
    while logged_in == False:  # Whilst user is not logged in display the login screen
        school_name = "St. test primary school"  # Store school name
        print("°------------------------------------------------------°")
        print("Welcome to " + school_name + " Multiplication program\n")
        username = input("Username: ")
        password = input("Password: ")
        print("\n°------------------------------------------------------°\n\n")
    

def admin_screen():
    choice_taken = False # User has not made a choice
    while choice_taken == False:
        print("°------------------------------------------------------°")
        print("Welcome to the Admin menu.\n")
        print("1 - Create Teacher account")
        print("2 - Create Student account")
        print("3 - Delete Teacher account")
        print("4 - Delete Student account\n")
        choice = input("What would you like to do: ")  # Choice stored as string

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print("Invalid choice, try again.\n")


def teacher_screen():
    pass


def student_screen():
    pass


login_screen()