"""
CP1404 - Practical 09
Menu programming using the Taxi and Silver Service taxi classes.
"""
from operator import index

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator with menu pattern."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.0
    current_taxi = ""
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            display_taxis(taxis)
            current_taxi = get_taxi(taxis)
        elif choice == 'd':
            if current_taxi == "":
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print("Finished")


def display_taxis(taxis: list) -> None:
    """Display taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def get_taxi(taxis: list):
    """Get taxi number from user to assign taxi."""
    taxi_choice = int(input("Choose taxi: "))
    if 0 <= taxi_choice < len(taxis):
        return taxis[taxi_choice]
    else:
        print("Invalid taxi choice")
        return ""

def drive_taxi(current_taxi, bill_to_date):
    """Drive taxi given distance with fare."""
    current_taxi.start_fare()
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    fare = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost ${fare:.2f}")
    bill_to_date += fare
    return bill_to_date


if __name__ == '__main__':
    main()
