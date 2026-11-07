class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each candidate is a binary decision, we can choose to include it in the output or exclude it
        # in order to avoid duplicate outputs if we decide to not take a candidate, we want to skip 
        # all future instances of that candidate, or we might add a duplicate combination
        candidates.sort()
        out = []
        curr = []

        def backtrack(i, curr, total):
            if total == target:
                out.append(curr.copy())
                return
            elif i >= len(candidates):
                return
            elif total > target:
                return
            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr.pop()
            backtrack(i + 1, curr, total)
        
        backtrack(0, curr, 0)
        return out
