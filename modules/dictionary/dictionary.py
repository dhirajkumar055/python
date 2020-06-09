l=[1,1,1,2,2,3,3,3,4,4,4,4,4]
d={}
for i in l:
    d[i]=d.get(i,0)+1

print(d)