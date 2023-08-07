from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = 0
        min_net = 0
        i_min_net = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            net += g - c
            if net < min_net:
                min_net = net
                i_min_net = i

        if net < 0:
            return -1
        elif min_net == 0:
            return 0
        else:
            return i_min_net + 1


print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
print(Solution().canCompleteCircuit(gas=[11, 4, 7, 1, 0], cost=[2, 5, 5, 9, 1]))
