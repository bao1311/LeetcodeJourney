class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        10,2,3,4,5,5,4,3,2,2
        10,8,8,8,8,8,8,10
        10,2,3,2,4,5,2,12,17,2,3,4,5,3,6,7,100
        1,1,1,1,3,3,3,5,5,5
        '''
        ele = nums.count(k)

        mx = 0

        for i in range(1,51):
            occur,max_occur = 0,0
            for num in nums:
                if num == k:
                    occur -= 1
                elif num == i:
                    occur += 1
                occur = max(occur,0)
                max_occur = max(max_occur,occur)
            mx = max(max_occur,mx)
        return mx + ele
                    
