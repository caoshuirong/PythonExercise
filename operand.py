# 一、优先级
'''
1.运算类  （ 算数运算类 > 按位运算）
2.值比较类
3.赋值类
4.判断类( 身份运算符 is > 成员运算符 in > 逻辑运算符（not and or））

'''
a = 3
b = 3
# 值比较
print(a == b)
# 身份判断
print( a is b)
# 类型判断
print(isinstance(a,int))







