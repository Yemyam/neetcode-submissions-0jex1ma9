class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we can do dfs and store each course and its pre reqs in a hashmap
        pr = {c: [] for c in range(numCourses)}
        possible = set()
        # track which node we are at in order to detect any cycles
        visiting = set()
        for c, p in prerequisites:
            pr[c].append(p)

        def dfs(c):
            if c in possible:
                return True
            if c in visiting:
                return False
            visiting.add(c)
            for p in pr[c]:
                if not dfs(p):
                    return False
            possible.add(c)
            visiting.remove(c)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True




            
            
