# Python3 program to sort an array
# using bucket sort
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b

def bucket_sort(arr):

    bucket = []

    for i in range(10):
        bucket.append([])
    # print(bucket)

    for j in arr: # .23
        index = int(10 * j) # 10 x .23 = 2.3 = 2
        bucket[index].append(j) # bucket[2].append(.23)
    # print(bucket)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    # print(bucket)

    # Get the sorted elements
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k = k + 1
    return arr

x = [0.897, 0.565, 0.656,
    0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucket_sort(x))

