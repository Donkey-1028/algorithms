"""
최대 수익을 구하는 알고리즘

가장 가격이 낮을때 구매하여
가장 높을때 판매하면 얼마의 이익이 남는지
계산하는 알고리즘
"""


def max_profit(n):
    min_value = n[0]
    max_value = n[0]
    for index, value in enumerate(n):
        if min_value > value:
            min_value = value
            max_value = 0
        elif value > max_value:
            max_value = value
    return max_value - min_value


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
