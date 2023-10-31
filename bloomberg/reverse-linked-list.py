# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverese(node1,node2):
            if not node2:
                return
            if not node2.next:
                node2.next = node1
                return node2
            node2Next = node2.next
            node2.next = node1
            return reverese(node2,node2Next)
        return reverese(None,head)
        