class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        '''
        left = target - baseCosts
        
        '''
        res = baseCosts[0]
        def help(cur,ind):
            nonlocal res
            if ((abs(target - cur) == abs(target - res)) and cur < res) or (abs(target-cur) < abs(target-res)):
                res = cur
            if ind >= len(toppingCosts):
                return
            help(cur,ind+1)
            help(cur+toppingCosts[ind],ind+1)
            help(cur+toppingCosts[ind]*2,ind+1)
        for cost in baseCosts:
            help(cost,0)
            




        return res
        
