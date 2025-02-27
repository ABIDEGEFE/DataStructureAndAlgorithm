
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
       
        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        left_head = head
        right_head = mid.next
        mid.next = None

        l = self.sortList(left_head)
        r = self.sortList(right_head)

        sorted_list = self.merge_and_sort(l, r)
        return sorted_list

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_and_sort(self, l, r):
        new_head = ListNode()
        current = new_head
        
        while l and r:
            if l.val < r.val:
                current.next = l
                l = l.next
            else:
                current.next = r
                r = r.next
            current = current.next
        
        if l:
            current.next = l
        if r:
            current.next = r

        return new_head.next

        
