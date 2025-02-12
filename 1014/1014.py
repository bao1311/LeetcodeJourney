class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        '''
        a[i] + i + a[j] - j
        '''
        n = len(values)
        a = 0
        b = values[n-1] - (n-1)
        for i in range(n-2,-1,-1):
            a = max(a,values[i] + i+b)
            b = max(b,values[i] - i)
        return a




        
