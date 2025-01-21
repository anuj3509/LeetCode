class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        # adjacency list for the graph
        # since it is a directed acyclic graph, we add links to and fro
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        visited.add(source)
        q = collections.deque()
        q.append(source)

        while q:
            current = q.popleft()
            if current == destination:
                return True

            # if current not in visited:
            #     visited.add(current)    # add the current node in the visited set

            for n in graph[current]:
                if n not in visited:
                    visited.add(n)
                    q.append(n) 

        return False