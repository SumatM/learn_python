### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# output: yaivePNT

str1 = "PyNaTive"

low = "";

upper = "";


for i in range(len(str1)):
    if str1[i].islower():
        low+=str1[i];
    else:
        upper+=str1[i]


print(low+upper)
