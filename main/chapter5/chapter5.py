# chapter 5.4 条件执行
x = -1
if x > 10:
    print('x bigger than 10')
else:
    print('x smaller than 10')

if x > 0:
    pass
else:
    print('x is not pass')

# chapter 5.6 条件链
m = 10;
n = 20;
if m < n:
    print('m is less than n')
elif m > n:
    print('m is greater than n')
else:
    print('m equals to n')

# chapter 5.7 嵌套条件
if m < n:
    print('5.7 m is less than n')
else:
    if m > n:
        print('5.7 m is greater than n')
    else:
        print('5.7 m equals to n')

if m > 0 and m < n:
    print('m is positive and less than n')
if 0 < m < n:
    print('m is positive and less than n')

# chapter 5.11 键盘输入
text = input('what ... is your name? \n')
print(text)
