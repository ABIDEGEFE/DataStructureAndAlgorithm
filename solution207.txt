class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = {i: [] for i in range(numCourses)}
        for second, first in prerequisites:
            graph[first].append(second)
        visited = [0] * numCourses

        def hasCircle(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True

            visited[course] = 1

            for crs in graph[course]:
                if not hasCircle(crs):
                    return False

            visited[course] = 2
            return True

        for course in range(numCourses):
            if not hasCircle(course):
                return False

        return True
      
      
        