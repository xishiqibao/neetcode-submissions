class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        V = 0
        l = 0   
        r = len(height) - 1

        leftmax, rightmax = height[l], height[r]

        while l < r:
            if(leftmax < rightmax):
                l += 1
                leftmax = max(leftmax, height[l])
                V += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                V += rightmax - height[r]
            
        return V
