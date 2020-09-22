
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

# 2.列表
list1 = [1,2]
list2 = [3,4,5]
print(list1+list2)
print(list1*3)
print(len(list1))
print(3 in list2)
print(max(list2))
print(min(list2))
del list2[1]
print(list2)
list2.append(1)
list2 = list2 + list1
del list2[1:3]
print(list2)
list2.insert(1,100)
print(list2)
list2.pop(2)
list2.remove(100)
print(list2)
list3 = list2.copy()
list4 = list2
list4.clear()
print(list2)
print(list3)
list3 = list3+[1,2,3,5,6,7]
list3.reverse()
print(list3)
# 默认非降序
# list.sort( key = None,reverse = false)
list3.sort()
print(list3)
list3.sort(reverse = True)
print(list3)
list4 = [[1,3,8,4],[0,5,6,7,8]]
def cmpDimension(x):
    return x[2]
list4.sort()
print("list4",list4)
