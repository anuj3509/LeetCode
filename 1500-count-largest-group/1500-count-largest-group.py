class Solution:
    def countLargestGroup(self, n: int) -> int:
        count_by_sum = {}   # map sum to count
        
        # group each number by digit sum
        for num in range(1, n + 1):
            digit_sum = 0
            temp = num
            # compute sum of digits
            while temp:
                digit_sum += temp % 10
                temp //= 10
            count_by_sum[digit_sum] = count_by_sum.get(digit_sum, 0) + 1    # increment group

        max_group_size = max(count_by_sum.values()) # find largest group size
        # count how many groups match max size
        return sum(1 for size in count_by_sum.values() if size == max_group_size)
