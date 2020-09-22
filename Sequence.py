# 切片得到的一定是列表，按下标访问得到才是具体元素
tmp = list([1 ,2, 3,'looking'])
print(tmp[3:])
print(type(tmp[3:]))
print(tmp[3])
print(type(tmp[3]))
