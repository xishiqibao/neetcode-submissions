# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l1 = self.maxDepth(root.left) + 1
        l2 = self.maxDepth(root.right) + 1
        maxL = max(l1, l2)
        return maxL


            