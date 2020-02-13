"""
백준 2588번

세 자리수의 곱은 다음과 같은 과정을 통하여 이루어진다.
        472
    x   385
-----------------
       2360 ----(1)
      3776 ----(2)
     1416 ----(3)
-----------------
    181720 ----(4)

세 자리수 두개가 주어졌을 때 (3), (4), (5), (6) 위치에 들어가는 값을 구하는 프로그램을 작성
"""

num1 = int(input())
num2 = int(input())


def multiple_processing_generator(a, b):
    """간단한 문제지만 제너레이터 연습하고자 제너레이터로 만들었다."""
    multiple_list = list(str(b))  # 입력받은 두번 째 숫자의 각각의 자릿수를 리스트로 만듬.
    index = 1  # 리스트의 인덱스
    while True:
        if index > len(multiple_list):
            yield a * b
            return
        value = a * int(multiple_list[-index])  # 리스트의 뒷부분부터 접근해야 하기 때문에 -index
        index += 1
        yield value


multiple_processing = multiple_processing_generator(num1, num2)
print(next(multiple_processing))
print(next(multiple_processing))
print(next(multiple_processing))
print(next(multiple_processing))


