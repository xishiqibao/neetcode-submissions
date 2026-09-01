class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, i in enumerate(nums):
            if(i > 0):
                break
            if idx > 0 and i == nums[idx - 1]:
                continue
        
            l, r = idx + 1, len(nums) - 1
            while l < r:
                sum = i + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([i, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

