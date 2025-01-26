class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Union Find by Rank Algorithm
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(n):
            p = par[n]
            
            # while p is not equal to its own parent, we keep updating its length
            while p != par[p]:
                par[p] = par[par[p]]    # path compression (optimization)
                p = par[p]
            return p
        
        # return False if already merged (can't complete because they have the same parent)
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)     # find parents of n1 and n2

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1    # p1 is the parent of p2
                rank[p1] += rank[p2]
            else:
                par[p1] = p2    # p1 is the parent of p1
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]