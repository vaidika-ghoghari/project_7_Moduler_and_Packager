import math


def math_menu():
    while True:
        print("\n--- Mathematical Operations ---")
        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
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
            try:
                number = int(input("Enter a non-negative integer: "))

                if number < 0:
                    raise ValueError("Number cannot be negative.")

                result = math.factorial(number)

            except ValueError as error:
                print("Error:", error)

            else:
                print("Factorial:", result)

            finally:
                print("Factorial operation completed.")

        elif choice == 2:
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                years = float(input("Enter time in years: "))

                if principal < 0 or rate < 0 or years < 0:
                    raise ValueError("Values cannot be negative.")

                amount = principal * (1 + rate / 100) ** years
                interest = amount - principal

            except ValueError as error:
                print("Error:", error)

            else:
                print("Final Amount:", round(amount, 2))
                print("Compound Interest:", round(interest, 2))

            finally:
                print("Compound interest operation completed.")

        elif choice == 3:
            try:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                sine = math.sin(radians)
                cosine = math.cos(radians)

            except ValueError as error:
                print("Error:", error)

            else:
                print("Sine:", round(sine, 4))
                print("Cosine:", round(cosine, 4))

                if abs(cosine) > 1e-10:
                    print("Tangent:", round(math.tan(radians), 4))
                else:
                    print("Tangent: Undefined")

            finally:
                print("Trigonometric operation completed.")

        elif choice == 4:
            try:
                print("1. Circle")
                print("2. Rectangle")
                print("3. Triangle")
                try:
                    shape = int(input("Choose a shape (1-3): "))

                    if shape < 1 or shape > 3:
                        raise ValueError("Shape choice must be between 1 and 3.")
                except ValueError:
                    print("Error: Shape choice must be an integer between 1 and 3.")
                    continue

                if shape == 1:
                    radius = float(input("Enter radius: "))

                    if radius < 0:
                        raise ValueError("Radius cannot be negative.")

                    area = math.pi * radius ** 2

                elif shape == 2:
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))

                    if length < 0 or width < 0:
                        raise ValueError("Dimensions cannot be negative.")

                    area = length * width

                elif shape == 3:
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))

                    if base < 0 or height < 0:
                        raise ValueError("Dimensions cannot be negative.")

                    area = 0.5 * base * height

                else:
                    raise ValueError("Invalid shape choice.")

            except ValueError as error:
                print("Error:", error)

            else:
                print("Area:", round(area, 2))

            finally:
                print("Area calculation completed.")

        elif choice == 5:
            print("Returning to Main Menu...")
            break

       

if __name__ == "__main__":
    math_menu()