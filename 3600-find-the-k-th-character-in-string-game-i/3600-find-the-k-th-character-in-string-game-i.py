class Solution:
    def kthCharacter(self, k: int) -> str:

        cnt = 0
        length = 1
        # compute the number of expansions - find the smallest power of 2 >= k
        while length < k:
            length *= 2
            cnt += 1

        ans = 0  # number of increments, i.e., how many times we move to second half
        while cnt > 0:
            if k > length // 2:
                ans += 1
                k -= length // 2
            length //= 2
            cnt -= 1
        return chr(ord('a') + ans)

        # TC: O(log k), SC: O(1)


        # Brute Force
        
        # word = "a"
        # while len(word) < k:
        #     nxt = ''.join(chr(ord(c)+1) for c in word)
        #     word += nxt
        # return word[k-1]

        # # TC = SC = O(k)
