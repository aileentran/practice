"""
Leetcode 1029. Two City Scheduling
"""

# Notes
# input: 2d array of costs per person [fly to city a, fly to city b]
# output: num - sum of MIN cost to fly EVERYONE out
# HALF to city A, HALF to city b


# OOF. new thoughts. okay. 
# figure out cost difference between city A and city B for each person
# create an ordered list of tuples (cost difference, idx of person)
# OR in list, idx = idx of person, cost difference = value; any added benefits? take up less space?
# ^no. have to sort for largest cost difference and if sort = change idxs
# larger differences = prioritize to cheaper city up to half peeps -> helper function
# shuffle less difference to other city
def twoCitySchedCost(costs):
        min_cost = 0
        cityA_people = len(costs) // 2
        cityB_people = len(costs) // 2
        differences = []
        
#       create differences list (cost difference, idx)        
        for idx, cost in enumerate(costs):
            cityA, cityB = cost
            difference = abs(cityA - cityB)
            differences.append((difference, idx))
            
#         greatest difference at beginning
        differences.sort(reverse = True)
        # print(differences)
        
        for difference in differences:
            cost_difference, idx = difference
            # print('cost_difference', cost_difference)
            # print('idx', idx)
            
            costA, costB = costs[idx]
            # print('costA', costA)
            # print('costB', costB)
            if cityA_people > 0 and cityB_people > 0:
                if costA < costB:
                    cityA_people -= 1
                    min_cost += costA
                    continue
                else:
                    cityB_people -= 1
                    min_cost += costB
                    continue
            # print('cityA_people', cityA_people)
            # print('cityB_people', cityB_people)
            # print('min_cost', min_cost)
            # print('\n')
            
#             determine which city is full
            if cityA_people == 0 and cityB_people > cityA_people:
                # print('CITY A EMPTY')
                cityB_people -= 1
                min_cost += costB
            elif cityB_people == 0 and cityA_people > cityB_people:
                # print('CITY B EMPTY')
                min_cost += costA
                cityA_people -= 1
                
            # print('cityA_people', cityA_people)
            # print('cityB_people', cityB_people)
            # print('min_cost', min_cost)
            # print('\n')
            
            
        return min_cost


costs1 = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# expect - 1859; initial sol'n output: 1706

print(twoCitySchedCost(costs1))

####################################
# Initial attempt - look for cheapest flights period w/out 
"""
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

"""