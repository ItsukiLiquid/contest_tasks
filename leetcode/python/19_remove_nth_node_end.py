# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        cur = dummy
        length = 0
        while head:
            # n'th from the end -> 0, 1, 2, 3, ... K, we need to find the len
            cur.next = ListNode(head.val)
            length += 1
            cur = cur.next
            head = head.next
        print(length)
        my_list = dummy.next # a head, but now len(list) is known
        dummy2 = ListNode()
        cur2 = dummy2
        for i in range(length):
            print(f"val:{my_list.val},i:{i},isRemPos:{i==length-n}")
            if i == length - n:
                print(f"Removing value: {my_list.val}")
            else:
                cur2.next = ListNode(my_list.val)
                cur2 = cur2.next
            my_list = my_list.next
        return dummy2.next
