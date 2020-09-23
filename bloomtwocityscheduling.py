"""
Leetcode 1029. Two City Scheduling
"""

# Notes
# input: 2d array of costs per person [fly to city a, fly to city b]
# output: num - sum of MIN cost to fly EVERYONE out

def twoCitySchedCost(costs):
        min_cost = 0
        
        for cost in costs:
            cityA, cityB = cost
            print('cityA', cityA)
            print('cityB', cityB)
            min_cost += min(cityA, cityB)
            print('cheaper city', min(cityA, cityB))
            print(min_cost)
            
        return min_cost

costs1 = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# expect - 1859; initial sol'n output: 1706

print(twoCitySchedCost(costs1))