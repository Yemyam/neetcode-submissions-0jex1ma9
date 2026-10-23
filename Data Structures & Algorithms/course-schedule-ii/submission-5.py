class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create an adjacency list prs
        prs = {c: [] for c in range(numCourses)}
        for c, pr in prerequisites:
            prs[c].append(pr)
        possible = set()
        visiting = set()
        out = []
        def dfs(c):
            # if a course has no pre reqs then it is possible, and we can add it to our course ordering
            if c in possible:
                return True
            if c in visiting:
                return False
            visiting.add(c)
            for pr in prs[c]:
                if not dfs(pr):
                    return False
            possible.add(c)
            out.append(c)
            visiting.remove(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return out
