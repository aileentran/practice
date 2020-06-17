# input: list of ints, always has at least 3 ints!
# output: int - highest product from 3 ints!

def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    
    # catching lists with less than 3 ints!
    if len(list_of_ints) < 3:
        raise ValueError('Whoopsidoodle! Need at least 3 ints!')


    # ints = []
    product = 1

    i = 1

    while i <= 3:

        largest = max(list_of_ints)
        idx = list_of_ints.index(largest)
        largest = list_of_ints.pop(idx)
        product *= largest
        # ints.append(largest)

        i += 1

    # product = 1

    # for num in ints:
    #     product *= num

    return product

print(highest_product_of_3([1, 2, 3, 4])) #24
print(highest_product_of_3([6, 1, 3, 5, 7, 8, 2])) #336
print(highest_product_of_3([-5, 4, 8, 2, 3])) #96
print(highest_product_of_3([-10, 1, 3, 2, -10])) #300
print(highest_product_of_3([-5, -1, -3, -2])) #-6
# also need account for lists < 3 nums
# print(highest_product_of_3([]))
# print(highest_product_of_3([1]))