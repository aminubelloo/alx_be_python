# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def display_menu():
    print("\nTemperature conversion tool \nConvert:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit.\n3. Quit. ")

def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celcius):
    return (celcius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice:").strip()
        try:
            choice = int(choice)
        except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        if choice == 1:
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
            except ValueError:
                print("Invalid temperature value.")
        

            
        elif choice == 2:
            try:
                c = float(input("Enter temperature in Celcius:"))
                print(f"{c} °C is {convert_to_fahrenheit(c)}°F")
            except ValueError:
                print("Invalid temperature value.")
        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice , please try again.")
            
if __name__ == "__main__":
    main()
