# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        rear, front = dummy_node, dummy_node
        for _ in range(n + 1):
            front = front.next
        
        while front:
            rear, front = rear.next, front.next
        rear.next = rear.next.next
        return dummy_node.next
        