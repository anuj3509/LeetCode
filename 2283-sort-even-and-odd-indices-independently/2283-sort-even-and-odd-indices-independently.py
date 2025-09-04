class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        nums1 = sorted(nums[::2])
        nums2 = sorted(nums[1::2], reverse = True)

        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(nums1[i // 2])
            else:
                res.append(nums2[i // 2])
        return res

        # print(nums1)
        # print(nums2)