"""
Leetcode 1029. Two City Scheduling
"""

# Notes
# input: 2d array of costs per person [fly to city a, fly to city b]
# output: num - sum of MIN cost to fly EVERYONE out

def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        
        for cost in costs:
            cityA, cityB = cost
            print('cityA', cityA)
            print('cityB', cityB)
            min_cost += min(cityA, cityB)
            
        return min_cost
