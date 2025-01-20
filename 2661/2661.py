class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        '''
        brute force: len(arr) * max(m,n)
        '''
        n = len(mat)
        m = len(mat[0])
        row = [0] * n
        col = [0] * m

        newA = []
        mp = {}
        for i in range(n):
            for j in range(m):
                mp[mat[i][j]] = (i,j)
        for i,v in enumerate(arr):
            r,c = mp[v]
            row[r] += 1
            col[c] += 1
            if row[r] == m or col[c] == n:
                return i
        return -1


        
