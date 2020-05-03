"""
선택 정렬
"""

def sel_sort(data):
    list_len = len(data)

    for out_index in range(0, list_len):
        for in_index in range(out_index, list_len):
            if data[out_index] > data[in_index]:
                # 찾은 최솟값과 원래 비교하던 값의 자리를 바꿈
                data[out_index], data[in_index] = data[in_index], data[out_index]


list_ = [3, 44, 2, 1, 5]
sel_sort(list_)
print(list_)