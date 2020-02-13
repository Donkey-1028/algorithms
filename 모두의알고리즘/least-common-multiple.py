"""
입력받은 리스트에서 요소들의 최소 공배수 구하기
"""


def least(a, b):
    i = 1
    while True:
        if a * i % b == 0:
            return a * i
        else:
            i += 1


def solution(arr):
    temp = arr[0]
    for _, value in enumerate(arr, 1):
        temp = least(temp, value)
    return temp


arr = [2, 6, 8, 14]
print(solution(arr))


