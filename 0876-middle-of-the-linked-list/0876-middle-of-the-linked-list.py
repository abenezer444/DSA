# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ahead=head
        countH = head
        count = 0
        while countH:
            countH = countH.next
            count += 1
        check = count//2
        while ahead and check:
            ahead = ahead.next
            check -= 1
        return ahead
        
    
        