"""
회문 찾기
회문이면 True
아니면 False
"""


def reverse_generator(g):
    """
    제너레이터를 입력받아
    reversed 된 제너레이터로 리턴
    """
    return reversed(tuple(g))


def palindrome(n):
    # 입력받은 문자열중 문자일 경우 소문자로 제너레이터 표현식으로 할당
    alpha_lower_list = (x.lower() for x in n if x.isalpha())
    # 제너레이터를 역순으로 할당
    reverse_list = reverse_generator(alpha_lower_list)
    for _, word in enumerate(n):
        # 입력받은 문자가 문자일 경우
        if word.isalpha():
            # 입력받은 문자를 제너레이터와 비교
            if word.lower() != next(reverse_list):
                return False
    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
print(palindrome("abc."))

