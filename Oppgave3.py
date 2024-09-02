
#Gather user input
num1 = input("Enter a number: ")
num2 =  input("Enter another number: ")

#Convert user input from strings to integers
num1 = int(num1)
num2 = int(num2)

#Using f-string method to print strings and values together despite mixed variables
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Modulo: {num1 % num2}")
print(f"Exponential: {num1 ** num2}")
print(f"Divide by rounding down: {num1 // num2}")