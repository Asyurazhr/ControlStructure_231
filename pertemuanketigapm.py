def evaluate_performance(percentage):
    if percentage >= 90:
        print("Excellent")
    elif percentage >= 80:
        print ("Very Good")
    elif percentage >= 70:
        print ("Good performance")
    elif percentage >= 60:
        print ("Average performance")
    else:
        print ("Needs improvement")

percentage = float(input("Enter the student's percentage: "))

performance = evaluate_performance(percentage)
print(f"Student's performance: {performance}")


#nomor 2
def largest_of_three (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Input: Three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Output: The largest number
largest = largest_of_three(num1, num2, num3)
print(f"The largest number is: {largest}")

#nomor 3
import math
def fibonacci_series(limit):
    fib_series = []
    a, b = 0, 1
    while a <= limit:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def factorial(n):
    return math.factorial(n)

n = int(input("Enter a number n to generate Fibonacci series up to n!: "))

n_factorial = factorial(n)
print(f"Factorial of {n} (n!) is: {n_factorial}")

fib_series = fibonacci_series(n_factorial)
print("Fibonacci series up to n! is:")
print(fib_series)

#nomor 4
import math

def factorial(n):
    return math.factorial(n)

def print_odd_numbers(limit):
    odd_numbers = []
    for num in range(1, limit + 1):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

n = int(input("Enter a number n to print odd numbers up to n!: "))

n_factorial = factorial(n)
print(f"Factorial of {n} (n!) is: {n_factorial}")

odd_numbers = print_odd_numbers(n_factorial)
print("Odd numbers up to n! are:")
print(odd_numbers)

#nomer 5
def print_pattern(n):
    for i in range(1, n+1):
        print(" ".join([str(i)] * i))

n = int(input("Enter a number n to generate the pattern: "))

print_pattern(n)