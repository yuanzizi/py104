# ----------ex1----------------------------------------
print("Hello World~!")
print("中文 您好~！")  # 中文的打印也都没有问题

# ----------ex2 注释符 ---------------------------------

print("注释符 # 在字符串里面") #输出 注释符 # 在字符串里面


# ---------ex3 数学计算---------------------------------

print("(2+3*5)/4  = ",(2+3*5)/4) # 输出 (2+3*5)/4=? 4.25
# 逻辑计算
print(3+2 <= 5-7) # 输出 False

# python 也能在命令行当计算器用

# ---------ex4 变量 -----------------------------------
# python 的变量定义是自动赋予类型的

name = "Eric Chi"
cars = 100
drivers = 20
space_in_a_car = 4.0
cars_not_driven = cars - drivers

print(name,"has",cars,"cars and ",drivers,"drivers")
# 浮点计算结果还是浮点
print("Every day transfer", space_in_a_car*cars," peoples")

#------ ex5 格式化打印 ----------------------------------
print(round(2.54990)) # round()四舍五入 取整函数

print(f"My name is {name}.") # 变量名通过 {} 引用
print(f"I have {cars} cars.")
print(f"Every day tranfer {space_in_a_car}*{cars} peoples")
peoples_tranfer = space_in_a_car * cars
print(f"Every day tranfer {peoples_tranfer} peoples")

# ----- ex6 高级格式化打印 ---------------------------------

x = f"My name is {name}."
y = f"I have {cars} cars."
print(x) # 直接打印 字符串变量
print(f"This is in ex6: {x}")
print(x + y)
print("I write a '单引号' 特殊字符!@#$%^&* in double-quote string") #单双引号都是代表字符串
print('I write a "双引号" 特殊字符!@#$%^&* in single-quote string')

print("I write a \"\" in double-qutoe string。") # 可以通过 \ 来转义字符


# ----- ex7，ex8 ，ex9高级格式化打印2 ------------------------------
print("It's fleece was white as {}.".format('snow'))
snow = 'SNOW'
print("It's fleece was white as {}.".format(snow))# {}代表一个参数，在后面进行传参

# 在字符串中多个{}参数,通过format() 来顺序传递
print("It's fleece was white as {} & {}".format((snow),'snow'))

formatter = "1:{} 2:{} 3:{} 4:{}"
print(formatter.format(1,2,3,4))
print(formatter.format(True,False,True,False)) # True False 代笔一个布尔值
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "这是第一行",
    "No 2",
    "No 3",
    "No 4"
))

# 打印特殊格式
print(x,"\n",y )
### 为何会"\n"下一行多一个空格？？？
### 如果用 + 而不是 ， 就不会多个空格，
### print()函数的 ，会自动多个空格么？

### My name is Eric Chi.
### I have 100 cars.
print(x+"\n"+y)

# 3个双引号(单引号) 可以把一大段字符串按照本来的格式输出
print("""
    这是一大堆字符串，
      我在这里换行了~！
    这里结束。
    """)

print("\t 这里加了\\t转义符~！")

for i in ["/","-","|","\\","|"]:
    print("{}".format(i))
    print("{}\n".format(i))
    print("\t{}".format(i))
