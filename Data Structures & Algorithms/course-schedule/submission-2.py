class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the adjency list    
        adj = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)


        seen = set()
        def dfs(course):
            if course in seen: 
                return False
            
    
            seen.add(course)
            
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False

            adj[course] = []
            seen.remove(course)
            return True



        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True