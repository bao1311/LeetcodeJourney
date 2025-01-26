class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # brute force?
        # Use prefix sum. loop through each subarray then take sum - 1 element each to find the desired result
        # TC: O(N^3)
        # Optimal: Kadane (Yes but not enough)
        # Tried to divide this problem into 2 smaller problem
        # So when we delete an element, we will have to account for the maxSum before that element and maxSum after that element
        # So we will populate maxEndHere and maxStartHere
        '''
        1 0 -2 -4 9 5 -3 10 -17
        '''

        n = len(arr)        
        if n == 1:
            return arr[0]
        mx = arr[0]
        maxEndHere = [0] * n
        maxEndHere[0] = arr[0]
        for i in range(1,n):
            maxEndHere[i] = max(arr[i],arr[i] + maxEndHere[i-1])
            mx = max(maxEndHere[i],mx)
        maxStartHere = [0] * n
        maxStartHere[n-1] = arr[-1]
        for i in range(n-2,-1,-1):
            maxStartHere[i] = max(arr[i],arr[i] + maxStartHere[i+1])
            mx = max(mx,maxStartHere[i])
        for i in range(1,n-1):
            mx = max(mx,maxStartHere[i+1]+maxEndHere[i-1])
        return mx

