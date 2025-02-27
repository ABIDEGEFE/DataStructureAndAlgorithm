# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        s1 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        s1_val = ""
        for i in range(len(s1)-1, -1, -1):
            s1_val += s1[i]
        s2 = ""
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        s2_val = ""
        for i in range(len(s2)-1, -1, -1):
            s2_val += s2[i]
        sum = int(s2_val) + int(s1_val)
       
        l = len(str(sum))-1
        H = ListNode(int(str(sum)[l]))
        current = H

        for i in range(l-1, -1, -1):

            c = ListNode(int(str(sum)[i]))
            current.next = c
            current = c
        return H

        
     