#Write a program to print the multiplication table.


num = int(input("Display the multiplication of :"))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")