# Problem 6: Concatenate two lists in the following order

#['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]


newList = [];

for i in range(len(list1)):
    for ele in list2:
        newList.append(list1[i]+""+ele)

print(newList)