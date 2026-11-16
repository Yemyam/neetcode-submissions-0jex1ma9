class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # the first character must always be an open bracket
        # after we place the first open bracket at each new bracket we are choosing if we should close off an existing bracket, or if we should open a new one, we can only add a closed bracket if there is currently an unclosed open bracket
        out = []
        curr = "("
        def backtrack(i, curr, open_num):
            if i >= n * 2:
                if open_num == 0:
                    out.append(curr[:])
                return
            if open_num > 0:
                curr += ")"
                backtrack(i + 1, curr, open_num - 1)
                curr = curr[:-1]
            curr += "("
            backtrack(i + 1, curr, open_num + 1)
        backtrack(1, curr, 1)
        return out