# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # def insert(node, val):
        #     if node:
        #         if node.val > val:
        #             return node.right = insert(node.right, val)
        #         else:
        #             return node.left = insert(node.left, val)
        #     else:
        #         return TreeNode(val)

        # root = null
        # size = len(nums)
        # mid = size // 2
        # for i in range(mid):
        #     root = insert(root, nums[i])
        #     root = insert(root, nums[mid + i])
        # if size % 2 != 0:
        #     root = insert(root, nums[size - 1])
        
        def buildBST(left,right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)

            return node

        return buildBST(0, len(nums) - 1)
        

