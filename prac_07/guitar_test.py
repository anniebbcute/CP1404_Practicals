from prac_07.guitar import Guitar

def main():
    one_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

    print(one_guitar)

    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    second_name = "Another Guitar"
    second_year = 2012

    first_guitar = Guitar(name, year, cost)
    second_guitar = Guitar(second_name, second_year)

    print("{} get_age() - Expected {}. Got {}".format(first_guitar.name, 96,
                                                      first_guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(second_guitar.name, 6,
                                                      second_guitar.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(first_guitar.name, True, first_guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(second_guitar.name, False, second_guitar.is_vintage()))

main()