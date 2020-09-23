
# 一、数字
# # 1.整数 int() 无限长
# # 3//3 = 1
# num = 128
# print(bin(num))
# print(oct(num))
# print(hex(num))
#
# # 2.布尔
# # 非空、非0都为True
# print(bool(num))
#
# # 3.浮点数,IEEE754双精度，保留小数点后6位即可
# print(float(num))

# 二、序列
# # 1.字符串
# # 1.1基本操作
str1 = "hello world"
str2 = '!'
# print(str1+str2)
# print(str1*3)
# # 原生字符串，相当于每个\前面自动加一个\
# print(r"c:\northwest")
# # 切片。【起点：终点[：步长]】
# print(str1[1:8:2])
# # 判断子串
# if 'hell' in str1:
#     print("yes")
# 1.2相关函数
# tmp = len(str1)
# print(tmp)
# print(str(192.128))
# print(chr(0x41),ord('A'))
# print(str1.upper(),str2.lower())
# print(str1.count('lo'))
# print(str1.replace('hell','tw'))
# print("%d + %d = %d" % (3,4,7))
# print("01".rjust(10,'0'))

# # 2.列表
# list1 = [1,2]
# list2 = [3,4,5]
# print(list1+list2)
# print(list1*3)
# print(len(list1))
# print(3 in list2)
# print(max(list2))
# print(min(list2))
# del list2[1]
# print(list2)
# list2.append(1)
# list2 = list2 + list1
# del list2[1:3]
# list2 =[1,2,3,4]
# list2.extend([5,6,7,8,9])
# print(list2)
# print(list2)
# list2.insert(1,100)
# print(list2)
# list2.pop(2)
# list2.remove(100)
# print(list2)
# list3 = list2.copy()
# list4 = list2
# list4.clear()
# print(list2)
# print(list3)
# list3 = list3+[1,2,3,5,6,7]
# list3.reverse()
# print(list3)
# # 默认非降序
# # list.sort( key = None,reverse = false)
# list3.sort()
# print(list3)
# list3.sort(reverse = True)
# print(list3)
list4 = [[1,3,8,4],[0,5,6,7,8]]
# # 返回比较维度
# def cmpDimension(x):
#     return x[2]
# list4.sort(key = cmpDimension)
# print("list4",list4)
# print(sorted(list4,key = cmpDimension))

# # 3.元组
# mytuple = (1,2,3,4,5,6,7,8,9)
# print(mytuple[0:8:2])
#
# mytuple = mytuple + (3,4)
# print(mytuple*3)
#
# print(len(mytuple))
# print(sorted(mytuple))
# for i in reversed("mystring"):
#     print(i,end = '')
#
# # 二、无序
# # 1.集合
# mySet = {1,2,3,4,5}
# print(len(mySet))
# if 1 in mySet:
#     print('Yes')
# print(sum(mySet))
# print(mySet | {1,2,3,8,0,9})
# print(mySet & {1,2,3})
# print(mySet - {1,2,3})
# print(mySet ^ {1,2,3,9,0})
# mySet.add(-1)
# print(mySet)
# if -1 in mySet:
#     mySet.remove(-1)
#     print(mySet)

# # 2.字典
# myDict = {'Y':1,'R':2,"W":3}
# print(len(myDict))
# for v in myDict.keys():
#     print(v,end = ' ')
# print(end = '\n')
# for v in myDict.values():
#     print(v)
# for v in myDict.items():
#     print(v)
# del myDict['Y']
# print(myDict['W'])
# str1 = 'Q'
# if myDict.get(str1,None) == None:
#     print("Can't find the key %s" % str1)
# print(myDict.pop("W",None))
# print(myDict)
# list1 = [1,2,3]
# list2 = ['a','b','c']
# for i in range(3):
#     myDict[list1[i]] = list2[i]
# print(myDict)



