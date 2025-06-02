class Solution:
    def reverse(self, x: int) -> int:
        org = x     # holds the original value including its sign
        x = abs(x)  # using absolute value to simplify digit reversal
        res = int(str(x)[::-1])     # converts to string, reverses the characters, then back to int

        # if the original was negative, restore the sign by multiplying with -1
        if org < 0:
            res *= -1

        # valid range is [1 * −2^31, 1 * 2^31 - 1]      -->      [−(1<<31), (1<<31)−1]
        # check for 32‑bit signed integer overflow
        if res < -(1 << 31) or res > (1 << 31) - 1:     
            return 0
        return res