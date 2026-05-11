class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_level = 0
        min_gas_level = float('inf')
        min_gas_position = 0
        for i in range(len(gas)):
            gas_level += gas[i] - cost[i]
            if gas_level < min_gas_level:
                min_gas_level = gas_level
                min_gas_position = i
        
        i = min_gas_position + 1
        gas_level = 0
        while i < min_gas_position + 1 + len(gas):
            
            j = i % len(gas)
            gas_level += gas[j] - cost[j]
            print(j, gas_level)
            if gas_level < 0:
                return -1
            i += 1
            
        return (min_gas_position + 1) % len(gas)