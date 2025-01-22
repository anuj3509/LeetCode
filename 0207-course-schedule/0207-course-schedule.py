class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}  # initially map every course to an empty list

        for crs, pre in prerequisites:
            premap[crs].append(pre) 

        visit = set()       
        def dfs(crs):
            # Detecting a loop in the course schedule
            if crs in visit:
                return False

            # If a course has no pre requisites
            if premap[crs] == []:
                return True

            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False   # return false if we find that any one can't be completed
            visit.remove(crs)   # remove after we finish visiting
            premap[crs] = []    # mark pre requisites as completed
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True