from prac_08.unreliable_car import UnreliableCar


def main():

    first_car = UnreliableCar("Bunny", 100, 82)
    second_car = UnreliableCar("Breadsticks", 100, 7)
    third_car = UnreliableCar("PURIN", 100, 56)

    for i in range(1, 10):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(first_car.name, first_car.drive(i)))
        print("{:12} drove {:2}km".format(second_car.name, second_car.drive(i)))
        print("{:12} drove {:2}km".format(third_car.name, third_car.drive(i)))

    print(first_car)
    print(second_car)
    print (third_car)


main()