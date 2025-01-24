class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        # if can reach the terminal node -> safe node
        # safe if every possible path start from that nodes lead to a terminal node

        # have to mark the node
        # optimal dfs

        n = len(g)

        c = [0] * n

        # 0: not visited
        # 1: works fine (safe)
        # 2: cause cycle
        def dfs(i):
            if c[i] != 0:
                return c[i] == 1
            c[i] = 2 # put it here 
            # use backtrack
            for n in g[i]:
                if not dfs(n):
                    return False
            
            c[i] = 1
            return True
        ret = []
        for i in range(n):
            if dfs(i):
                ret.append
            
        return ret
