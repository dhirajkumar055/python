tempList=[]
with open('fileToSort','r') as f:
 tempList.append(f.read())

tempList=tempList[0].split()
tempList.sort()
for i in tempList:
 print(i)


#Sort on the basis of particular column
li=[(1, 0.23),(78, 0.39),(5, 0.27)]
print(sorted(li,key=lambda l:l[1], reverse=True))


#nC0 + nC1 + nC2 + … nCn = 2n
