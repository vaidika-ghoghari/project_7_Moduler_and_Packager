import random
import string

def random_menu():
     while True:
        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice < 1 or choice > 5:
                print("Error: Choice must be between 1 and 5.")
                continue
            
        except ValueError:
            print("Error: Choice must be an integer between 1 and 5.")
            continue

        if choice == 1:
                
            print(f"\nRandom Number: {random.randint(1, 100)}")

        elif choice == 2:

            try:
                length = int(input("Enter the length of the list: "))
                start = int(input("Enter starting value: "))
                end = int(input("Enter ending value: "))

                

                if length <= 0:
                    print("List length must be positive.")
                    continue

                if start > end:
                    print("Starting value cannot exceed ending value.")
                    continue

                random_list = [
                    random.randint(start, end)
                    for _ in range(length)
                ]
                print("Random List:", random_list)

            except ValueError:
                print("Please enter valid integers.")

        elif choice == 3:
            try:
                length = int(input("\nEnter the desired password length: "))
                if length <= 0:
                    print("Password length must be positive.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer for password length.")
                continue
            characters = string.ascii_letters + string.digits 
            password = ''.join(random.choices(characters, k=length))
            print(f"\nGenerated Password: {password}")

        elif choice == 4:
            try:
                length = int(input("\nEnter the desired OTP length: "))
                if length <= 0:
                    print("OTP length must be positive.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid integer for OTP length.")
                continue

            otp = ''.join(random.choices(string.digits, k=length))
            print(f"\nGenerated OTP: {otp}")

        elif choice == 5:
            print("\nReturning to Main Menu...")
            break

        

if __name__ == "__main__":
    random_menu()