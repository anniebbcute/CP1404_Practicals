from prac_07.guitar import Guitar


def main():
    my_guitars = []

    print("My guitars!")
    get_name = input("Name: ")
    while get_name != "":
        get_year = int(input("Year: "))
        get_cost = float(input("Cost: $"))
        add_guitars = Guitar(get_name, get_year, get_cost)
        my_guitars.append(add_guitars)
        print(add_guitars, "added.")
        get_name = input("Name: ")

    my_guitars.sort()

    if my_guitars is not None:
        print("These are my guitars:")
        for i, guitar in enumerate(my_guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
             {2}".format(i + 1, guitar, vintage_string))
    else:
        print("There are no guitars.")


main()