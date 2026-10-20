class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            if triplets[0] == target:
                return True
            return False
        # we are checking if there exists triplets such that each element matches
        possible = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                possible = [max(possible[0], t[0]), max(possible[1], t[1]), max(possible[2], t[2])]
        if possible == target:
            return True
        return False

