407 Solution:

- At first I thought I can just implement another loop and solve as the Trapping Rainwater I.
- Turn out I was wrong since the water have to be surrounded by 4 blocks which is higher than the one that the water is being above

Approach: Use a min heap and BFS
- This problem should be like the graph coloring.
- You start from the edge first
- Then, you increase the level
- If the current block next to other blocks where the height of the current block < current level we will add that gap to res
- Then we will bfs all the graph
