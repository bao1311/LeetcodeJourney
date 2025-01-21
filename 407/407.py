class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        n = len(heightMap)
        m = len(heightMap[0])
        for i in range(n):
            for j in range(m):
                if i * j * (i - (n-1)) * (j - (m-1)) == 0:
                    heappush(heap,(heightMap[i][j],i,j))
        
        level = 0
        d = [-1,0,1,0,-1]
        res = 0
        visited = set()
        while heap:
            h,x,y = heappop(heap)
            visited.add((x,y))
            level = max(level,h)
            '''
            2 3 4
            5 6 7
            8 9 10
            11 12 13
            14 15 16
            '''
            for i in range(4):
                dx,dy = x + d[i],y+d[i+1]
                if 0 <= dx < n and 0 <= dy < m and (dx,dy) not in visited:
                    if heightMap[dx][dy] < level:
                        res += (level - heightMap[dx][dy])
                    visited.add((dx,dy))
                    heappush(heap,(heightMap[dx][dy],dx,dy))
        return res 
