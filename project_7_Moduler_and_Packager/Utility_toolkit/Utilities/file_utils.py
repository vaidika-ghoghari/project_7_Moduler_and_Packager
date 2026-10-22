import os


def file_menu():
    while True:
        print("\n--- File Operations ---")
        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")
            continue

        if choice < 1 or choice > 5:
            print("\nInvalid choice. Please select a number between 1 and 5.")
            continue

        if choice == 1:

            filename = input("\nEnter file name: ")
            try:
                file = open(filename, "x")
                file.close()
                print("File created successfully!")
            except FileExistsError:
                print("\nFile already exists.")
            except OSError as error:
                print("\nFile error:", error)

        elif choice == 2:

            filename = input("\nEnter file name: ")
            data = input("Enter data to write: ")

            if not os.path.exists(filename):
                print("\nFile does not exist. Please create the file first.")
                continue

            try:
                file = open(filename, "w")
                file.write(data + "\n")
                file.close()
                print("\nData written successfully!")
            except OSError as error:
                print("\nFile error:", error)
            

            

        elif choice == 3:
            filename = input("Enter file name: ")

            if not os.path.exists(filename):
                print("File does not exist. Please create the file first.")
                continue
            try:
                file = open(filename, "r")
                content = file.read()
                file.close()

                print("File Content:")
                print(content)

            except FileNotFoundError:
                print("Error: File not found. Please enter a valid file name.")

            except PermissionError:
                print("Error: Permission denied. You cannot read this file.")

            except OSError as error:
                print("File error:", error)

        elif choice == 4:
            filename = input("\nEnter file name: ")
            data = input("Enter data to append: ")

            if not os.path.exists(filename):
                print("\nFile does not exist. Please create the file first.")
                continue 
               
            try:
                file = open(filename, "a")
                file.write(data + "\n")
                file.close()
                print("\nData appended successfully!")
            except OSError as error:
                print("\nFile error:", error)
            
        elif choice == 5:
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    file_menu()