class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # res = []
        # for i in range(len(folder)):
        #     is_sub = False
        #     for j in range(len(folder)):
        #         if i != j and folder[i].startswith(folder[j] + '/'):
        #             is_sub = True
        #             break
        #     if not is_sub:
        #         res.append(folder[i])
        # return res

        # # brute force -> TC: O(n^2 * L) ; SC: O(n)




        # sort the list, if a folder is subfolder they will be adjacent; 
        # only add the folder if its not a subfolder of the previous folder
        folder.sort()
        res = []
        for f in folder:
            if not res or not f.startswith(res[-1] + '/'):
                res.append(f)
        return res

        # TC: O(n*log(n) + n*L)   ;   SC: O(n)