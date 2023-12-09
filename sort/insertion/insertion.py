# for j = 2 to A.length
#     key = A[j]
#     // Insert A[j] into the sorted sequence A[1..j-1].
#     i = j - 1
#     while i > 0 and A[i] > key
#         A[i+1] = A[i]
#         i = i - 1
#     A[i+1] = key


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

numbers = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)