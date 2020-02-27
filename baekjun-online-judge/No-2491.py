croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for index, value in enumerate(croatia_alpha):
    word = word.replace(value, '@')

print(len(word))
