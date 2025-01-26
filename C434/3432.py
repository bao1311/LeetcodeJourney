class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        tot = sum(nums)
        for i in range(1,n):
            a = sum(nums[0:i])
            if (a - (tot - a))% 2 == 0:
                res += 1
        return res
            
        
