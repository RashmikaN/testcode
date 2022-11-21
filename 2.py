str1=input()
str2=input()
key,count=str2[-1],0
for i in str1:
    if(i==key):
        count+=1
print(count)