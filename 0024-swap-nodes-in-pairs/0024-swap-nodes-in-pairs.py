# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode()
        dummyNode.next = head

        def swap(node):
            if not node or not node.next:
                return node

            nextNode = node.next
            nextHead = nextNode.next
            nextNode.next = node
            node.next = swap(nextHead)
            return nextNode

        dummyNode.next = swap(head)
        return dummyNode.next
        