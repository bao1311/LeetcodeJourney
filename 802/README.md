Naive: DFS on every node and check cycle with a new set => O(N^2). not working since 10^4 * 4*10^4

1st Solution: we can introduce a new feature that is unvisited, safe, unsafe. Then use backtrack to do this problem O(N)

2nd Solution: Use Kahn's algo to reduce the degree of the node


