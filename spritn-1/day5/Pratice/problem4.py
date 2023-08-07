# Write a Python program that uses a while loop to find the sum of the first 10 positive integers. Use the break statement to stop the loop after the sum exceeds 30.


#for loop in range 
ans = 0

for i in range(10+1):
   ans=i+ans

print(ans)

#for in list or array;

arr = [1,2,3,4,5,6,7,8,9,10]

ans = 0;

for ele in arr:
  ans+=ele;

print(ans);


#while loop

ans = 0

i = 0;

while i<=10:
   ans= i + ans
   if ans > 30:
    break
   i+=1
print(ans)


