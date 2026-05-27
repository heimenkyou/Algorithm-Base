# https://leetcode.cn/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from structures.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 反转当前节点，并将其连到 prev 上
        def reverse(curr, prev):
            if not curr:
                return prev
            # 把自己的尾巴连到 prev 上
            next_node = curr.next
            curr.next = prev
            # 让下一个节点去重复这个过程，此时下一个节点的前驱（prev）就是当前的 curr
            return reverse(next_node, curr)

        return reverse(head, None)
