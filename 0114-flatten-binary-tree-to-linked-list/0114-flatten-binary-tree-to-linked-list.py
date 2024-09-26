# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        

        def recursive(node):
            if node:
                print(node)
                recursive(node.left)
                recursive(node.right)

                if not node.left:
                    return
                right = node.right
                left = node.left
                while left.right:
                    left = left.right
                left.right = right
                node.right = node.left
                node.left = None
            
        
        recursive(root)