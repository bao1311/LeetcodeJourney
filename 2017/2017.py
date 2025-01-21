class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        r1,r2 = 0,0
        r1 = sum(grid[0])
        res = 99999999999
        n = len(grid[0])
        for i in range(n):
            r1 -= grid[0][i]
            res = min(res,max(r1,r2))
            r2 += grid[1][i]

        
        return res

        
