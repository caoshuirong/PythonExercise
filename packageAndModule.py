# The organization architecture of python includes package , module and class.
# package = folder + initial module(__init__.py)
# module is similar to file
# import 通常用来导入同一个命名空间下的模块，或者子包内的模块。
# 同一个包内为同一个命名空间。避免名字重复的模块，调用时发生冲突
import flowControl
import subPackage.c1

def func(
        a,
        *b
        ):
    pass
