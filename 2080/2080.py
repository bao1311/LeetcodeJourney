class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.mp = defaultdict(list)
        # prefixSum approach
        for i,v in enumerate(arr):
            self.mp[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.mp[value],right) - bisect_left(self.mp[value],left)
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
