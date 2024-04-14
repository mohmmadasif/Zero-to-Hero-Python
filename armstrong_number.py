#Write a program to check Armstrong Number?

#Armstrong number 
# - It is a number that is equal to the sum of its own digits, each raised to a power equal to the 
#number of digits in the number.

# For example, let's consider the number 153:
# ~It has three digits (1,5 and 3)
# ~If we calculate 1*3 + 5*3 + 3*3, we get 1 + 125 + 27, which is equal to 153.
# So,153 is an Armstrong number because it equals the sum of its digits raised to the power of the number of
# digits in the number.

#Another example is 9474:
# ~It has four digits (9,4,7 and 4)
# ~If we calculate 9*3 + 4*3 + 7*3 + 4*3, which is equal to 9474.
# So,9474 is an Armstrong number because it equals the sum of its digits raised to the power of the number of 
# digits in the number.


num = int(input("Enter the number you want to check if it is Armstrong number or not: "))

#Calculate the number of digits in the number.

num_str =  str(num)
num_digits = len(num_str)

#Initialize variables

sum_of_powers = 0
temp_num = num

#Calculate the sum of digits raised to the power of num_digits.

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num = temp_num // 10
    
#Check whether it is Armstrong or not.
if sum_of_powers == num:
    print(num, "is an Armstrong number.")
    
else:
    print(num, "is not an Armstrong number.")