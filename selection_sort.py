"""
선택정렬.
입력: 리스트 a
출력: 정렬된 새 리스트
주어진 리스트에서 최솟값의 위치를 돌려주는 함수
"""


def find_min(n):
    for index, value in enumerate(n):
        if value is min(n):
            return index


def sort(n):
    result = []
    while n:
        min_num = n.pop(find_min(n))
        result.append(min_num)
    return result


t = [3, 4, 2, 1, 5]
print(sort(t))