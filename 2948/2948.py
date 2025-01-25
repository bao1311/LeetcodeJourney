class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # O(n) or O(nlogn)
        mp = {} # map element and group index
        grps = [] # list of deque
        for i in sorted(nums):
            if not grps or abs(grps[-1][-1] - i) > limit:
                grps.append(deque())
            mp[i] = len(grps) - 1
            grps[-1].append(i)
        res = []
        for i in nums:
            idx = mp[i] # index of group
            res.append(grps[idx].popleft())
        return res
