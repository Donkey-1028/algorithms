"""
선택 정렬

리스트 [2, 4, 5, 1, 3] 을 정렬해보자.
"""

list_ = [2, 4, 5, 1, 3]


def selection_sort(data):
    data_len = len(data)
    for index, value in enumerate(data):
        min_value = value  # 최소값은 현재 인덱스의 값.
        for i in range(index+1, data_len):  # 현재 인덱스 다음인덱스부터 data의 길이까지 for loop
            if min_value > data[i]:
                min_value = data[i]
                min_index = i
        if min_value != value:  # 만약 현재 인덱스의 값이 최솟값이 아니면
            data[min_index] = value
            data[index] = min_value


selection_sort(list_)
print(list_)