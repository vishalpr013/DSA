class Solution(object):
    def frequencySort(self, nums):
        ans = {}
        for num in nums:
            if num in ans:
                ans[num]+=1
            else:
                ans[num]=1
        sorted_ans = sorted(ans.keys(),key = lambda x:(ans[x],-x))
        
        result=[]
        for num in sorted_ans:
            result.extend([num]*ans[num])
        return result