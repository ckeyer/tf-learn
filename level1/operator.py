#!/usr/bin/env python3


print(9 / 4)
print(9 // 4)
print(2.33 // 1)

for x in (1, 2, 3):
    print(x,)
for x in (1, 2, 3):
    print(x)


thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
thisset2 = ("Google", "Runoob", "Taobao")
print(thisset2)


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        break

print('')
