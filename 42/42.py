class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        maxL = maxR = 0
        r = len(height) - 1
        res = 0
        while l <= r:
            if maxL == maxR == 0:
                maxL = height[l]
                maxR = height[r]
                l += 1
                r -= 1
            else:
                if maxL >= maxR:
                    ans = min(maxL,maxR) - height[r]
                    ans = 0 if ans < 0 else ans
                    res += ans
                    maxR = max(maxR,height[r])
                    r -= 1
                else:
                    ans = min(maxL,maxR) - height[l]
                    ans = 0 if ans < 0 else ans
                    res += ans
                    maxL = max(maxL,height[l])
                    l += 1
        return res
