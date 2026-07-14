# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur1 = list1
        cur2 = list2
        cur = dummy
        while cur1 and cur2:
            while cur1 and cur2 and cur1.val < cur2.val:
                cur.next = ListNode(cur1.val)
                if cur1: cur1 = cur1.next
                cur = cur.next
            while cur1 and cur2 and cur1.val >= cur2.val:
                cur.next = ListNode(cur2.val)
                if cur2: cur2 = cur2.next
                cur = cur.next
        else:
            if cur1:
                while cur1:
                    cur.next = ListNode(cur1.val)
                    cur = cur.next
                    cur1 = cur1.next
            elif cur2:
                while cur2:
                    cur.next = ListNode(cur2.val)
                    cur = cur.next
                    cur2 = cur2.next
        return dummy.next
