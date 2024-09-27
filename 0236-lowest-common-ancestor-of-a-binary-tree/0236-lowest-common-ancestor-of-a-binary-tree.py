# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ancestor = None
        
        def recursive(node):

            if not node:
                return False

            left = recursive(node.left)
            right = recursive(node.right)

            current = (node == p or node == q)

            if current + left + right >= 2:
                self.ancestor = node       

            return current or left or right

        recursive(root)
        return self.ancestor
