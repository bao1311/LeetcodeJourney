Naive Approach:
- TC: O(N^2)
- Loop through each element and find the swappable one!
- swappable: Find the one that have the closest distance and less than it (abs(curr - element)) <= limit
=> Will not work with N = 10^5
Optimal:
- TC: O(NlogN)
- Observation: not every element can be swappable. Some element is just too large and it is more than the limit that we can accept.
- Thus, we can put them in groups.
- The question here is what DS we need for O(1) operation since we do not want to travel the whole groups and find out which element should we pushed into the result.
- Turn out the groups is sort and we can use list of queues for this problem

