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
        # we initialize a list, put all vals, sort and transform it into ListNode
        vals_list = []
        while cur1:
            vals_list.append(cur1.val)
            if cur1: cur1 = cur1.next
        while cur2:
            vals_list.append(cur2.val)
            if cur2: cur2 = cur2.next
        vals_list.sort()
        for elem in vals_list:
            cur.next = ListNode(elem)
            cur = cur.next
        # # edge cases where there is either list1 or lis2 emit
        # if not list1: return list2
        # if not list2: return list1
        # while cur1 and cur2:
        #     val1 = cur1.val if cur1 else None
        #     val2 = cur2.val if cur2 else None
        #     print(f"val1: {val1}, val2: {val2}")
        #     # if two values are distinct we first put the one who is less
        #     if val1 != val2:
        #         # we reserve 2 spaces so we use double next iterators to put both val1 and val2
        #         if val1 < val2:
        #             cur.next = ListNode(val1)
        #             cur.next.next = ListNode(val2)
        #             print(f"cur.next: {cur.next.val} ({val1}), cur.next.next: {cur.next.next.val} ({val2})")
        #         else:
        #             cur.next = ListNode(val2)
        #             cur.next.next = ListNode(val1)
        #             print(f"cur.next: {cur.next.val} ({val2}), cur.next.next: {cur.next.next.val} ({val1})")

        #     else:
        #         cur.next = ListNode(val1)
        #         cur.next.next = ListNode(val2)
        #         print(f"cur.next: {cur.next.val} ({val1}), cur.next.next: {cur.next.next.val} ({val2})")
        #     # now check for existence of value for the next pointer: it may contain two values, not 1 as usual
        #     if cur.next:
        #         if cur.next.next: cur = cur.next.next # the last value
        #         else: cur = cur.next
        #     if cur1: cur1 = cur1.next
        #     if cur2: cur2 = cur2.next
        # if cur1 and not cur2:
        #     while cur1:
        #         val1 = cur1.val
        #         cur.next = ListNode(val1)
        #         cur = cur.next
        #         if cur1: cur1 = cur1.next
        # if cur2 and not cur1:
        #     while cur2:
        #         val2 = cur2.val
        #         cur.next = ListNode(val2)
        #         cur = cur.next
        #         if cur2: cur2 = cur2.next
        return dummy.next
