import math
class Solution:
    def maximumGroups(self, nums):
        return int((math.sqrt(1+8*len(nums))-1))//2

obj=Solution()
l=[2,31,41,31,36,46,33,45,47,8,31,6,12,12,15,35]
print(obj.maximumGroups(l))
