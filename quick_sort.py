"""
퀵정렬
Median of Three 방식
"""


def choice_pivot(arr, left, right):
    """
    리스트의 첫번째값, 마지막값, 가운데값중
    어떠한 값을 pivot 으로 이용할지 정렬하고 리턴
    """
    center = (left + right) // 2
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[center] > arr[right]:
        arr[center], arr[right] = arr[right], arr[center]
    if arr[left] > arr[center]:
        arr[left], arr[center] = arr[center], arr[left]
    return center


def quick_sort(arr, left, right, pivot_index):
    if right - left <= 0:
        return

    #pivot은 리스트의 Median of three를 이용하여 가운데로 설정.
    pivot = arr[pivot_index]
    j = left
    for i in range(left, right):
        #pivot을 기준으로 작으면 왼쪽, 크면 오른쪽에 정렬
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    #pivot을 기준으로 왼쪽으로 정렬된 리스트를 다시 퀵정렬 하기 위해 다음 pivot 설정
    next_min_pivot = choice_pivot(arr, left, pivot_index)
    #왼쪽으로 정렬된 리스트 퀵정렬
    quick_sort(arr, left, pivot_index, next_min_pivot)

    #pivot을 기준으로 오른쪽으로 정렬된 리스트를 다시 퀵정렬 하기 위해 다음 pivot 설정
    next_max_pivot = choice_pivot(arr, pivot_index+1, right)
    #오른쪽으로 정렬된 리스트 퀵정렬
    quick_sort(arr, pivot_index+1, right, next_max_pivot)


def sort(arr):
    pivot_index = choice_pivot(arr, 0, len(arr)-1)
    quick_sort(arr, 0, len(arr)-1, pivot_index)


t = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5, 11, 12]
sort(t)
print(t)