class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min(dp[i - c] + 1)

        dp = [10001] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if(c <= i):
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[-1] if dp[-1] != 10001 else -1 
