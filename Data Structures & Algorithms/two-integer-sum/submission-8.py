class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        for idx, i in enumerate(nums):
            diff = target - i
            if(diff in A):
                return [A[diff], idx]
            A[i] = idx
        return []
        
