# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        
        fast = head
        slow = head

        current = head
        prev = None

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        if fast:
            slow = slow.next    

        while prev and slow:
            if slow.val != prev.val:
                return False

            prev = prev.next
            slow = slow.next

        return True


        
        