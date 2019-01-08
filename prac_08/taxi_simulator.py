from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
 SilverServiceTaxi("Hummer", 200, 4)]


def menu():
    MENU = """q)uit, c)hoose taxi, d)rive"""
    print(MENU)
    choice = input(">>> ").lower()
    return choice


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))

def main():
    print("Let's drive!")
    option = menu()
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
    SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0
    while option != "q":
        if option == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
        elif option == "d":
            chosen_taxi.start_fare()
            get_drive_distance = float(input("Drive how far? "))
            chosen_taxi.drive(get_drive_distance)
            current_cost = chosen_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, current_cost))
            total_cost += current_cost
        else:
            print("Invalid input.")
        print("Bill to date: ${:.2f}".format(total_cost))
        option = menu()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


main()