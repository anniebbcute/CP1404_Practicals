import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def generateNumbers():
    num_list = []
    for i in range(NUMBERS_PER_LINE):
        in_the_list = False
        num = random.randint(MINIMUM, MAXIMUM)
        for i in num_list:
            if i == num:
                in_the_list = True
        if in_the_list == False:
            num_list.append(num)
    num_list.sort()
    return num_list

picks = int(input("How many quick picks? : "))
for i in range(picks):
    mylist = generateNumbers()
    print(mylist)