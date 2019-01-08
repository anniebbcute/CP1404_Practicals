out_file = open('name.txt', 'w')
name = str(input("Please enter your name: \n"))
print("Your name is " + name, file=out_file)
out_file.close()

file = open('name.txt', 'r')
file.read
print(file.read())


file = open('numbers.txt', 'r')
first_num = int(file.readline())
second_num = int(file.readline())
print(first_num + second_num)
file.close()

file = open("numbers.txt", "r")
total = 0
for line in file:
 number = int(line)
 total += number
print(total)
file.close()