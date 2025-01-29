class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Building the adjacency list with cost associated with points
        n = len(points)
        adj = {i:[] for i in range(n)}  # list of [cost, node]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's Algorithm [Minimum Spanning Tree]
        visit = set()
        res = 0
        minheap = [[0, 0]]  # each point is: [cost, point]
        while len(visit) < n:
            cost, i = heapq.heappop(minheap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neicost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap, [neicost, nei])
        return res