class Solution:
    def maximumUniqueSubarray(self, nums):
        d={}
        dp=[nums[0]]
        d[nums[0]]=0
        last=-1
        for index,element in enumerate(nums):
            if index==0:
                continue
            try:
                if d[element]>=0:
                    if d[element]>last and last != -1:
                        d[element]=index
                        last=d[element]
                        dp.append(dp[index-1]+element)
                        continue
                    dp.append(element+dp[index-1]-dp[d[element]])
                    d[element]=index
                    last=d[element]
            except:
                d[element]=index
                dp.append(dp[index-1]+element)
        return max(dp)

a=Solution()
print(a.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
