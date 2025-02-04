n, b = map(int, input().split())
a = list(map(int, input().split()))
position = a.index(b)

left_even = {}
left_odd = {}
right_even = {}
right_odd = {}
left_even[0] = 1
right_even[0] = 1

current_balance = 0
current_balance_r = 0

steps_r = 0
steps = 0

result = 0


for i in range(position - 1, -1, -1):
    steps += 1
    if a[i] < b:
        current_balance += 1
    else:
        current_balance -= 1
    if steps % 2 == 0:
        left_even[current_balance] = left_even.get(current_balance, 0) + 1
    else:
        left_odd[current_balance] = left_odd.get(current_balance, 0) + 1


for i in range(position + 1, n):
    steps_r += 1
    if a[i] < b:
        current_balance_r += 1
    else:
        current_balance_r -= 1
    if steps_r % 2 == 0:
        right_even[current_balance_r] = right_even.get(current_balance_r, 0) + 1
    else:
        right_odd[current_balance_r] = right_odd.get(current_balance_r, 0) + 1


for key in left_even:
    result += left_even[key] * right_even.get(-key, 0)

for key in left_odd:
    result += left_odd[key] * right_odd.get(-key, 0)

print(result)
