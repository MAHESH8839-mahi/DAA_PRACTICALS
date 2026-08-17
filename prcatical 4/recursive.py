def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("enter the number:"))

if num < 0:
    print ("factorial is not defined for negative number.")
else:
    print ("Factorial =",factorial(num))