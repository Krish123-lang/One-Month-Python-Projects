import os


def display_menu():
    print("\n" + "=" * 45)
    print("             CRUD FILE")
    print("=" * 45)
    print("1. Create")
    print("2. Update")
    print("3. Read")
    print("4. Delete")
    print("5. Exit")
    print("=" * 45)


def get_menu_choice():
    """Get a valid menu choice from the user."""

    while True:
        choice = input("Enter your option (1-5): ").strip()

        if choice in {"1", "2", "3", "4", "5"}:
            return choice

        print("Error: Please enter a number between 1 and 5.")


def createfile(file_name, content):
    if os.path.exists(file_name):
        print("-" * 45)
        return f"{file_name} already exist! Please choose another name."
    else:
        with open(file_name, "w") as f:
            f.write(content)
        print("-" * 45)
        return f"{file_name} has been created !"


def updatefile(file_name, old_content, new_content):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            file_content = f.read()

        updated_content = file_content.replace(old_content, new_content)
        with open(file_name, "w") as f:
            f.write(updated_content)
        print("-" * 45)
        return f"{file_name} has been updated !"
    else:
        print("-" * 45)
        return f"{file_name} does not exists !"


def readfile(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            read_file = f.read()
        return read_file
    else:
        print("-" * 45)
        return f"{file_name} does not exists !"


def deletefile(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} has been deleted.")
    else:
        print("The file does not exist!")


def main():
    while True:
        display_menu()
        user_inp = get_menu_choice()

        if user_inp == "1":
            file_name = input("Enter file name (with extension): ").strip()
            content = input("Enter the content: ")
            print(createfile(file_name, content))

        elif user_inp == "2":
            file_name = input("Enter file name (with extension): ").strip()
            old_content = input("Enter the text to be updated: ")
            new_content = input("Enter the new content to update: ")
            print(updatefile(file_name, old_content, new_content))

        elif user_inp == "3":
            file_name = input("Enter the file name: ")
            print("-" * 45)
            print(readfile(file_name))

        elif user_inp == "4":
            file_name = input("Enter file name (with extension): ").strip()
            deletefile(file_name)

        elif user_inp == "5":
            print("Bye Bye")
            break
        else:
            print("Invlaid Option !")


if __name__ == "__main__":
    main()
