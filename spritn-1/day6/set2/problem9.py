### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

#{'name': 'Kelly', 'salary': 8000}


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]


my_dictionary={}

for ele in keys:
    my_dictionary[ele]=sample_dict[ele]


print(my_dictionary)