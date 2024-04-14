#Write a program to print the sum of all the natural numbers.

limit = int(input("Enter the limit: "))

#Initialize the sum
sum = 0

for num in range(1, limit+1):
     sum += num
     
#Sum
print(f"The sum of all the natural numbers between 1 and {limit} is {sum}.")