def factorial(n):
    if n <2:
        return 1
    else:
        return n*factorial(n-1)
input("enter a number:")
print("factorial of 5 is :",factorial(5))