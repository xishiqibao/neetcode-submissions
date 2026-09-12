class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        A = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in A:
                length = 1
                while (num + length) in A:
                    length += 1
                longest = max(length, longest)
        return longest