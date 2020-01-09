"""
병합정렬
"""


def merge_sort(n):
    list_len = len(n)
    if list_len <= 1:
        return

    center = list_len // 2
    first = n[:center]
    second = n[center:]

    merge_sort(first)
    merge_sort(second)

    n_index = 0
    first_index = 0
    second_index = 0

    while first_index < len(first) and second_index < len(second):
        if first[first_index] > second[second_index]:
            n[n_index] = second[second_index]
            n_index += 1
            second_index += 1
        else:
            n[n_index] = first[first_index]
            n_index += 1
            first_index += 1

    while first_index < len(first):
        n[n_index] = first[first_index]
        n_index += 1
        first_index += 1
    while second_index < len(second):
        n[n_index] = second[second_index]
        n_index += 1
        second_index += 1


t = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(t)
print(t)