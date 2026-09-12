

"""
Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 231 - 1

https://leetcode.com/problems/first-bad-version/
"""

bad = 4

def isBadVersion(version):
    return version >= bad

def firstBadVersion(n: int) -> int:
    left, right = 0, n
    while left <= right:
        mid = left + (right - left) // 2
        isBad = isBadVersion(mid)
        if isBad == False:
            left = mid + 1
        else:
            right = mid - 1
    return left
        

if __name__ == "__main__":
    print(firstBadVersion(5))