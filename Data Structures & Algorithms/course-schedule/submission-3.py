class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjency list
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adj[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
