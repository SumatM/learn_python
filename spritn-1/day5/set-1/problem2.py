# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."


# integers 

age = 25
cost = 12 
chips = 50
cost = cost + 21
print(cost)

# floats

pi = 3.14
value = 1.66
temperature = 22.5

# string 

name = 'sumat'

sirName = 'Mallick'

full_Name = name + " " + sirName

print(full_Name)

# boolean 

is_valid = True


# list array 

fruits = ["apple","banana","cherry"]
marks = [21,32,99,82,11]

print(marks)
print(marks[2])
marks[2] = 1
print(marks[2])


#tuple 

coordinates = (10,20)

print(coordinates);

new_cordinates = coordinates+(32,);

print(new_cordinates)




#dictionary Object 

person = {"name":'sumat',"age":11}

print(person["name"])

person['name'] ='aman'

print(person)

#set 

unique_number = {1,2,3,4,5}


print(unique_number);
print(3 in unique_number);

happy_number = unique_number.union({6})

print(happy_number)

# unions create a new set , if not value pass returns the shallow copy 


