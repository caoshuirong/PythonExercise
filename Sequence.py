
# chapter1 输入输出
count = 0
while True:
    try:
        # cinStr = input()
        # cinList = cinStr.split()
        # a,b = map(int , cinList)
        a,b = map(int,input().split())
        c = a + b
        count += 1
        print("case%d: %d" % (count,c))
        # rjust 右对齐，第一个参数为总输出宽度，第二个参数是一个填充字符。字符！！！
        print(("%d" % count).rjust(10,'0'))
    except:
        break











# 数字
# 1.整数 int() 无限长  2//2 = 1











# 切片得到的一定是列表，按下标访问得到才是具体元素
# tmp = list([1 ,2, 3,'looking'])
# print(tmp[3:])
# print(type(tmp[3:]))
# print(tmp[3])
# print(type(tmp[3]))

