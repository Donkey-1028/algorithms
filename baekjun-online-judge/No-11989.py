"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오. (카운팅정렬)

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

입력
10
5
2
3
1
4
2
3
5
1
7
출력
1
1
2
2
3
3
4
5
5
7
"""
import sys


count = int(input())
list_ = [0] * 10001
for _ in range(count):
    number = int(sys.stdin.readline())
    list_[number] += 1


for index, value in enumerate(list_):
    if value != 0:
        for i in range(value):
            print(index)