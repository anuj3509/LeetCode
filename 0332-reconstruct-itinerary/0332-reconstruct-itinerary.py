# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adj = {src:[] for src, dest in tickets}
#         tickets.sort()

#         for src, dest in tickets:
#             adj[src].append(dest)

#         res = ["JFK"]
#         def dfs(src):
#             if len(res) == len(tickets) + 1:
#                 return True

#             if src not in adj:      # if source is not in the adjacency list
#                 return False
            
#             temp = list(adj[src])
#             for i, v in enumerate(temp):
#                 adj[src].pop(i)
#                 res.append(v)

#                 if dfs(v): return True
                
#                 # reversing the above decision we made if recursive call is not converging
#                 adj[src].insert(i, v)
#                 res.pop()
#             return False

#         dfs("JFK")
#         return res



class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        # building the adjacency list with destinations sorted in reverse order
        for src, dest in sorted(tickets, reverse=True):
            adj[src].append(dest)
        
        result = []
        stack = ["JFK"]
        
        # traverse the graph using a stack iteratively
        while stack:
            while adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            result.append(stack.pop())
        
        # The result is built in reverse order, so reverse it at the end
        return result[::-1]
