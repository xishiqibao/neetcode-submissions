class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] = max(nums[i], min dp[i] * nums[i], max dp[i] * nums[i])

        n = len(nums)
        maxDP = [0] * n
        minDP = [0] * n

        maxDP[0] = nums[0]
        minDP[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            maxDP[i] = max(
                nums[i],
                maxDP[i - 1] * nums[i],
                minDP[i - 1] * nums[i]
            )
            minDP[i] = min(
                nums[i],
                maxDP[i - 1] * nums[i],
                minDP[i - 1] * nums[i]
            )
            res = max(res, maxDP[i])
        return res
            