"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

각 테스트 케이스마다 A+B를 출력한다.

5
1 1
2 3
3 4
9 8
5 2
예제 출력
2
5
7
17
7
"""

loop = int(input())


def add_generator():
    while True:
        number1, number2 = map(int, input().split(' '))
        yield number1 + number2


result = []
it = add_generator()

for i in range(loop):
    sum_value = next(it)
    result.append(sum_value)

for _, value in enumerate(result):
    print(value)
