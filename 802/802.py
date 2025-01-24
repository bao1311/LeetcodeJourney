# Solve by using both Kahn's algo and graph marking

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        # if can reach the terminal node -> safe node
        # safe if every possible path start from that nodes lead to a terminal node

        # Kahn's algo
        n = len(g)
        out = [0] * n
        O = [[] for _ in range(n)]
        for i in range(n):
            for nei in g[i]:
                O[nei].append(i)
                out[i] += 1
        ret = []
        q = deque()
        for i in range(n):
            if out[i] == 0:
                q.append(i)
                ret.append(i)

        while q:
            t = q.popleft()
            for nei in O[t]:
                out[nei] -= 1
                if out[nei] == 0:
                    ret.append(nei)
                    q.append(nei)
                
        return sorted(ret)


        # have to mark the node
        # optimal dfs

        # n = len(g)

        # c = [0] * n

        # # 0: not visited
        # # 1: works fine (safe)
        # # 2: cause cycle
        # def dfs(i):
        #     if c[i] != 0:
        #         return c[i] == 1
        #     c[i] = 2 # put it here 
        #     # use backtrack
        #     for n in g[i]:
        #         if not dfs(n):
        #             return False
            
        #     c[i] = 1
        #     return True
        # ret = []
        # for i in range(n):
        #     if dfs(i):
        #         ret.append
            
        # return ret








