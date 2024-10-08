# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        # direction = 0 left, 1 right
        self.maxcount = 0
        def recursive(node, direction, count):
            if not node:
                return
            self.maxcount = max(self.maxcount, count)

            if direction == 0:
                recursive(node.left, 0, 1)
                recursive(node.right, 1, count + 1)
            else:
                recursive(node.left, 0, count + 1)
                recursive(node.right, 1, 1)
        recursive(root, 0, 0)
        return self.maxcount