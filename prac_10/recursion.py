"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return 0
    print(n ** 2)
    do_something(n - 1)


print (do_something(4))


def cal_blocks(n):
    if n < 0:
        return 0
    return n + cal_blocks(n-1)


def main():
    get_rows = int(input("How many rows are there? "))
    print("You need {} blocks for {} rows in a pyramid.".format(cal_blocks(get_rows),get_rows))


main()