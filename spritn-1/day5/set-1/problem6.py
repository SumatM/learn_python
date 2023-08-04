# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

count = 0
vow = 'aeiouAEIOU'

str = "Hello"

for ele in str:
    if ele in vow:
        count+=1;

print(count);
