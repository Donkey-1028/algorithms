"""
학생 번호로 학생이름 찾기
"""

students = {39: 'Justin', 14: 'John', 67: 'Mike', 105: 'Summer'}


def find_student(students, grade):
    try:
        name = students[grade]
    except KeyError:
        return '?'
    else:
        return name


n = int(input("학번을 입력하세요 : "))
print(find_student(students, n))
