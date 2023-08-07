# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."


def getDivision(num1,num2):
    try:
       return num1/num2;
    except:
        return "It is not possible to divide with zero"


print(getDivision(1,0))
