import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place
    i = 0

    while i < len(the_list):

    	ran = get_random(1, len(the_list))
    	ran_idx = the_list.index(ran)
    	new = the_list.pop(ran_idx)
    	the_list.insert(0, new)

    	i += 1

    return the_list

    




sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)