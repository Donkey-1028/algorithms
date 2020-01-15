"""
미로찾기
그래프탐색을 이용
"""

maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}


def maze_solution(maze, start, end):
    qu = []
    solution = set()

    qu.append(start)
    solution.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for i in maze[v]:
            if i not in solution:
                qu.append(p + i)
                solution.add(i)

    return "?"


print(maze_solution(maze, 'a', 'p'))
