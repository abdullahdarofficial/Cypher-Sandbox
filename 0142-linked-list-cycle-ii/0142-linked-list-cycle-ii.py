# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def check_cycle(start):
            slow = start
            fast = start
            count = 0
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                count += 1

                if slow == fast:
                    return count

            return 0

        count = check_cycle(head)
        if count > 0:
            # cycle exists

            curr_node = head
            next_node = head.next
            curr_count = count

            while curr_node and curr_node != next_node:
                next_node = next_node.next
                curr_count -= 1
                if curr_count == 0:
                    curr_node = curr_node.next
                    curr_count = count

            return curr_node if curr_node != None else -1
                
