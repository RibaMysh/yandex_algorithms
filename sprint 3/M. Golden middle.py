from typing import List


def solution(A, B, n, m):
    total = n + m
    half = total // 2

    if m < n:
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:

        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)

            return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return solution(nums1, nums2, len(nums1), len(nums2))


n = int(input())
m = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(A, B, n, m))
