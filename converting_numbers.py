#Write a program to convert numbers in binary,hexa-decimal,octal.

dec_num = int(input('Enter the number to convert: '))

print("The decimal value of", dec_num,"is")
print(bin(dec_num), "in Binary. ")
print(oct(dec_num), "in Octal. ")
print(hex(dec_num), "in Hexadecimal. ")