class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        memo = {}
        for i in range(1, n + 1):
            if i <= 3:
                result = i
            else:
                result = memo[i - 1] + memo[i - 2]
            memo[i] = result

        return memo[n]
        
        
        
        
