"""
친구와 친밀도 구하기
"""

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Justin', 'Summer'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

def find_friend(n, first):
    qu = []
    # 자료형은 중복을 허용하지 않는다.
    result = set()

    qu.append((first, 0))
    result.add(first)

    while qu:
        p, d = qu.pop(0)
        print(p, d)
        for friend in n[p]:
            if friend not in result:
                result.add(friend)
                qu.append((friend, d+1))


find_friend(fr_info, 'Summer')
print()
find_friend(fr_info, 'Jerry')
