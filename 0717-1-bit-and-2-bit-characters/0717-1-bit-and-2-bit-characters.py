class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2 
        return i == len(bits) - 1



        # ------------- not working -------------

        # start_pos = bits[0]
        # for i in range(len(bits)-1):
        #     if bits[i] == 1 and bits[i+1]:
        #         start_pos = bits[i+2]
        #     else:
        #         start_pos = bits[i]
        # return start_pos == bits[-1]