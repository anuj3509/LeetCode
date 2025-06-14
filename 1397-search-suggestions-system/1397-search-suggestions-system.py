class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, r = 0, len(products) - 1
        res = []

        for i in range(len(searchWord)):
            search = searchWord[i]
            while l<=r and (len(products[l]) <= i or products[l][i] != search):
                l += 1
            while l<=r and (len(products[r]) <= i or products[r][i] != search):
                r -= 1

            words_left = r-l+1
            if words_left >= 3:
                res.append([products[l], products[l+1], products[l+2]])
            elif words_left == 2:
                res.append([products[l], products[l+1]])
            elif words_left == 1:
                res.append([products[l]])
            else:
                res.append([])

        return res