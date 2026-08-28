# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         num_2 = set(nums)
#         return len(num_2) != len(nums)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i - 1] == nums[i]):
                return True
        return False

