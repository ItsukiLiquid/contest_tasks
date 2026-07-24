# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_val = []
        for nodes in lists:
            while nodes:
                all_val.append(nodes.val)
                nodes = nodes.next
        all_val.sort()
        dummy = ListNode()
        cur = dummy
        for node in all_val:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next
        
