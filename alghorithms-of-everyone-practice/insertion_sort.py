"""
삽입 정렬
"""


def insertion_sort(data):
    for index, value in enumerate(data):
        while index - 1 >= 0 and data[index-1] > value:
            """ 현재의 요소값보다 앞에 있는 요소들을 순회하는데, 만약 현재 요소가 앞의 요소보다 크다면
            그 인덱스 자리에 value가 들어가야 하기 때문에 while문 정지."""
            data[index] = data[index-1]
            index -= 1
        data[index] = value


list_ = [2, 4, 3, 5, 1]
insertion_sort(list_)
print(list_)
