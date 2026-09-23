class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        for i, num in enumerate(nums):
            A[num] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in A and A[diff] != i:
                return [i, A[diff]]
        return []