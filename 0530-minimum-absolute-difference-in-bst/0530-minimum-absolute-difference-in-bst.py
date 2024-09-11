# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if node is None:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Process the current node
            if self.prev is not None:
                # Update the minimum difference
                self.min_diff = min(self.min_diff, abs(node.val - self.prev))
            
            # Update previous node value
            self.prev = node.val
            
            # Traverse the right subtree
            inorder(node.right)

        inorder(root)
        return self.min_diff

            


        

