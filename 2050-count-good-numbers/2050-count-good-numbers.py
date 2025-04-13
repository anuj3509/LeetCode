class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even_count = (n + 1) // 2  # number of digits at even indices
        odd_count = n // 2         # number of digits at odd indices
        
        # Using modular exponentiation
        result = (pow(5, even_count, mod) * pow(4, odd_count, mod)) % mod
        return result


# Explanatin for counting positions . . .

# for a string of length n, the number of even positions (0-indexed) 
# is the ceiling of n/2, which can be calculated as even_count = (n + 1) // 2 
# (this works because when n is odd, there is an extra even index).

# the number of odd positions is the floor of n/2, which is odd_count = n // 2.

# multiplying this, total = (5^even_count * 4^odd_count) mod 10**9 + 7