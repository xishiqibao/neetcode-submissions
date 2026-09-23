class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        memo[0], memo[1] = 0, 0

        for i in range(2, n + 1):
            memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2])
        return memo[n]
