class Solution:
    def countPairs(self, d: List[int]) -> int:
        mp = defaultdict(int)
        MOD = 10**9+7
        res = 0
        for i in d:
            cur = 1
            for j in range(22):
                if cur - i in mp:
                    res = (res + mp[cur-i])%MOD
                cur *= 2
            mp[i] += 1
        return res
