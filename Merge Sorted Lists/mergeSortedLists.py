# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1 is None: 
            return list2
    
        if list2 is None: 
            return list1
    
        head = tail = ListNode()

        head1 = list1 
        head2 = list2

        while True:
            if head1 is None:
                tail.next = head2
                break
            if head2 is None:
                tail.next = head1
                break    

            if head1.val > head2.val:
                tail.next = head2
                tail = tail.next
                head2 = head2.next
            else:
                tail.next = head1
                tail = tail.next
                head1 = head1.next

        return head.next
