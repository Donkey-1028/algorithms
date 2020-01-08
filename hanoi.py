"""
하노이의 탑
입력 : 옮기려는 원반의 갯수 N
    옮길 원반이 현재 있는 출발점 기둥 start
    원반을 옮길 도착점 기둥 end
    중간 기둥 center
출력 : 원반을 옮기는 순서
"""


def hanoi(n, start, end, center):
    if n is 1:
        print(start, '>', end)
        return
    hanoi(n-1, start, center, end)
    print(start, '>', end)
    hanoi(n-1, center, end, start)


n = int(input('원반 갯수를 입력하세요 : '))
hanoi(n, 1, 3, 2)