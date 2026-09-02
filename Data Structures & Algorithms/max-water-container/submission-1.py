class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        maxV = 0
        r = len(heights) - 1
        while l < r:
            curV = min(heights[l], heights[r]) * (r - l)
            maxV = max(curV, maxV)
            if(heights[l] < heights[r]):
                l += 1
            else:
                r -=1
        return maxV