# Write a program to perfom quadradtic equation
# the standard form of a quadratic eqaution is (ax2 +  bx + c = 0)
#      where 
#        a,b and c are real numbers and a/= 0
#            the solutions of this quadratic equation is given by
#              (-b+-(b2 - 4ac)1/2)/(2a)




import math

#input coefficients
a = float(input("Enter value of a "))
b = float(input("Enter value of b "))
c = float(input("Enter value of c "))

#calculate the discriminant
discriminant = b**2 - 4*a*c

#check if the discriminant is positive, negative or zero
if discriminant > 0:
    #two real and distinct roots
    root1 = ( -b + math.sqrt(discriminant))/(2*a)
    root2 = ( -b - math.sqrt(discriminant))/(2*a)
    print(f"Root1:{root1}")
    print(f"Root2:{root2}")
elif discriminant == 0:

        #one real root (repeated)    
    root = -b/(2*a)
    print(f"Root:{root}")
else :
    #complex roots
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(abs(discriminant))/(2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")