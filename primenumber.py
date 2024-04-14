#Write a program to check whether a numnber is prime or not.add()


num =  int(input("Enter your number you want to check: "))

#define a flag variable
flag = False

if num == 1:
    print(f"{num}, is a not prime number")
elif num > 1:
    #check for the factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True    #if factor is found, set flag to true
            
            #break out of loop
            break 
        
            #check if flag true
if flag == True:
            print(f"{num}, is a not prime number. ")
else:
            print(f"{num}, is a prime number. ")