"""
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

입력
110
출력
99

입력한 값 보다 작거나 같고 1보다 크거나 같은 수중 등차수열의 갯수를 구하기
"""

number = int(input())


def count_ap(n):
    count = 0
    for i in range(1, n+1):
        str_number = str(i)
        number_len = len(str_number)
        if number_len < 3:
            count += 1
        else:
            sum_diff = 0
            for index, value in enumerate(str_number):
                if index > 0:
                    diff = int(value) - int(str_number[index-1])
                    sum_diff += int(value) - int(str_number[index-1])
            if sum_diff / (number_len-1) == diff:
                count += 1
    return count


print(count_ap(number))
