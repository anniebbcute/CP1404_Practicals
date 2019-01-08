item_num = -1
while (item_num <0):
    item_num = int(input("Please enter the number of items.\n"))
    item_price = [float(input("Enter the price of the item \n")) for i in range(item_num)]
    total = sum(item_price)
    if item_num >=0:
        if total >100:
            discountprice = total * 0.9
            print("Final Price is ${:.2f}".format(discountprice))
        else:
            print("Final Price is ${:.2f}".format(total))
    else:
        print ("Invalid number.")




