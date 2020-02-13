"""
두 번 이상 나온 이름 찾기
"""


def find_same_name(n):
    name_dict = {}
    for name in n:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    result = set()
    for index in name_dict:
        if name_dict[index] > 1:
            result.add(index)

    return result


name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Jerry"]
print(find_same_name(name2))
