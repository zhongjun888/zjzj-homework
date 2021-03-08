# -*- coding: utf-8 -*-

# for循环从1加到100求和
sum = 0
for i in range(1, 101):
    sum = sum + i

print('1～100 的和为%d' % sum)

# for循环从1加到100求偶数和
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i

print('1～100 的偶数和为%d' % sum)

# 直接for循环从1加到100求偶数和
sum = 0
for i in range(0, 101, 2):
    sum = sum + i
print('1～100 的偶数和为%d' % sum)
