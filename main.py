import random 
import os
import logo
from pystyle import Colors, Write
from cryptography.fernet import Fernet

try:
    if not os.path.exists("key.key"):
        Write.Print("Encryption key not found. Generating a new key...\n", Colors.blue_to_purple, interval=0.025)
        with open("key.key", "wb") as key_file:
            key = Fernet.generate_key()
            key_file.write(key)
            Write.Print("Encryption key successfully generated and saved as 'key.key'.\n", Colors.green, interval=0.025)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    cipher_suite = Fernet(key)
except Exception as e:
    Write.Print(f"An error occurred during key handling: {str(e)}\n", Colors.red, interval=0.025)
    Write.Input("Press Enter to exit...", Colors.red, interval=0.025)
    exit()

def clear(next_function=None, *args):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(logo.logo(), "\n")
    if next_function:
        next_function(*args)  

def main():
    options = {1: "Generate Password", 2: "Manage Password History", 3: "Credits and Update logs", 4: "Change Encryption key"}
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
        elif choice == "4":
            clear(rek)
        else:
            Write.Print("Invalid choice. Please try again.\n", Colors.blue_to_purple, interval = 0.025)
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
                Write.Print("Invalid length. Password length should be between 3 and 50 characters.\n", Colors.blue_to_purple, interval = 0.025)
        except ValueError:
            Write.Print("Invalid input. Please enter a valid integer.\n", Colors.blue_to_purple, interval = 0.025)

    lowerchars = Write.Input("Include lower case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if lowerchars.lower() == "y":
            break
        elif lowerchars.lower() == "n":
            lower_chars = ""
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.\n", Colors.blue_to_purple, interval = 0.025)
            lowerchars = Write.Input("Include lower case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)

    upperchars = Write.Input("Include upper case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if upperchars.lower() == "y":
            break
        elif upperchars.lower() == "n":
            upper_chars = ""
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.\n", Colors.blue_to_purple, interval = 0.025)
            upperchars = Write.Input("Include upper case characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)

    nums = Write.Input("Include numbers? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if nums.lower() == "y":
            break
        elif nums.lower() == "n":
            numbers = ""
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.\n", Colors.blue_to_purple, interval = 0.025)
            nums = Write.Input("Include numbers? (y/n): ", Colors.blue_to_purple, interval = 0.025)

    special_char = Write.Input("Include special characters? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    while True:
        if special_char.lower() == "y":
            break
        elif special_char.lower() == "n":
            special_chars = ""
            break
        else:
            Write.Print("Invalid input. Please enter 'y' or 'n'.\n", Colors.blue_to_purple, interval = 0.025)
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
            Write.Print("Invalid input. Please enter 'y' or 'n'.\n", Colors.blue_to_purple, interval = 0.025)
            save = Write.Input("Save password? (y/n): ", Colors.blue_to_purple, interval = 0.025)
    clear(main)

def save_password(password):
    filename = "passwords.txt"
    note = Write.Input("Enter your note (Leave blank for none): ", Colors.blue_to_purple, interval=0.025).strip() or "None"

    try:
        encrypted_password = cipher_suite.encrypt(password.encode()).decode()
        with open(filename, "a") as f:
            f.write(f"Password: {encrypted_password} | Note: {note}\n")
        Write.Print("Password and note saved successfully.\n", Colors.blue_to_purple, interval=0.025)
        Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
        clear(main)
    except Exception as e:
        Write.Print(f"An error occurred while saving the password: {e}\n", Colors.blue_to_purple, interval=0.025)

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
            check_file(edit_password)
            break
        elif choice1 == "3":
            check_file(delete_password)
            break
        elif choice1 == "4":
            check_file(edit_note)
            break
        elif choice1 == "5":
            check_file(delete_note)
            break
        elif choice1 == "6":
            check_file(delete_all)
            break
        elif choice1 == "7":
            clear(main)
            break
        else:
            Write.Print("Invalid choice. Please try again.\n", Colors.blue_to_purple, interval = 0.025)
            choice1 = Write.Input("Enter your choice: ", Colors.blue_to_purple, interval = 0.025)

def view_passwords():
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.\n", Colors.blue_to_purple, interval=0.025)
    else:
        with open(filename, "r") as f:
            content = f.readlines()
            if not content:
                Write.Print("Password history is empty.\n", Colors.blue_to_purple, interval=0.025)
            else:
                Write.Print("\nSaved Passwords:", Colors.blue_to_purple, interval=0.025)
                for i, line in enumerate(content, start=1):
                    try:
                        encrypted_password = line.split(" | ")[0].split(": ")[1]
                        decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
                        note = line.split(" | ")[1]
                        Write.Print(f"\n{i}. Password: {decrypted_password} | {note.strip()}", Colors.blue_to_purple, interval=0.0025)
                    except Exception as e:
                        Write.Print(f"\n{i}. Error decrypting password: {e}", Colors.red, interval=0.0025)
    Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
    clear(manage_password_history)

def edit_password(filename="passwords.txt"):
    while True:
        try:
            index = int(Write.Input("Enter the number of the password you want to edit: ", Colors.blue_to_purple, interval=0.025)) - 1
            with open(filename, "r") as f:
                lines = f.readlines()
            if 0 <= index < len(lines):
                line_parts = lines[index].strip().split(" | ")
                encrypted_password = line_parts[0].split(": ")[1]
                note = line_parts[1].replace("Note: ", "") if len(line_parts) > 1 else "None"

                decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
                Write.Print(f"Current password #{index + 1}: {decrypted_password}\n", Colors.blue_to_purple, interval=0.025)

                new_password = Write.Input("Enter the new password: ", Colors.blue_to_purple, interval=0.025)
                while True:
                    confirm = Write.Input(f"Are you sure you want to replace password #{index + 1} with '{new_password}'? (y/n): ", Colors.blue_to_purple, interval=0.025)
                    if confirm.lower() == "y":
                        encrypted_new_password = cipher_suite.encrypt(new_password.encode()).decode()
                        lines[index] = f"Password: {encrypted_new_password} | Note: {note}\n"
                        with open(filename, "w") as f:
                            f.writelines(lines)
                        Write.Print("Password updated successfully.\n", Colors.blue_to_purple, interval=0.025)
                        break
                    elif confirm.lower() == "n":
                        Write.Print("Operation canceled.\n", Colors.blue_to_purple, interval=0.025)
                        break
                    else:
                        Write.Print("Invalid choice. Please try again.\n", Colors.blue_to_purple, interval=0.025)
                break
            else:
                Write.Print("Invalid number. Please enter a valid index.\n", Colors.blue_to_purple, interval=0.025)
        except ValueError:
            Write.Print("Invalid input. Please enter a valid number.\n", Colors.blue_to_purple, interval=0.025)

    Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
    clear(manage_password_history)

def delete_password(filename="passwords.txt"):
    while True: 
        try:
            index = int(Write.Input("Enter the number of the password you want to delete: ", Colors.blue_to_purple, interval=0.025)) - 1
            with open(filename, "r") as f:
                lines = f.readlines()
            if 0 <= index < len(lines):
                line_parts = lines[index].strip().split(" | ")
                encrypted_password = line_parts[0].split(": ")[1]

                decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
                Write.Print(f"Current password #{index + 1}: {decrypted_password}\n", Colors.blue_to_purple, interval=0.025)
                
                while True:
                    confirm = Write.Input(f"Are you sure you want to delete password #{index + 1}? (y/n): ", Colors.blue_to_purple, interval=0.025)
                    if confirm.lower() == "y":
                        del lines[index]
                        with open(filename, "w") as f:
                            f.writelines(lines)
                        Write.Print("Password deleted successfully.", Colors.blue_to_purple, interval=0.025)
                        break
                    elif confirm.lower() == "n":
                        Write.Print("Operation canceled.", Colors.blue_to_purple, interval=0.025)
                        break 
                    else:
                        Write.Print("Invalid choice. Please try again.\n", Colors.blue_to_purple, interval=0.025)
                break  
            else:
                Write.Print("Invalid number. Please enter a valid index.\n", Colors.blue_to_purple, interval=0.025)
        except ValueError:
            Write.Print("Invalid input. Please enter a valid number.\n", Colors.blue_to_purple, interval=0.025)

    Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
    clear(manage_password_history)

def edit_note(filename="passwords.txt"):
    while True:
        try:
            index = int(Write.Input("Enter the number of the note you want to edit: ", Colors.blue_to_purple, interval=0.025)) - 1
            with open(filename, "r") as f:
                lines = f.readlines()
            if 0 <= index < len(lines):
                line_parts = lines[index].strip().split(" | ")
                note = line_parts[1].split(": ")[1]
                password = line_parts[0].split(": ")[1]

                Write.Print(f"Current note #{index + 1}: {note}\n", Colors.blue_to_purple, interval=0.025)

                new_note = Write.Input("Enter the new note: ", Colors.blue_to_purple, interval=0.025)
                while True:
                    confirm = Write.Input(f"Are you sure you want to replace note #{index + 1} with '{new_note}'? (y/n): ", Colors.blue_to_purple, interval=0.025)
                    if confirm.lower() == "y":
                        lines[index] = (f"Password: {password} | Note: {new_note}\n")
                        with open(filename, "w") as f:
                            f.writelines(lines)
                        Write.Print("Note updated successfully.\n", Colors.blue_to_purple, interval=0.025)
                        break
                    elif confirm.lower() == "n":
                        Write.Print("Operation canceled.\n", Colors.blue_to_purple, interval=0.025)
                        break
                    else:
                        Write.Print("Invalid choice. Please try again.\n", Colors.blue_to_purple, interval=0.025)
                break
            else:
                Write.Print("Invalid number. Please enter a valid index.\n", Colors.blue_to_purple, interval=0.025)
        except ValueError:
            Write.Print("Invalid input. Please enter a valid number.\n", Colors.blue_to_purple, interval=0.025)

    Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
    clear(manage_password_history)

def delete_note(filename="passwords.txt"):
    while True:
        try:
            index = int(Write.Input("Enter the number of the note you want to delete: ", Colors.blue_to_purple, interval=0.025)) - 1
            with open(filename, "r") as f:
                lines = f.readlines()
            if 0 <= index < len(lines):
                line_parts = lines[index].strip().split(" | ")
                note = line_parts[1].split(": ")[1]
                password = line_parts[0].split(": ")[1]

                if note == "None":
                    Write.Print("No note to delete.", Colors.blue_to_purple, interval=0.025)
                    break

                Write.Print(f"Current note #{index + 1}: {note}\n", Colors.blue_to_purple, interval=0.025)
                
                while True:
                    confirm = Write.Input(f"Are you sure you want to delete note #{index + 1}? (y/n): ", Colors.blue_to_purple, interval=0.025)
                    if confirm.lower() == "y":
                        lines[index] = (f"Password: {password} | Note: None\n")
                        with open(filename, "w") as f:
                            f.writelines(lines)
                        Write.Print("Note deleted successfully.", Colors.blue_to_purple, interval=0.025)
                        break
                    elif confirm.lower() == "n":
                        Write.Print("Operation canceled.", Colors.blue_to_purple, interval=0.025)
                        break
                    else:
                        Write.Print("Invalid choice. Please try again.\n", Colors.blue_to_purple, interval=0.025)
                break
            else:
                Write.Print("Invalid number. Please enter a valid index.\n", Colors.blue_to_purple, interval=0.025)
        except ValueError:
            Write.Print("Invalid input. Please enter a valid number.\n", Colors.blue_to_purple, interval=0.025)

    Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
    clear(manage_password_history)

def delete_all(filename = "passwords.txt"):
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

    Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
    clear(manage_password_history)

def creditss():
    Write.Print("""
    Password Machine v1.1
    Developed by: StivoMix
    Discord: StivoMix
    GitHub: https://github.com/StivoMix

    Update Logs:
    1.0 - Release
    1.1 - Added password encryption
    """, Colors.blue_to_purple, interval = 0.025)
    Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval = 0.025)
    clear(main)

def check_file(next_function=None, *args):
    filename = "passwords.txt"
    if not os.path.exists(filename):
        Write.Print("No passwords saved yet.", Colors.blue_to_purple, interval = 0.025)
        Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval = 0.025)
        clear(manage_password_history)
        return
    if next_function:
        next_function(*args)  

def rek():
    if not os.path.exists("key.key"):
        Write.Print("Encryption key not found. Generating a new key...\n", Colors.blue_to_purple, interval=0.025)
        with open("key.key", "wb") as kf:
            key = Fernet.generate_key()
            kf.write(key)
            Write.Print("Encryption key successfully generated and saved as 'key.key'.\n", Colors.green, interval=0.025)
            Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
            clear(main)
    else:
        try:
            with open("key.key", "rb") as kf:
                old_key = kf.read()
            old_cipher = Fernet(old_key)

            with open("passwords.txt", "r") as pf:
                lines = pf.readlines()
            
            decrypted_passwords = []
            for line in lines:
                line_parts = line.strip().split(" | ")
                if len(line_parts) < 2:
                    Write.Print("Invalid password format detected. Skipping line.\n", Colors.red, interval=0.025)
                    continue
                
                note = line_parts[1].split(": ")[1]
                encrypted_password = line_parts[0].split(": ")[1] 
                
                try:
                    decrypted_password = old_cipher.decrypt(encrypted_password.encode()).decode()
                    decrypted_passwords.append((decrypted_password, note)) 
                except Exception as e:
                    Write.Print(f"Error decrypting password: {str(e)}\n", Colors.red, interval=0.025)

            new_key = Fernet.generate_key()
            with open("key.key", "wb") as kf:
                kf.write(new_key)
            new_cipher = Fernet(new_key)
            global cipher_suite
            cipher_suite = new_cipher

            with open("passwords.txt", "w") as pf:
                for password, note in decrypted_passwords:
                    new_encrypted_password = new_cipher.encrypt(password.encode()).decode()
                    pf.write(f"Password: {new_encrypted_password} | Note: {note}\n")

            Write.Print("Encryption key regenerated and passwords re-encrypted successfully.\n", Colors.green, interval=0.025)
        
        except Exception as e:
            Write.Print(f"An error occurred while regenerating the key: {str(e)}\n", Colors.red, interval=0.025)
        
        Write.Input("\nPress enter to return.", Colors.blue_to_purple, interval=0.025)
        clear(main)

clear(main)
