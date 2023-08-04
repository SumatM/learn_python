# Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

s1 = "Ault"
s2 = "Kelly"

#output : AuKellylt

mid = len(s1)/2

s3 = ""

i = 0


while i<len(s1):
    if(i==mid):
        s3+=s2;

    s3+=s1[i];
    i+=1;

print(s3);
