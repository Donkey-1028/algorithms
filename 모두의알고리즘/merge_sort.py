"""
합병정렬
"""


def merge_sort(n):
    list_len = len(n)
    if list_len <= 1:
        return

    #리스트를 center 기준으로 나눔.
    center = list_len // 2
    first = n[:center]
    second = n[center:]

    #재귀를 통해 나눠진 리스트를 또 나눔. 결국 하나의 값만 들어있는 리스트로 됨.
    #하나의 값만 리스트로 나누어져도 결국 first 리스트와 second 리스트가 존재.
    merge_sort(first)
    merge_sort(second)

    n_index = 0
    first_index = 0
    second_index = 0

    #각각 하나의 값만 가진 리스트를 시작으로 하나의 리스트가 되도록 합병
    #리스트들의 길이만큼 해당 while문 진행.
    #first와 second 리스트의 값을 비교하여 작은값부터 차례대로 기존의 리스트에 대입
    while first_index < len(first) and second_index < len(second):
        if first[first_index] > second[second_index]:
            n[n_index] = second[second_index]
            n_index += 1
            second_index += 1
        else:
            n[n_index] = first[first_index]
            n_index += 1
            first_index += 1

    #second문보다 first문이 클 경우 남은값을 차례대로 기존의 리스트에 대입
    while first_index < len(first):
        n[n_index] = first[first_index]
        n_index += 1
        first_index += 1
    #이하동문
    while second_index < len(second):
        n[n_index] = second[second_index]
        n_index += 1
        second_index += 1


t = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(t)
print(t)