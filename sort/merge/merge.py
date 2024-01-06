def merge(inputs: list, start: int, mid: int, end: int) -> list:
    left = inputs[start:mid+1]
    right = inputs[mid+1:end+1]

    left.append(float("inf"))
    right.append(float("inf"))

    left_index = right_index = 0
    for output_index in range(start, end+1):
        if left[left_index] <= right[right_index]:
            inputs[output_index] = left[left_index]
            left_index += 1
        else:
            inputs[output_index] = right[right_index]
            right_index += 1

    return inputs


def merge_sort(inputs: list, start: int, end: int) -> list:
    if start < end:
        mid = (start + end) // 2
        merge_sort(inputs, start, mid)
        merge_sort(inputs, mid+1, end)
        merge(inputs, start, mid, end)

    return inputs    


numbers = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_numbers = merge_sort(numbers, 0, len(numbers) - 1)
print(sorted_numbers)