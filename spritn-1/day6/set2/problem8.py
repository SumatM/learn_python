### Problem **8: Initialize dictionary with default values**

#In Python, we can initialize the keys with the same values.

#{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


new_dictionary= {}

for ele in employees:
    new_dictionary[ele]=defaults;

print(new_dictionary);