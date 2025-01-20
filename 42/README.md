Explanation:
1. Brute force approach:
TC: O(N^2)
SC: O(1)

2 for loops: first one traverse through the array. Then find if there is any column > max(column) before
Formula = maxL - heights[j]

2. Optimal approach:
TC: O(N)
SC: O(1)

Have 2 pointers one at the beginning and the others at the end.
Focus on which one has the lower height. 
2 cases:
- Meet the smaller column: res += min(maxL,maxR) - height[curr]
- Meet the bigger one: min(maxL,maxR) - height[curr] would be < 0, which we don't want so res remains the same

Remember to adjust the max height of the 2 sides afterwards

