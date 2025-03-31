class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        splits = []
        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i + 1])
        splits.sort()
        
        i = k - 1

        # maxScore = weights[0] + weights[-1] + sum(splits[-i:])
        # minScore = weights[0] + weights[-1] + sum(splits[:i])
        
        # when we take the difference, the weights[0] and weights[-1] would be cancelled anyways
        maxScore = sum(splits[-i:])
        minScore = sum(splits[:i])

        return (maxScore - minScore)