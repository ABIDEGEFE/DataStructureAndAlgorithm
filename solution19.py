# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):

        current = head
        target = head
        prev = None
        count = 0
        found_gap = False

        while current.next:
            count += 1
            if count % n == 0:
                found_gap = True
            if found_gap:
                prev = target
                target = target.next
            current = current.next
        
        if target == head:
            head = head.next
        else:
            prev.next = target.next
        
        return head
        