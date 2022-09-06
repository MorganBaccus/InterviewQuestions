# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current and current.next :
            #comparing the val at current node with current.next
            if current.next.val == current.val :
                #if == then just taking the address of current.next.next in current.next
                current.next = current.next.next
            else :
                #else just update pointer normally
                current = current.next
        return head
