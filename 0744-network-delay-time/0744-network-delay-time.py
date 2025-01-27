class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # Djikstra's Algorithm to find shortest path algorithm

        edges = collections.defaultdict(list)   # Finding neighbours of every node
        for u, v, w in times:
            edges[u].append((v, w))     # v -> neighbour node, w -> weight of that node

        minheap = [(0, k)]      # starting value is 0 (weight to reach that node) and the given node is k
        visit = set()
        t = 0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1 + w2, n2))
                    
        return t if len(visit) == n else -1