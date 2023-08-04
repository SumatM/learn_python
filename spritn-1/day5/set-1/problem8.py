# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."


num = 5;
factor = 1;


for i in range(1,num+1):
    factor = i*factor;
    print(factor);

print(factor);
