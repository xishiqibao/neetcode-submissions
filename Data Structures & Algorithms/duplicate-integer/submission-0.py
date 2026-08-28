class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_2 = set(nums)
        return len(num_2) != len(nums)
