"""
리스트에서 특정 숫자의 위치 찾기
입력 : 리스트 a, 찾는 값 x
출력 : 찾으면 위치, 못하면 -1
"""


def search_list(a , x):
    for index, value in enumerate(a):
        if value is x:
            return index

    return -1


t = [19, 2, 3, 4, 50, 1]
print(search_list(t, 50))
print(search_list(t, 100))