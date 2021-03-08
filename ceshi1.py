
# coding=utf-8
# 猜数字游戏 计算出一个1~100之间的随机数由人来猜，计算机跟进人猜的数字进行对比，给出提示大一点，小一点，如果猜对了则结束游戏

import random

num = random.randint(1, 100)
while True:
    try:
        user_guess = int(input("请输入您猜的数字： "))
    except ValueError:
        print("输入有误,请输入数字！")
        continue

    if user_guess > num:
        print("请试试小一点的数！")
        continue
    elif user_guess < num:
        print("请试试大一点的数！")
        continue
    else:
        print("猜对了！")
        break
