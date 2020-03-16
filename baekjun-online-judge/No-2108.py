"""
수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다.
입력되는 정수의 절댓값은 4,000을 넘지 않는다.

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

입력
5
1
3
8
-2
2
출력
2
2
1
10
"""
import sys


loop = int(input())
list_ = []
for _ in range(loop):
    number = int(sys.stdin.readline())
    list_.append(number)


def average(li):
    # 평균을 구하기
    return round(sum(li) / len(li))


def find_center_value(li):
    # 중앙값 구하기
    # 정렬후 리스트의 길이에 절반에 해당되는 요소값 리턴
    li.sort()
    return li[(len(li)-1) // 2]


def count_number(li):
    # 숫자의 빈도수 구하기
    # 카운팅 정렬을 이용하였음.
    # 카운팅 되는 인덱스들은 0, -4000, -3999, ... 1, 2, 3 ... 4000
    count_list = [0] * 8001
    for index, value in enumerate(li):
        if value >= 0:
            count_list[value+4000] += 1
        else:
            count_list[-(4001-value)] += 1
    count_list = [(index, value) for index, value in enumerate(count_list) if value == max(count_list)]
    if len(count_list) > 1:
        # 만약 최대 빈도수의 값들이 여러개일 경우에는
        # 두번째에 오는 값.
        return count_list[1][0] - 4000
    else:
        return count_list[0][0] - 4000


def max_min(li):
    # 최대와 최소 값의 차이.
    if len(li) == 1:
        return 0
    return max(li) - min(li)


print(average(list_))
print(find_center_value(list_))
print(count_number(list_))
print(max_min(list_))
