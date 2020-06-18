# input: list of ints
# output: list of ints - each num is a product of all other nums

# O(n^2) solution!
# def get_products_of_all_ints_except_at_index(int_list):

#     # Make a list with the products

#     if len(int_list) < 2:
#         raise ValueError('Need at least 2 numbers in list!')

#     result = []

#     i = 0

#     while i < len(int_list):
#         curr = int_list[i]
#         # print('curr', curr)

#         product = 1

#         k = 0

#         while k < len(int_list):
#             num = int_list[k]
#             # print('num', num)
            
#             if k != i:
#                 product *= num
#                 # print('product', product)
#             k += 1

#         result.append(product)

#         i += 1

#     return result


# O(n) time and space solution!
def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products

    if len(int_list) < 2:
        raise ValueError('Need at least 2 numbers in list!')

    before = []
    
    b_product = 1

    for num in int_list:
        print(num)

        before.append(b_product)
        b_product *= num

    before.append(b_product)

    print(before)

    # to get product AFTER the index, reverse before


print(get_products_of_all_ints_except_at_index([1, 2, 3])) 
#[6, 3, 2]
print(get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])) 
#[120, 480, 240, 320, 960, 192]
print(get_products_of_all_ints_except_at_index([6, 2, 0, 3])) 
#[0, 0, 36, 0]
print(get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0]))
# [0, 0, 0, 0, 0]
print(get_products_of_all_ints_except_at_index([-3, 8, 4])) 
#[32, -12, -24]
print(get_products_of_all_ints_except_at_index([-7, -1, -4, -2]))
[-8, -56, -14, -28]
# account for inputs w/1 or less ints
# print(get_products_of_all_ints_except_at_index([]))
# print(get_products_of_all_ints_except_at_index([1]))