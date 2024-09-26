# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.total_sum = 0
        def recursive(node, s):

            if node: 

                if not node.left and not node.right:
                    self.total_sum += (s * 10) + node.val 
                    return 

                recursive(node.left, (s * 10) + node.val )
                recursive(node.right, (s * 10) + node.val)


        recursive(root, 0)
        return self.total_sum
