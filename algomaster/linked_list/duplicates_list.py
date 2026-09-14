from typing import Optional


"""
Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev_node = None
        while node != None:
            if prev_node == None:
                prev_node = node
                node = node.next
                continue
            if node.val == prev_node.val:
                prev_node.next = node.next
                node = node.next
            else:
                prev_node = node
                node = node.next
        return head


if __name__ == '__main__':
    def _list_to_head(vals: list[int]) -> Optional[ListNode]:
        head = tail = None
        for v in vals:
            node = ListNode(v)
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
        return head

    def _head_to_list(head: Optional[ListNode]) -> list[int]:
        out: list[int] = []
        while head is not None:
            out.append(head.val)
            head = head.next
        return out

    def run_example(head_vals: list[int]) -> None:
        head = _list_to_head(head_vals)
        result = Solution().deleteDuplicates(head)
        print(f"Input: head = {head_vals}")
        print(f"Output: {_head_to_list(result)}")

    run_example([1, 1, 2])
    print()
    run_example([1, 1, 2, 3, 3])
