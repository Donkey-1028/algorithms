"""
이분 탐색
"""


def binary_search(data, number):
    start = 0
    end = len(data) - 1

    while end >= start:
        mid = (start + end) // 2

        if number == data[mid]:
            return mid
        elif number > data[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))