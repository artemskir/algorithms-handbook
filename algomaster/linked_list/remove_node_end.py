

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]


https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow = fast = dummy
        steps = 0
        while fast.next is not None:
            fast = fast.next
            if steps >= n:
                slow = slow.next
            steps += 1
        slow.next = slow.next.next
        return dummy.next

if __name__ == '__main__':
    def _list_to_head(vals: list[int]) -> ListNode | None:
        head = tail = None
        for v in vals:
            node = ListNode(v)
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
        return head

    def _head_to_list(head: ListNode | None) -> list[int]:
        out: list[int] = []
        while head is not None:
            out.append(head.val)
            head = head.next
        return out

    def assert_remove_nth(head_vals: list[int], n: int, expected: list[int]) -> None:
        head = _list_to_head(head_vals)
        result = Solution().removeNthFromEnd(head, n)
        actual = _head_to_list(result)
        assert actual == expected, (
            f"head={head_vals}, n={n}: expected {expected}, got {actual}"
        )

    assert_remove_nth([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
    assert_remove_nth([1], 1, [])
    assert_remove_nth([1, 2], 1, [1])
    print("All tests passed.")