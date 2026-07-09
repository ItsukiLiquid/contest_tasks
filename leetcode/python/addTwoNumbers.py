# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy # cur and dummy are interconnected!! if cur makes changing to listnode, dummy will change too!!!
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10
            cur.next = ListNode(total)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

def make_list(nums):
    dummy = ListNode()
    cur = dummy

    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next

    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


l1 = make_list([2, 4, 3])
l2 = make_list([5, 6, 4])

s = Solution()
final_list = s.addTwoNumbers(l1, l2)
print_list(final_list)