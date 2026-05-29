class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cum_gas = [0] * len(gas)
        for i in range(len(gas)):
            cum_gas[i] = cum_gas[i - 1] + gas[i] - cost[i]
        
        start = cum_gas.index(min(cum_gas)) + 1
        cum_gas = [0] * len(gas)
        for i in range(len(gas)):
            pos = (start + i) % len(gas)
            cum_gas[pos] = cum_gas[pos - 1] + gas[pos] - cost[pos]
            if cum_gas[pos] < 0:
                return -1
        return start % len(gas)