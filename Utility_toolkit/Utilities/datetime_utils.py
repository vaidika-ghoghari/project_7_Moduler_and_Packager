import datetime
import time

def datetime_menu():
    """
    Displays a menu for datetime utilities.
    """
    while True:
        print("\n--- Datetime & Time Operations Menu ---")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Two Dates")
        print("3. Format Date into Custom Format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Return to Main Menu")


        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice < 1 or choice > 6:
                print("Error: Choice must be between 1 and 6.")
                continue
        except ValueError:
            print("Error: Choice must be an integer between 1 and 6.")
            continue

        if choice == 1:
        
            current = datetime.datetime.now()
            print("Current Date and Time:",current.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == 2:
            try:
                date1 = input("Enter first date (YYYY-MM-DD): ")
                date2 = input("Enter second date (YYYY-MM-DD): ")

                d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

                difference = abs((d2 - d1).days)
                print(f"Difference between {date1} and {date2} is {difference} days.")
            except ValueError:
                print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

        elif choice == 3:
            date = datetime.datetime.now()
            print("Custom Date:",date.strftime("%d-%B-%Y %I:%M %p"))

        elif choice == 4:
            try:
                input("Press Enter to start the stopwatch...")
                start_time = time.time()
                input("Press Enter to stop the stopwatch...")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Elapsed Time: {elapsed_time:.2f} seconds")
            except KeyboardInterrupt:
                print("\nStopwatch interrupted. Please only press Enter to start and stop the stopwatch.")

        elif choice == 5:
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                if seconds > 0:
                    print("Countdown Timer Started...")
                    while seconds:
                        print("Time remaining:", seconds, "seconds")
                        time.sleep(1)
                        seconds -= 1
                    print("Countdown completed!")
                else:
                    print("Please enter a positive integer for countdown.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for countdown.")
            
        elif choice == 6:
            print("Returning to Main Menu...")
            break
        
        
if __name__ == "__main__":
    datetime_menu()
