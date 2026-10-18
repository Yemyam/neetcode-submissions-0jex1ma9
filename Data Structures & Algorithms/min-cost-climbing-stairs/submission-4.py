class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # construct an array in reverse order which represents the cheapest cost to the end of the stair case at each index. The min cost of each i is cost[i] + min(cost[i - 1], cost[i - 2])
        min_cost = [0] * len(cost)
        min_cost[0] = cost[-1]
        min_cost[1] = cost[-2]
        if len(cost) == 2:
            return min(cost)
        cost = cost[::-1]
        for i in range(2, len(min_cost)):
            min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
        print(min_cost)
        return min(min_cost[-1], min_cost[-2])