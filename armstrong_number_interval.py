#Write a program to check whether a number is Armstrong in the interval.
# Input the interval from the user
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

for num in range(lower, upper+1):       #Iterate through the numbers in the interval.
    order = len(str(num))               #Find the number of digtis in 'num'
    temp_num = num
    sum = 0
    while temp_num > 0:
      digit = temp_num % 10
      sum += digit ** order
      temp_num //= 10
            
 # Checking
    if num == sum:
        print(num)
    else:
         0