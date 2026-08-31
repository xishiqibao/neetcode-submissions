class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        res = []
        for i in nums:
            count[i] += 1
        
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if(j > i + 1 and nums[j] == nums[j - 1]):
                    continue
                target = -(nums[i] + nums[j])
                if target in count and count[target] > 0:
                    res.append([nums[i], nums[j], target])
            for i in range(i + 1, len(nums)):
                count[nums[i]] += 1
        return res



# O(nlogn) + O(n) + O(n^2) + O(n^2) => O(n^2)

