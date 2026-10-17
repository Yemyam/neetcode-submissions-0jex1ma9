class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # iterate through the gas stations, if gas becomes negative then update the starting gas station to the one we're at
        # track total gas to determine if a solution is even possible at all
        curr_gas = 0
        total_gas = 0
        start = 0
        for i in range(len(gas)):
            if curr_gas < 0:
                start = i
                curr_gas = 0
            curr_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
        if total_gas < 0:
            return -1
        return start