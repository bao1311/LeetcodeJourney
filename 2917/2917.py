class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        '''
        count the bits at every position
        '''
        arr = [0] * 31
        res = 0
        # bit nao ra bit day
        # arr[0] for bit 0
        # so make the bit 0 at arr[0]. It's easiest to remember it like that
        for num in nums:
            for i in range(31):
                arr[i] += (num >> i) & 1
        
        b = 2**0
        for i,v in enumerate(arr):
            if v >= k:
                res = res | (1 << i)
        return res


