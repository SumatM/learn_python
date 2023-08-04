# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

sum = 0
count = 0
list = [10,20,30,40]

for x in list:
    sum+=x;
    count+=1;

print(sum)

print(sum/count)

