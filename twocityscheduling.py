"""
Leetcode - 1029. Two City Scheduling

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""
# Notes:
# input: array of costs - idx = a person; [cityA flight, cityB flight]
# output: number - minimum cost to fly every person to a city
# *half the people in city A; half in city B

# minimum cost variable to 0 
# list [cost difference, person's idx] --> sort that in descending order

# counter for city A, counter for city B half thepeople per city
# loop through cost difference list
# prioritize them n the cheaper city until a city is full
# push all the other people in the empty city
# while doing this, adding the flight cost to the minimum cost vairable

# outside the loop
# return the minimum cost
# talk time: 16 min

def twoCitySchedCost(costs):
    min_cost = 0 
    cost_diff = []

    for person, cost in enumerate(costs):
        flightA, flightB = cost
        diff = abs(flightA - flightB)
        cost_diff.append([diff, person])

    cost_diff.sort(reverse = True)
    
    cityA = len(costs) // 2
    cityB = len(costs) // 2

    for diff in cost_diff:
        price_diff, idx = diff 
        costA, costB = costs[idx]
        if (costA < costB and cityA > 0) or cityB == 0:
            cityA -= 1
            min_cost += costA
        else:
            cityB -= 1
            min_cost += costB

    return min_cost

# run time: O(n)
# run space: cost_diff -> n space; everything else is a constant; O(n)


costs1 = [[10,20],[30,200],[400,50],[30,20]] #expected: 110
costs2 = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]] # expected: 1859
costs3 = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]] # expected: 3086


print(twoCitySchedCost(costs3))




























# Notes and thoughts
# input: array of arrays - array[person] = [cityAflight, cityBflight]
# output: num - minimum cost
# HALF of people to city a, HALF to city b
# want to prioritize people with greatest cost difference to go to their cheapest city
# THEN fill in the rest of the slots with the other peeps

# having an empty minimum cost set to 0

# maybe have dictionary of each person[key] with their cost difference[value]
# can we.. sort a dictionary from greatest difference to least difference?

# OR array [cost diff, idx of person] and sort desending order based on cost difference
# loop through array
# get idx of person
# find cheapest city (keep track of.. how many people in that city)
# pop them in there 
# once a city fills up, just stick the rest in the other city :o 

def twoCitySchedCost1(costs):
    min_cost = 0
    difference = [] #[cost difference, idx of person]

    for person, flights in enumerate(costs):
        flight_A, flight_B = flights
        diff = abs(flight_A - flight_B)
        difference.append([diff, person])

    difference.sort(reverse = True)
    
    # space available in each city
    city_A = len(costs) // 2 
    city_B = len(costs) // 2

    for diff in difference:
        cost_diff, person = diff
        cost_A, cost_B = costs[person]
        # print('costA', cost_A)
        # print('costB', cost_B)
        # print('cityA', city_A)
        # print('cityB', city_B)
        if (cost_A < cost_B and city_A > 0) or city_B <= 0:
            # print('A is cheaper! OR no more room in city B')
            min_cost += cost_A
            city_A -= 1
        else:
            min_cost += cost_B
            city_B -= 1

        # print('min_cost', min_cost)
        # print('cityA', city_A)
        # print('cityB', city_B)
        # print('\n')

    return min_cost
