num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print("Addition : " , sum_result)

# Subtraction
sub_result = num1 - num2
print("Subtraction : ", sub_result)

# Multiplication
mul_result = num1 * num2
print("Multiplication : " , mul_result )

# Division
if num2 != 0:
    div_result = num1 / num2 
    print("Division : " , div_result ) 
else:
    print("Division by zero is not allowed")

# Modulus (remainder)
if num2 != 0 :
    mod_result = num1 % num2
    print("Modulus : " , mod_result)
else:
    print("Cannot calculate the zero. ")
