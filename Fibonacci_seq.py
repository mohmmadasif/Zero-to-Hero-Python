#Write a program to print the Fibonacci sequence.

#Fibonacci sequence:
#The Fibonacci sequence is a series of numbers where each number is the sum of the 
#two preceding ones.Typically starting with 0 and 1.So,the seqeunce begins with 0 and 1,and 
#the next number is obtained by adding the previous two numbers. This pattern continues
#indefinitely,generating a sequence that looks like this:

#0,1,1,2,3,5,8,13,21,34,55,89,144, and so on.

#Mathematically,the Fibonacci sequence can be defined as using the following recurrence 
#relation


#F(0) = 0F(1) = 1F(n) = F(n-1) + F(n-2) for n>1


nterms = int(input("How many terms? "))

#first two terms
n1,n2 = 0,1
count = 0

#check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive number: ")
    
    #if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
    
    #generate fibonacci sequence
else:
    print("Fibonacci sequence :")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1 
        
