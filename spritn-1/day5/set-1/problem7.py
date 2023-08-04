# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."


count = 0
num = 3;

for i in range(1,num+1):
    if num%i==0:
        count+=1;

if count == 2:
    print(num,"is a Prime number")
else:
    print(num, "is not a Prime number")