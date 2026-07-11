class Solution(object):
    def twoCitySchedCost(self, costs):

        costs.sort(key=lambda x: x[1] - x[0])

        n = len(costs) // 2
        total = 0

        for i in range(n):
            total += costs[i][1]      # send to B

        for i in range(n, 2 * n):
            total += costs[i][0]      # send to A

        return total