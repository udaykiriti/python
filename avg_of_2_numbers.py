def calculate_average(num1, num2):
    average = (num1 + num2) / 2
    return average
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
average_result = calculate_average(number1, number2)
print(f"The average of {number1} and {number2} is: {average_result}")