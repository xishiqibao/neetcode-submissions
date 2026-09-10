class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in A:
                return [A[diff], idx]
            A[num] = idx
        
