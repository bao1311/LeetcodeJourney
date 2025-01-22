class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        n = len(isWater)
        m = len(isWater[0])
        '''
        1 2 3 4 4 3 2 1 0
        0 1 2 3 4 3 2 1 1
        1 2 3 4 4 4 3 2 2
        '''
        visited = set()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1: # water
                    visited.add((i,j))
                    q.append((0,i,j))
        d = [-1,0,1,0,-1]
        res = [[0 for _ in range(m)] for _ in range(n)]
        while q:
            p,x,y = q.popleft()
            for i in range(4):
                X,Y = x + d[i], y + d[i+1]
                if 0 <= X < n and 0 <= Y < m and (X,Y) not in visited:
                    q.append((p+1,X,Y))
                    res[X][Y] = p + 1
                    visited.add((X,Y))
        return res




