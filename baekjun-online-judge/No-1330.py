"""
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

1 2 가 입력 값일 경우 < 출력
10 2 가 입력 값일 경우 > 출력
5 5 가 입력 값일 경우 == 출력
"""

left_number, right_number = map(int, input().split(' '))
if left_number > right_number:
    print('>')
elif left_number < right_number:
    print('<')
else:
    print('==')
