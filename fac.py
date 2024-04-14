#Write a program to find factorial of the number.

num = int(input("Enter your prefered number: "))
factorial = 1
if num <0:
    print("Factorial of the number does not exist for negative number.")
elif num  == 0:
    print("Factorial of the number does not exist for 0 and 1.")
else :
    for i in range(1, num+1):
        factorial = factorial*i
    print(f'The factorial of {num} is {factorial}')