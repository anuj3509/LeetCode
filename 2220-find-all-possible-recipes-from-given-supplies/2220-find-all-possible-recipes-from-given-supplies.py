class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # using dictionary comprehension for the hashmaps below
        can_cook = {s:True for s in supplies}   # hashmap - map each recipe to true or false
        recipe_index = {r:i for i, r in enumerate(recipes)}

        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_index:
                return False

            can_cook[r] = False     # to avoid circular loop

            for n in ingredients[recipe_index[r]]:
                if not dfs(n):
                    return False
            can_cook[r] = True
            return can_cook[r]

        # res = []
        # for r in recipes:
        #     if dfs(r):
        #         res.append(r)
        # return res
        return [r for r in recipes if dfs(r)]   # list comprehension [can be written instead of above 5 lines]