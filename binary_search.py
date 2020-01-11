"""
이분탐색
"""


#f: 찾으려는 숫자, n: 리스트
#찾으려는 값이 없으면 -1 리턴
def binary_search(n, f):
    left = 0
    right = len(n)-1

    while left <= right:
        center = (left + right) // 2

        if f is n[center]:
            return center
        elif f > n[center]:
            left = center - 1
        else:
            right = center - 1
    return -1


t = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(t, 36))
print(binary_search(t, 2))
