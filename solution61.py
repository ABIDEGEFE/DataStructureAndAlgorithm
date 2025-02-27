# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        
        if k == 0 or not head or not head.next:
            return head
          
        nodes = []
        cur = head
        prev = None
        while cur:
            nodes.append(cur)
            prev = cur
            cur = cur.next
        if k == len(nodes) or k % len(nodes) == 0:
            return head

        if k > len(nodes):
            k = k % len(nodes)
        p = len(nodes) - k

        new_head = nodes[p]
        new_tail = nodes[p-1]

        prev.next = head
        new_tail.next = None
        head = new_head

        return head