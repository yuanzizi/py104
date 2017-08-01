# -------ex11 ex12输入 -------------
print("How old are you?",end=" ")  #python3 不换行，用空格结束
age = input()
print("How tall are you?",end=" ")
height = input()
print("So,you're {} old, {} tall.".format(age,repr(height)))
# repr() 直接输出原始值，适合debug

age = input("How old are you?")
# 加分作业
# 在python 命令行 help(input) 可以查看语法解释
# windows 下没有pydoc
