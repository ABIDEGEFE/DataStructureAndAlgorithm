# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
       
        if not head or not head.next:
            return head
        current = head.next
        prev = head
        head = head.next
        no_swap = 0
        right_shift = None

        while prev and current:

            node = current.next
            prev.next = node
            current.next = prev

            if no_swap > 0:
                right_shift.next = current
            right_shift = prev
            prev = prev.next
            if prev:
                current = prev.next
            no_swap += 1
        return head
            