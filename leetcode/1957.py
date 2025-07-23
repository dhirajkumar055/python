class Solution:
    def makeFancyString(self, s: str):
        res=[]
        i,last,lastchar=0,0,s[0]
        while i<len(s):
            if s[i]==lastchar and last>=2:
                i=i+1
                continue
            elif s[i]==lastchar:
                last=last+1
            else:
                last=1
                lastchar=s[i]
            res.append(s[i])
            print(i,last,res)
            i=i+1
        return ''.join([x for x in res])

a=Solution()
print(a.makeFancyString("leetcode"))
