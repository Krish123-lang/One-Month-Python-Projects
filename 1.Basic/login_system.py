from getpass import getpass
users = {}


def register():
    fullname = input("Enter fullname: ").strip()
    email = input("Enter email address: ").strip().lower()

    if '@' not in email or '.' not in email:
        print("Invalid email !")
        return

    password = getpass("Enter password: ")

    if len(password) < 8:
        print("Password must be atleast 8 characters long .")
        return
    elif not password.isalnum():
        print("Password must contain atleast one number.")
        return
    else:
        print("Password must be atleast 8 characters long and must contain atleast one number.")
        

    confirm_password = getpass("Confirm password: ")

    if not fullname or not email or not password or not confirm_password:
        print("Fill all the fields .")
        return

    if email in users:
        print("Email already exists !")
        return

    if password != confirm_password:
        print("Password do not match .")
        return

    users[email] = {
        "fullname": fullname,
        "password": password
    }
    print("Registration successfull !")
    print(users)


def login():
    email = input("Enter email: ").strip().lower()
    password = getpass("Enter password: ")

    if email not in users:
        print("Email not found !")
        return
    if users[email]["password"] == password:
        print(f"Welcome, {users[email]["fullname"]} !")
    else:
        print("Incorrect password")


while True:
    user_choice = input('''
    =================== Authentication System ===================
    1. Register
    2. Login
    3. Exit
    ''')

    if user_choice == "1":
        register()
    elif user_choice == "2":
        login()
    elif user_choice == "3":
        print("Good Bye !")
        break
    else:
        print("Invalid option !")
