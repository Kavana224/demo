c={'India':2,'Srilanka':1,'Australia':4,'Westindies':2,'Pakisthan':1,'England':1}
l=sorted(c.values())
l.reverse()
l1=[]
for i in l:
    for k,v in c.items():
        if(i==c[k] and k not in l1):
            l1.append(k)

print(l1)
