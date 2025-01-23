class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ##### I am using topological sort for solving this problem  #####

        premap = {i:[] for i in range(numCourses)}  # initially map every course to an empty list

        for crs, pre in prerequisites:
            premap[crs].append(pre) 

        # A course has 3 possible states:-
        #   1. visited: crs has been added to the output
        #   2. visiting: crs not added to the output, but added to the cycle
        #   3. unvisited: crs not added to output or cycle

        output = []
        visit, cycle = set(), set()   

        def dfs(crs):
            # Detecting a loop in the course schedule
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)

            for pre in premap[crs]:
                if not dfs(pre): return False   # return false if we find that any one can't be completed
            cycle.remove(crs)   # remove after we finish visiting
            visit.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output