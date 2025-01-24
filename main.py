import random # stuff to do: add swift error handling to pass history management
import os
import logo
from pystyle import Colors, Write

def clear(next_function=None, *args):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(logo.logo(), "\n")
    if next_function:
        next_function(*args)  

def main():
    options = {1: "Generate Password", 2: "Manage Password History", 3: "Credits"}
    Write.Print("Choose an option:", Colors.blue_to_purple, interval = 0.025)
    for key, value in options.items():
        Write.Print(f"\n{key}. {value}", Colors.blue_to_purple, interval = 0.0025)

    choice = Write.Input("\nEnter your choice: ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if choice == "1":
            clear(generate_password)
        elif choice == "2":
            clear(manage_password_history)
        elif choice == "3":
            clear(creditss)
        else:
            Write.Print("Invalid choice. Please try again.", Colors.blue_to_purple, interval = 0.025)
            choice = Write.Input("Enter your choice: ", Colors.blue_to_purple, interval = 0.025)

def generate_password():
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    special_chars = "!#$%&?@_~"

    while True:
        try:
            length = int(Write.Input("Enter your desired password's length (min: 3, max: 50): ", Colors.blue_to_purple, interval = 0.025))
            if 3 <= length <= 50:
                break
            else:
                Write.Print("Invalid length. Password length should be between 3 and 50 characters.", Colors.blue_to_purple, interval = 0.025)
        except ValueError:
            Write.Print("Invalid input. Please enter a valid integer.", Colors.blue_to_purple, interval = 0.025)

    lowerchars = Write.Input("Include lower case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if lowerchars.lower() == "y":
            break
        elif lowerchars.lower() == "n":
            lower_chars = ""
            break
        else:
            Write.Print("Invalid input Please enter 'y' or 'n'.", Colors.blue_to_purple, interval = 0.025)
            lowerchars = Write.Input("Include lower case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)

    upperchars = Write.Input("Include upper case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if upperchars.lower() == "y":
            break
        elif upperchars.lower() == "n":
            upper_chars = ""
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.", Colors.blue_to_purple, interval = 0.025)
            upperchars = Write.Input("Include upper case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)

    nums = Write.Input("Include numbers? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if nums.lower() == "y":
            break
        elif nums.lower() == "n":
            numbers = ""
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.", Colors.blue_to_purple, interval = 0.025)
            nums = Write.Input("Include numbers? (y/n): ", Colors.blue_to_purple, interval = 0.025)

    special_char = Write.Input("Include special characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if special_char.lower() == "y":
            break
        elif special_char.lower() == "n":
            special_chars = ""
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.", Colors.blue_to_purple, interval = 0.025)
            special_char = Write.Input("Include special characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)

    password = random.choices(lower_chars + upper_chars + numbers + special_chars, k=length)
    password = "".join(password)
    Write.Print(f"Generated Password: {password}\n", Colors.blue_to_purple, interval = 0.025)
    save = Write.Input("Save password? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if save.lower() == "y":
            save_password(password)
            break
        elif save.lower() == "n":
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.", Colors.blue_to_purple, interval = 0.025)
    clear(main)

def save_password(password):
    filename = "passwords.txt"
    note = Write.Input("Enter your note (Leave blank for none): ", Colors.blue_to_purple, interval = 0.025).strip() or "None"

    try:
        with open(filename, "a") as f:
            f.write(f"Password: {password} | Note: {note}\n")
        Write.Print("Password and note saved successfully.\n", Colors.blue_to_purple, interval = 0.025)
        Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
        clear(main)
    except Exception as e:
        Write.Print(f"An error occurred while saving the password: {e}", Colors.blue_to_purple, interval = 0.025)

def manage_password_history():
    options1 = {
        1: "View passwords",
        2: "Edit password",
        3: "Delete password",
        4: "Edit note",
        5: "Delete note",
        6: "Delete all",
        7: "Back"
    }
    Write.Print("Manage Password History:", Colors.blue_to_purple, interval = 0.025)
    for key, value in options1.items():
        Write.Print(f"\n{key}. {value}", Colors.blue_to_purple, interval = 0.0025)

    choice1 = Write.Input("\nEnter your choice: ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if choice1 == "1":
            view_passwords()
            break
        elif choice1 == "2":
            edit_password()
            break
        elif choice1 == "3":
            delete_password()
            break
        elif choice1 == "4":
            edit_note()
            break
        elif choice1 == "5":
            delete_note()
            break
        elif choice1 == "6":
            delete_all()
            break
        elif choice1 == "7":
            clear(main)
            break
        else:
            Write.Print("Invalid choice. Please try again.", Colors.blue_to_purple, interval = 0.025)
            choice1 = Write.Input("\nEnter your choice: ", Colors.blue_to_purple, interval = 0.025)

def view_passwords():
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.", Colors.blue_to_purple, interval = 0.025)
    else:
        with open(filename, "r") as f:
            content = f.readlines()
            if not content:
                Write.Print("Password history is empty.", Colors.blue_to_purple, interval = 0.025)
            else:
                Write.Print("\nSaved Passwords:", Colors.blue_to_purple, interval = 0.025)
                for i, line in enumerate(content, start=1):
                    Write.Print(f"\n{i}. {line.strip()}", Colors.blue_to_purple, interval = 0.0025)
    Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
    clear(manage_password_history)

def edit_password():
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.", Colors.blue_to_purple, interval = 0.025)
        Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
        clear(manage_password_history)
        return

    try:
        index = int(Write.Input("Enter the number of the password you want to edit: ", Colors.blue_to_purple, interval = 0.025)) - 1
        with open(filename, "r") as f:
            lines = f.readlines()
        if 0 <= index < len(lines):
            new_password = Write.Input("Enter the new password: ", Colors.blue_to_purple, interval = 0.025)
            parts = lines[index].split("| Note:")
            lines[index] = f"Password: {new_password} | Note:{parts[1]}"
            with open(filename, "w") as f:
                f.writelines(lines)
            Write.Print("Password updated successfully.", Colors.blue_to_purple, interval = 0.025)
        else:
            Write.Print("Invalid number. Please try again.", Colors.blue_to_purple, interval = 0.025)
    except (ValueError, IndexError):
        Write.Print("Invalid input. Please try again.", Colors.blue_to_purple, interval = 0.025)
    Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
    clear(manage_password_history)

def delete_password():
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.", Colors.blue_to_purple, interval = 0.025)
        Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
        clear(manage_password_history)
        return

    try:
        index = int(Write.Input("Enter the number of the password you want to delete: ", Colors.blue_to_purple, interval = 0.025)) - 1
        with open(filename, "r") as f:
            lines = f.readlines()
        if 0 <= index < len(lines):
            del lines[index]
            with open(filename, "w") as f:
                f.writelines(lines)
            Write.Print("Password deleted successfully.", Colors.blue_to_purple, interval = 0.025)
        else:
            Write.Print("Invalid number. Please try again.", Colors.blue_to_purple, interval = 0.025)
    except (ValueError, IndexError):
        Write.Print("Invalid input. Please try again.", Colors.blue_to_purple, interval = 0.025)
    Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
    clear(manage_password_history)

def edit_note():
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.", Colors.blue_to_purple, interval = 0.025)
        Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
        clear(manage_password_history)
        return

    try:
        index = int(Write.Input("Enter the number of the note you want to edit: ", Colors.blue_to_purple, interval = 0.025)) - 1
        with open(filename, "r") as f:
            lines = f.readlines()
        if 0 <= index < len(lines):
            new_note = Write.Input("Enter the new note: ", Colors.blue_to_purple, interval = 0.025)
            parts = lines[index].split("| Note:")
            lines[index] = f"{parts[0]}| Note: {new_note}\n"
            with open(filename, "w") as f:
                f.writelines(lines)
            Write.Print("Note updated successfully.", Colors.blue_to_purple, interval = 0.025)
        else:
            Write.Print("Invalid number. Please try again.", Colors.blue_to_purple, interval = 0.025)
    except (ValueError, IndexError):
        Write.Print("Invalid input. Please try again.", Colors.blue_to_purple, interval = 0.025)
    Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
    clear(manage_password_history)

def delete_note():
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.", Colors.blue_to_purple, interval = 0.025)
        Write.Input("\nPress Enter to return to the menu.")
        clear(manage_password_history)
        return

    try:
        index = int(Write.Input("Enter the number of the note you want to delete: ", Colors.blue_to_purple, interval = 0.025)) - 1
        with open(filename, "r") as f:
            lines = f.readlines()
        if 0 <= index < len(lines):
            parts = lines[index].split("| Note:")
            lines[index] = f"{parts[0]}| Note: None\n"
            with open(filename, "w") as f:
                f.writelines(lines)
            Write.Print("Note deleted successfully.", Colors.blue_to_purple, interval = 0.025)
        else:
            Write.Print("Invalid number. Please try again.", Colors.blue_to_purple, interval = 0.025)
    except (ValueError, IndexError):
        Write.Print("Invalid input. Please try again.", Colors.blue_to_purple, interval = 0.025)
    Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
    clear(manage_password_history)

def delete_all():
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.", Colors.blue_to_purple, interval=0.025)
        Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval=0.025)
        clear(manage_password_history)
        return

    while True:
        confirm = Write.Input("Are you sure you want to delete all saved passwords? (y/n): ", Colors.blue_to_purple, interval=0.025).lower()
        if confirm == "y":
            with open(filename, "w") as f:
                pass
            Write.Print("All passwords deleted successfully.", Colors.blue_to_purple, interval=0.025)
            break
        elif confirm == "n":
            Write.Print("Operation canceled.", Colors.blue_to_purple, interval=0.025)
            break
        else:
            Write.Print("Invalid input. Try again.\n", Colors.blue_to_purple, interval=0.025)

    Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval=0.025)
    clear(manage_password_history)

def creditss():
    Write.Print("""
    Password Machine v1.0
    Developed by: StivoMix
    Discord: StivoMix
    GitHub: https://github.com/StivoMix
    """, Colors.blue_to_purple, interval = 0.025)
    Write.Input("\nPress Enter to return to the menu.", Colors.blue_to_purple, interval = 0.025)
    clear(main)

clear(main)