#creating a dictionary of characters in a string
s=input('Enter a string:')
d={}
for i in s:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1

print(d)

