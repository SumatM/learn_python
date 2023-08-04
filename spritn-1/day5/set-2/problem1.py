# ### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


bag = "";

for i in range(1,5+1):
      bag+= str(i)+" ";
      print(bag);