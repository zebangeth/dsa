class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        min_tank = float('inf')
        min_tank_idx = -1
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < min_tank:
                min_tank = tank
                min_tank_idx = i
        
        # 总油量小于总的消耗，无解
        if tank < 0:
            return -1
        return (min_tank_idx + 1) % len(gas)
