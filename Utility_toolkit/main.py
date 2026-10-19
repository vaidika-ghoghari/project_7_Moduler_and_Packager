
import math
import datetime
import time
import random
import uuid

from Utilities import (
    datetime_menu,
    math_menu,
    random_menu,
    uuid_menu,
    file_menu
)


def explore_modules():
    while True:
        print("\n--- Explore Module Attributes ---")
        print("1. Explore math")
        print("2. Explore datetime")
        print("3. Explore time")
        print("4. Explore random")
        print("5. Explore uuid")
        print("6. Explore custom module")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(dir(math))

        elif choice == "2":
            print(dir(datetime))

        elif choice == "3":
            print(dir(time))

        elif choice == "4":
            print(dir(random))

        elif choice == "5":
            print(dir(uuid))

        elif choice == "6":
            import Utilities.math_utils
            print(dir(Utilities.math_utils))

        elif choice == "7":
            break

        else:
            print("Invalid choice. Try again.")


def main():
    while True:
        print("\n" + "=" * 35)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 35)

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        print("=" * 35)

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_modules()

        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()