class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [100000] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if(coin <= i):
                    memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[amount] if memo[amount] != 100000 else -1