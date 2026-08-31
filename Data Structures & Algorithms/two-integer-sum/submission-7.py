class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        for i, num in enumerate(nums):
            diff = target - num
            if(diff in A):
                return [A[diff], i]
            A[num] = i
        return []
        
