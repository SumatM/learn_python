# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"


arr = ["flower","flow","flight"];


prefix = ""

charPrefix = {}

for ele in arr:
     for char in ele:
          if charPrefix[char]==True:
            charPrefix[char]=False;
          else:
             charPrefix[char] = True;


print(charPrefix)