class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friendsSet = set(friends)
        res = []

        for id in order:
            if id in friendsSet:
                res.append(id)
        return res