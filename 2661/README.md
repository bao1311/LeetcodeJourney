1. Brute force solution would cause: O(N^2) which will give TLE
Approach: Find the element and delete the number of element of the rows or cols and then check if the row or column of that element == row or column of the table

2. Optimal approach: Time: O(N) Space: O(N)
Approach: You can populate the row and column of the array first.
Use a map to store the row and col or that element
Everytime we access an element, decrement the column and row where that element resides
Then check if that row or col equals to 0

