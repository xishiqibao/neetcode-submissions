class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = nums[0]
        n = len(nums)

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]