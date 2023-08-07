### Problem **10: Modify the tuple**

#Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

#tuple1: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44,[1,22], 55)

new_tuple = ()

list = list(tuple1)


for key in list:
    if type(key)!=int:
        for i in range(len(key)):
            if key[i] == 22:
                key[i] = 222;
   
tuple1 = tuple(list);

print(tuple1)