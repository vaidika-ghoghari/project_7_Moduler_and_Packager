
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
        print("3. Explore random")
        print("4. Explore uuid")
        print("5. Explore file_utils")
        print("6. Back to Main Menu")

        try:
            ch = int(input("Enter your choice (1-6): "))

            if ch < 1 or ch > 6:
                print("Error: Choice must be between 1 and 6.")
                continue

        except ValueError:
            print("Error: Choice must be an integer between 1 and 6.")
            continue

        if ch == 1:
            import Utilities.math_utils
            print(dir(Utilities.math_utils))

        elif ch == 2:
            import Utilities.datetime_utils
            print(dir(Utilities.datetime_utils))

        elif ch == 3:
            import Utilities.random_utils
            print(dir(Utilities.random_utils))

        elif ch == 4:
            import Utilities.uuid_utils
            print(dir(Utilities.uuid_utils))

        elif ch == 5:
            import Utilities.file_utils
            print(dir(Utilities.file_utils))

        elif ch == 6:
            print("Returning to the Main Menu...")
            break


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

        try:
            choice = int(input("Enter your choice (1-7): "))

            if choice < 1 or choice > 7:
                print("Error: Choice must be between 1 and 7.")
                continue

        except ValueError:
            print("Error: Choice must be an integer between 1 and 7.")
            continue

        if choice == 1:
            datetime_menu()

        elif choice == 2:
            math_menu()

        elif choice == 3:
            random_menu()

        elif choice == 4:
            uuid_menu()

        elif choice == 5:
            file_menu()

        elif choice == 6:
            explore_modules()

        elif choice == 7:
            print("\nThank you for using the Multi-Utility Toolkit!")
            break


if __name__ == "__main__":
    main()
