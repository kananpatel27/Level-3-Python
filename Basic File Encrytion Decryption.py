from cryptography.fernet import Fernet

def generate_key():               #Generate key and save it
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("✅ Encryption key generated and saved as secret.key")


def load_key():     #Load existing key
    return open("secret.key", "rb").read()


def encrypt_file(filename, key):  #Encrypt file
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:   # Read original file data
            original_data = file.read()

        encrypted_data = fernet.encrypt(original_data)   #Encrypt data 

        encrypted_file = "encrypted_" + filename  #save encrypted data

        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)

        print(f"File encrypted successfully: {encrypted_file}")

    except FileNotFoundError:
        print("File not found.")



def decrypt_file(filename, key):  #Decrypt file 
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:  #Read encrypted file data
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)  #Decrypt data

        decrypted_file = "decrypted_" + filename  #save decrypted data

        with open(decrypted_file, "wb") as file:
            file.write(decrypted_data)

        print(f"File decrypted successfully: {decrypted_file}")

    except FileNotFoundError:
        print("File not found.")

    except Exception:
        print("Invalid key or corrupted encrypted file.")


# Main Program
print("====== FILE ENCRYPTION & DECRYPTION ======")    

generate_key()   #Generate key only once 

key = load_key()  #Load key

while True:

    print("\n1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Encrypt option
    if choice == "1":
        filename = input("Enter file name to encrypt: ")
        encrypt_file(filename, key)

    # Decrypt option
    elif choice == "2":
        filename = input("Enter file name to decrypt: ")
        decrypt_file(filename, key)

    # Exit
    elif choice == "3":
        print("Program Exited")
        break

    else:
        print("Invalid choice. Please try again.")