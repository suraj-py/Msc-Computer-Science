def maxSubArraySum(a,size):

    max_so_far = a[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
size = len(arr)
ans = maxSubArraySum(arr, size)
print(ans)
