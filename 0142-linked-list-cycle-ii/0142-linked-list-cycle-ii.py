# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # def check_cycle(start):
        #     slow = start
        #     fast = start
        #     count = 0
        #     while fast and fast.next:
        #         slow = slow.next
        #         fast = fast.next.next
        #         count += 1

        #         if slow == fast:
        #             return count

        #     return 0

        # count = check_cycle(head)
        # if count > 0:
        #     # cycle exists

        #     curr_node = head
        #     next_node = head.next
        #     curr_count = count

        #     while curr_node and curr_node != next_node:
        #         next_node = next_node.next
        #         curr_count -= 1
        #         if curr_count == 0:
        #             curr_node = curr_node.next
        #             curr_count = count

        #     return curr_node if curr_node != None else -1
                

        if not head or not head.next:
            return None
        
        # Step 1: Detect the cycle using Floyd’s algorithm
        def get_intersection(start):
            slow = fast = start
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:  # Cycle detected
                    return slow
            return None
        
        intersection = get_intersection(head)
        if not intersection:
            return None  # No cycle
        
        # Step 2: Find the cycle's starting node
        pointer1 = head
        pointer2 = intersection
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        return pointer1  # The start of the cycle