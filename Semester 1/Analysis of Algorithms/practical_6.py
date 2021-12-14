def counting_sort(A):
    # Step 1: make output arr of len(A)
    size = len(A)
    output = [0] * size

    # Step 2: make count array of lenght max+1
    m = max(A) + 1
    count = [0] * m

    # Step 3: store the count of each element in count array
    for i in range(size):
        count[A[i]] += 1

    # Step 4: calculate the cumilative sum of count array
    for i in range(1, m):
        count[i] += count[i-1]

    # Step 5: find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
        i -= 1

    # Step 6: copy elements from output array into original array
    A = output[:]
    return A

A = [7, 0, 3, 5, 1, 3, 4, 1, 2, 3, 0, 6]
ans = counting_sort(A)
print(ans)
