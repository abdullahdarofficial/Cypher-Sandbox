# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # def recursive(node, count):
        #     if not node:
        #         return count
        #     left = right = 0
        #     if node.left and node.left.val >= node.val:                    
        #         left = recursive(node.left, count + 1)
        #     if node.right and node.right.val >= node.val:
        #         right = recursive(node.right, count + 1)

        #     return max(left, right)

        # return recursive(root, 1) if root else 0

        def recursive(node, max_val):
            if not node:
                return 0
            
            good_count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            good_count += recursive(node.left, max_val)
            good_count += recursive(node.right, max_val)

            return good_count
        return recursive(root, root.val) if root else 0
