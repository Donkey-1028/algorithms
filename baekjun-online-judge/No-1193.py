"""
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은
지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

첫째 줄에 분수를 출력한다.

입력
14
출력
2/4
"""

number = int(input())

index = 1  # 증가값에 의해 더해지는 수
add = 1  # 계차수열의 증가값
value = 0  # 계차수열의 값과 입력한 값의 차이를 담기 위한 변수
while True:
    if number == 1:
        print(1, '/', 1)
        break
    else:
        add += 1  # 2, 3, 4, 5 '''. 즉 증가값이 1 씩 올라간다
        index += add  # 증가값을 현재값에 더한다.

        if index >= number:  # 입력한 값이 계차수열의 값보다 커졌을때.
            value = index - number  # 입력한 숫자가 계차수열의 양쪽에서 몇번째인지 확인을 위한 변수
            if add % 2 == 0:
                print('%d/%d' % (add-value, 1+value))  # 계차수열이 홀수면 left값 감소, right 증가
            else:
                print('%d/%d' % (1+value, add-value))  # 짝수면 그 반대.
            break
