class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        for i, num in enumerate(nums):
            A[num] = i
        for index, num in enumerate(nums):
            diff = target - num
            if (diff in A) and (A[diff] != index):
                return [index, A[diff]]
        return []