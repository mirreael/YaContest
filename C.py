n = int(input().strip())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
stack = []

position = [0] * (n + 1)
for i, value in enumerate(a):
    position[value] = i

func_f = [0] * (n + 1)
func_g = [0] * (n + 1)

included = [1] * (n + 1)
count_f = [0] * (n + 1)
count_g = [0] * (n + 1)

for x in range(1, n + 1):
    i = position[x]
    func_f[x] = b[i]
    func_g[x] = c[i]


for x in range(1, n + 1):
    count_f[func_f[x]] += 1
    count_g[func_g[x]] += 1

for x in range(1, n + 1):
    if count_f[x] == 0 or count_g[x] == 0:
        stack.append(x)



while stack:
    x = stack.pop()
    if included[x] == 0:
        continue
    included[x] = 0
    fx = func_f[x]
    gx = func_g[x]
    count_f[fx] -= 1
    count_g[gx] -= 1
    if included[fx] == 1 and count_f[fx] == 0:
        stack.append(fx)
    if included[gx] == 1 and count_g[gx] == 0:
        stack.append(gx)

result = sum(included[1:])


print(n - result)
