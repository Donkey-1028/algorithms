"""
가짜 동전을 찾는 알고리즘
주어진 동전 N개 중에 무게가 다른 동전을 찾아내는 알고리즘.

출력 : 가짜 동전 번호
"""

def fake_coin(a, b, c, d):
    """
    a 에서 b 까지에 놓인 동전과 c 에서 d 까지에 놓인 동전의 무게를 비교
    a 에서 b 까지에 가짜 동전이 있으면 -1
    c 에서 d 까지에 가짜 동전이 있으면 1
    가짜 동전이 없으면 0
    """
    fake = 50
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0


def find_fake_coin(start, end):
    if start == end:
        return start

    center = (start + end) // 2
    fc1_left = start
    fc1_right = center
    fc2_left = center + 1
    fc2_right = end

    check = fake_coin(fc1_left, fc1_right, fc2_left, fc2_right)

    if check == -1:
        return find_fake_coin(fc1_left, fc1_right)
    elif check == 1:
        return find_fake_coin(fc2_left, fc2_right)

n = 100
print(find_fake_coin(0, n))
