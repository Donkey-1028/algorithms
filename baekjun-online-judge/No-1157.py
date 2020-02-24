"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는
프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

입력
Mississipi
출력
?

입력
zZa
출력
Z

입력
z
출력
Z

입력
baaa
출력
A
"""
word = input()


def get_word(w):
    word_dict = {}
    for index, value in enumerate(w):
        value = value.lower()
        try:
            word_dict[value] += 1
        except:
            word_dict[value] = 1
    return word_dict


def find_max_word(d):
    max_count = sorted(d.values())
    if len(max_count) > 1:
        if max_count[-1] == max_count[-2]:
            print('?')
        else:
            for key, value in d.items():
                if value == max_count[-1]:
                    print(key.upper())
    else:
        print(word.upper())


find_max_word(get_word(word))
