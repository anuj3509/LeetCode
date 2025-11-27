class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # prefixSum = []
        # sum = 0

        # # calculating prefix sum
        # for num in nums:
        #     sum += num
        #     prefixSum.append(sum)
        # print(prefixSum)

        # res = float("-inf")     # because we want to calculate max value, so this makes it easier for comparison

        # for i in range(len(nums)):
        #     j = i
        #     while j+k-1 < len(nums):    # choosing a subarray of size divisible by k from the current index and updating the max sum
        #         if i == 0:
        #             subtract = 0    # if prefix sum is out of bound, we can set it to zero
        #         else:
        #             subtract = prefixSum[i-1]

        #         res = max(res, prefixSum[j+k-1] - subtract)
        #         j += k      # we add the next 'k' elements to the subarray

        # return res

        # # Above solution gets TLE error :((




        prefix = [float("inf")] * k
        prefix[0] = 0
        res = float("-inf")
        total = 0

        for i, n in enumerate(nums):
            total += n
            length = i + 1      # length of the subarray
            prefix_len = length % k
            res = max(res, total - prefix[prefix_len])
            prefix[prefix_len] = min(prefix[prefix_len], total)

        return res