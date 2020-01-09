"""
삽입 정렬
"""


def insertion_sort(n):
    for index, value in enumerate(n):
        for i in range(index-1):
            if n[i] > value:
                temp = n[i]
                n[i] = n[index]
                n[index] = temp


t = [2, 4, 5, 1, 3]
insertion_sort(t)
print(t)