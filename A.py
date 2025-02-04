r, c = map(int, input().split())
table = [input().strip() for _ in range(r)]
result = []

def get(x):
    words = []
    current = []
    for ch in x:
        if ch == '#':
            if len(current) >= 2:
                words.append(''.join(current))
            current = []
        else:
            current.append(ch)


    if len(current) >= 2:
        words.append(''.join(current))
    return words

for x in table:
    result.extend(get(x))

for j in range(c):
    vert = ''.join([table[i][j] for i in range(r)])
    result.extend(get(vert))


print(min(result))