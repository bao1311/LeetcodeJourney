class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = sorted([t[0],t[1],i] for i,t in enumerate(tasks))
        curr = t[0][0]
        heap = []
        i = 0
        n = len(tasks)
        res = []
        while len(res) < n:
            while i < n and t[i][0] <= curr:
                heappush(heap,(t[i][1],t[i][2]))
                i += 1
            if heap:
                diff,orig = heappop(heap)
                curr += diff
                res.append(orig)
            elif i < n:
                curr = t[i][0]

        return res
