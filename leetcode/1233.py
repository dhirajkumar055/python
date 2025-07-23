class Tree:
    def __init__(self):
        self.val={}

class Solution:
    def removeSubfolders(self, folder: list[str]):
        root=Tree()
        root.val["/"]=Tree()
        result=[]
        folder=sorted(folder, key=lambda x: len(x))
        for i in folder:
            temp=root.val["/"]
            splittext=i.split("/")
            for index,j in enumerate(splittext):
                try:
                    if temp.val[j].val["True"]==True:
                        break
                except:
                    pass
                try:
                    if temp.val[j]:
                        temp=temp.val[j]
                except:
                    temp.val[j]=Tree()
                    temp=temp.val[j]
                if index==len(splittext)-1:
                    temp.val["True"]=True
                    result.append(i)           
        
        return result


a=Solution()
print(a.removeSubfolders(["/ah/al/am","/ah/al"]))
