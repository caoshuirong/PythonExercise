# if
condition = False
if condition:
    pass
elif condition:
    pass
else:
    pass

# while 用于次数不定的情况
while True:
    break

# for 常用于遍历和次数控制
# 1.遍历
myList = list(range(32))
for v in myList:
    print(v,end = ' ')
print(end = '\n')

# 2.次数控制
count = 0
for i in range(21,10,-1):
    print(i,end = ' ')
    count += 1
print('\n',count,end = '\n')

# range 的使用，返回的是可迭代的range对象
start = 0
end_next = 101 # 不用管加减，知道是最后一个元素的下一个就可以
step = 50
print(type(range(start,end_next,step)))

