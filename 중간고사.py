x = 3.141592
print(int(x))

a = 17 // 4
b = 17 % 4
print(a, b)

a = 100
b = '200'
print(int(a) + int(b))

print('python', 'java', sep='-', end='!!')
print('C++')

score = 85
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')

total = 0
for i in range(1, 6):
    if i % 2 == 0:
        continue
    total += i
print(total)

s = 'pythonPrograming'
print(s[:6].upper())

data = [10, 500, 20, 30]
print(data)


student = {'name': '김철수', 'age': 20}
print(student.get('major', '컴퓨터공학'))

count = 0
n = 10
while n > 0:
    if n % 3 == 0:
        count += 1
    if n == 4:
        break
    n -= 1
print(count)

x = 5
result = 'pass' if x >= 10 and x % 2 == 1 else 'Fail'
print(result)

text = 'python programming'
result = text.strip().upper().replace('PYTHON', 'AI')
print(result)

nuters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x*2 for x in nuters if x % 2 == 0]
print(even_squares)

def func(*args, **kwargs):
    return len(args) + len(kwargs)
print(func(1, 2, 3, a=4, b=5))

g_var = 10
def update_var():
    global g_var
    g_var += 5
    return g_var
update_var()
print(g_var)

import copy
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 99
print(a[0][0], b[0][0])
