class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        '''
        2: [0]
        1: [1,3]
        3: [2,5,6,7,8,9,10,11,13]
            5 
            5   6 
            |6 - 5|
            5   6   9
            |6 - 5| + |9 - 6|
            5   6   9   10
            |6 - 5| + |9 - 6| + |10 - 9|

        => 2 7 13 20
        [2,5,6,8,9]
        6 * 2 - (5 + 2) + (9 + 8) - (6*2)
        2----5----6----8---9
             <---->
             <------------->
             <--------->
        <---->
        
        9 - 2 + 6 - 5 + 8 - 5 
        '''
        n = len(arr)
        mp = defaultdict(list)
        res = [0]*n
        for i in range(n):
            mp[arr[i]].append(i)
        for x in mp:
            lst = mp[x]
            pref = [0] * (len(lst) + 1)
            n = len(lst)
            for i in range(n):
                pref[i+1] = pref[i] + lst[i]
            '''
            2: [3,5,6,9]
            [0,3,8,14,23]
            '''
            
            for i in range(0,n):
                cur = lst[i]
                res[cur] = (cur * i) - pref[i] + pref[-1] - pref[i+1] - (cur * (n-i-1))
            
        return res
