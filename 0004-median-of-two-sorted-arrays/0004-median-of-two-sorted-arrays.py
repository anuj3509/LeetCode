class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # we are running binary search on A only
        if len(B) < len(A):
            A, B = B, A     # set the smaller arrays to A to operate on

        l, r = 0, len(A) - 1

        # Binary search on A [TC: log(min(n, m))]
        while True:
            i = (l + r) // 2    # A
            j = half - i - 2    # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # our left partition is correct for the condition below
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1   # reduce the size of left partition of A
            
            else:
                l = i + 1   # increase the size of left partition of A