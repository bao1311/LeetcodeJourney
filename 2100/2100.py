class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        res = []
        n = len(security)
        inc = [0] * (n)
        dec = [0] * (n)
        if time == 0:
            return [i for i in range(n)]
        for i in range(1,n):
            if security[i] >= security[i-1]:
                inc[i] = inc[i-1] + 1
            if security[i] <= security[i-1]:
                dec[i] = dec[i-1] + 1

        for i in range(time,max(n-time,0)):
            a = inc[i+time] - inc[i]
            b = dec[i] - dec[i-time]
            if  a == time and b == time:
                res.append(i)
        



        return res
