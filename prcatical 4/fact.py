num = int(input("enter the number:"))

factorial = 1

if num < 0:
 print ("factorial is not defined for negative numbers.")  
elif num == 0 or num == 1:
 print ("factorial =", 1)
else:
    for i in range (2, num + 1):
        factorial *= i
        print ("factorial =",factorial)