# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # hashmap = {}
        # def recursive(node, cumsum, count, map):
        #     if node:
        #         cumsum += node.val
        #         if (cumsum - targetSum) in map:
        #             map[cumsum - targetSum] += 1
        #             count += 1
        #         else:
        #             map[cumsum - targetSum] = 1
        #         left = recursive(node.left, cumsum, count, map)
        #         right = recursive(node.right, cumsum, count, map)
        #         return left + right
        #     else:
        #         return count
                
        # return recursive(root, 0, 0, hashmap)
            
        def recursive(node, cumsum, map):
            if not node:
                return 0

            cumsum += node.val

            count = map.get((cumsum - targetSum), 0)

            if cumsum == targetSum:
                count += 1
            
            map[cumsum] = map.get(cumsum, 0) + 1

            count += recursive(node.left, cumsum, map)
            count += recursive(node.right, cumsum, map)

            map[cumsum] -= 1
            if map[cumsum] == 0:
                del map[cumsum]
            
            return count
        return recursive(root, 0, {})