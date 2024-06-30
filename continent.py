cont={}
for i in range(0,7):
    c=input("Enter the name of continent:")
    cont[c]=len(c)



print("The continents and number of character in each is:")
for k,v in cont.items():
    print(k,v)

    
