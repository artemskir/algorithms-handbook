from typing import Optional

"""

Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
Output: Intersected at '8'

https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = lenB = 0
        a, b = headA, headB
        while a is not None:
            lenA += 1
            a = a.next
        while b is not None:
            lenB += 1
            b = b.next
        a, b = headA, headB
        while lenA > lenB:
            a = a.next
            lenA -= 1
        while lenB > lenA:
            b = b.next
            lenB -= 1
        while a is not b:
            a, b = a.next, b.next
        return a


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

    def _prefix_then(shared_head: Optional[ListNode], prefix_vals: list[int]) -> Optional[ListNode]:
        if not prefix_vals:
            return shared_head
        head = _list_to_head(prefix_vals)
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = shared_head
        return head

    def build_intersected_lists(
        list_a: list[int],
        list_b: list[int],
        skip_a: int,
        skip_b: int,
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
        if skip_a >= len(list_a) or skip_b >= len(list_b):
            return _list_to_head(list_a), _list_to_head(list_b)
        shared_head = _list_to_head(list_a[skip_a:])
        head_a = _prefix_then(shared_head, list_a[:skip_a])
        head_b = _prefix_then(shared_head, list_b[:skip_b])
        return head_a, head_b

    def format_intersection(node: Optional[ListNode]) -> str:
        if node is None:
            return "No intersection"
        return f"Intersected at '{node.val}'"

    def run_example(
        intersect_val: int,
        list_a: list[int],
        list_b: list[int],
        skip_a: int,
        skip_b: int,
    ) -> None:
        head_a, head_b = build_intersected_lists(list_a, list_b, skip_a, skip_b)
        result = Solution().getIntersectionNode(head_a, head_b)
        print(
            f"Input: intersectVal = {intersect_val}, listA = {list_a}, listB = {list_b}, "
            f"skipA = {skip_a}, skipB = {skip_b}"
        )
        print(f"Output: {format_intersection(result)}")

    run_example(2, [2, 2, 4, 5, 4], [2, 4, 5, 4], skip_a=1, skip_b=0)
    print()
    run_example(8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], skip_a=2, skip_b=3)
    print()
    run_example(2, [1, 9, 1, 2, 4], [3, 2, 4], skip_a=3, skip_b=1)
    print()
    run_example(0, [2, 6, 4], [1, 5], skip_a=3, skip_b=2)
