class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [10001] * (amount + 1)
        memo[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if(coin <= amount):
                    memo[i] = min(memo[i], memo[i - coin] + 1)

        return memo[amount] if memo[amount] != 10001 else -1