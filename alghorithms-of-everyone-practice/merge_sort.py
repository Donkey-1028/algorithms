"""
병합정렬
"""


def merge_sort(data):
    if len(data) <= 1:
        return

    center = len(data) // 2
    left = data[:center]
    right = data[center:]

    merge_sort(left)
    merge_sort(right)

    left_index = 0
    right_index = 0
    data_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            data[data_index] = right[right_index]
            data_index += 1
            right_index += 1
        else:
            data[data_index] = left[left_index]
            data_index += 1
            left_index += 1

    while right_index < len(right):
        data[data_index] = right[right_index]
        data_index += 1
        right_index += 1

    while left_index < len(left):
        data[data_index] = left[left_index]
        data_index += 1
        left_index += 1


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)