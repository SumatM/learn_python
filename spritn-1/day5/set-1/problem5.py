# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

bag = ""
str = 'Python'

for x in reversed(str):
    bag+=x;

print(bag);