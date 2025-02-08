class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        '''
        '''
        jobs = sorted(zip(difficulty,profit))
        worker.sort()
        
        j = 0
        n = len(worker)
        ans = 0
        cur = 0
        for i in range(n):
            while j < len(jobs) and jobs[j][0] <= worker[i]:
                cur = max(cur,jobs[j][1])
                j += 1
            ans += cur
            
        return ans
