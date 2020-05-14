"""
input: 3 lists - takout, dinein, served
output: boolean - True if served is in first-come first serve order!

ints values are arbitrary

"""

# out of order
oo_takeout = [1, 3, 5]
oo_dinein = [2, 4, 6]
oo_served = [1, 2, 4, 6, 5, 3]

# in order
in_takeout = [17, 8, 24]
in_dinein = [12, 19, 2]
in_served = [17, 8, 12, 19, 24, 2]

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served

    for served in served_orders:
        # checking if anything is queued up for both takeout and dinein
        if len(take_out_orders) > 0:
            first_takeout = take_out_orders[0]
        else:
            first_takeout = None

        if len(dine_in_orders) > 0:
            first_dinein = dine_in_orders[0]
        else:
            first_dinein = None

        # check order of served vs queues 
        if (served == first_takeout):
            take_out_orders.remove(first_takeout)
        elif (served == first_dinein):
            dine_in_orders.remove(first_dinein)
        else:
            return False

    # orders still unfulfilled
    if len(take_out_orders) > 0 or len(dine_in_orders) > 0:
        return False

    return True

print(is_first_come_first_served(oo_takeout, oo_dinein, oo_served)) #False
print(is_first_come_first_served(in_takeout, in_dinein, in_served)) #True