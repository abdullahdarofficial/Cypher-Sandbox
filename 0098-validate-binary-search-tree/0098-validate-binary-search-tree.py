# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
 

        # def recursive(node):
        #     if node:
        #         left = right = True
        #         if node.left:
        #             if node.left.val < node.val:
        #                 left = recursive(node.left)
        #             else:
        #                 left = False
        #         if node.right:
        #             if node.right.val > node.val:
        #                 right = recursive(node.right)
        #             else:
        #                 right = False
        #         return left and right
        #     else:
        #         return True
                
        # return recursive(root)

 
        

        def recursive(node, left = float("-inf"), right = float("inf")):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False

            return recursive(node.left, left, node.val) and recursive(node.right, node.val, right)

        return recursive(root)
                