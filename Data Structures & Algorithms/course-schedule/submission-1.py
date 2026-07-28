class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Turn the prereq list into a map: course -> list of prerequisites
        pre_map = {n : [] for n in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)


        visitSet = set()


        def dfs(course):
            # Have we already visited this node? if yes -> loop -> return False
            if course in visitSet:
                return False

            if pre_map[course] == []:
                return True

            # We are visiting this node for the first time, add it to the set
            visitSet.add(course)

            for pre in pre_map[course]:
                if not dfs(pre):
                    return False

            visitSet.remove(course)
            pre_map[course] = []
            return True
            



        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True