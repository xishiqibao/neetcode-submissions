class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for tar, pre in prerequisites:
            preMap[tar].append(pre)

        Visited = set()

        def dfs(tar):
            if tar in Visited:
                return False
            if preMap[tar] == []:
                return True

            Visited.add(tar)

            for pre in preMap[tar]:
                if not dfs(pre):
                    return False

            Visited.remove(tar)
            preMap[tar] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True