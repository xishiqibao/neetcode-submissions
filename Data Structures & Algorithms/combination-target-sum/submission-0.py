class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, target, [], 0)
        return self.res
    
    def backtrack(self, nums: List[int], target: int, curr: List[int], start: int):
        sumL = 0
        for num in curr:
            sumL += num
        if(sumL == target):
            self.res.append(curr.copy())
            return
        elif(sumL > target):
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.backtrack(nums, target, curr, i)
            curr.pop()
