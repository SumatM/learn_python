# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"



num = 10;

new_List = [];


for ele in range(1,num+1):
    new_List.append(ele*ele);

print(new_List);