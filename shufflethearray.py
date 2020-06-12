# input: array, n = int
# output: array

# n = x1, x2, ... xn, y1, y2, ... yn
# output: x1, y1, etc. 

def shuffle(nums, n):
    x = nums[:n]
    y = nums[n:]

    s = []

    i = 0

    while i < n:
        s.append(x[i])
        s.append(y[i])

        i += 1

    return s


print(shuffle([2,5,1,3,4,7], 3)) #[2,3,5,4,1,7]
print(shuffle([1,2,3,4,4,3,2,1], 4)) #[1,4,2,3,3,2,4,1]
print(shuffle([1,1,2,2], 2)) #[1,2,1,2]