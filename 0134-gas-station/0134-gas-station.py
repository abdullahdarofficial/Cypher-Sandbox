class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # for start in range(len(gas)):

        #     i = start
        #     currgas = 0
        #     first = True
        #     while currgas > 0 and i != start or first:
        #         first = False
        #         currgas += gas[i] - cost[i]
        #         i+=1
        #         if i == len(gas):
        #             i = 0
            
        #     if i == start and first == False and currgas >= 0:
        #         return start

        # return -1

        total_cost = 0
        total_gas = 0
        tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_cost += cost[i]
            total_gas += gas[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start_index = i + 1
                tank = 0
        return start_index if total_gas >= total_cost else -1


