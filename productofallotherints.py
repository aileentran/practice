# input: list of ints
# output: list of ints - each num is a product of all other nums

def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products

    if len(int_list) < 2:
        raise ValueError('Need at least 2 numbers in list!')


print(get_products_of_all_ints_except_at_index([1, 2, 3])) 
#[6, 3, 2]
print(get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])) 
#[120, 480, 240, 320, 960, 192]
print(get_products_of_all_ints_except_at_index([6, 2, 0, 3])) 
#[0, 0, 36, 0]
print(get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
# [0, 0, 0, 0, 0]
print(get_products_of_all_ints_except_at_index([-3, 8, 4])) 
#[32, -12, -24]
print(get_products_of_all_ints_except_at_index([-7, -1, -4, -2]))
#[-8, -56, -14, -28]
# account for inputs w/1 or less ints
# print(get_products_of_all_ints_except_at_index([]))
# print(get_products_of_all_ints_except_at_index([1]))