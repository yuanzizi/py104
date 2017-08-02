# --- ex18 函数 ----------------
def print_chengfabiao(argv1):
    for i in range(argv1+1):
        for j in range(i+1):
            print("{}*{}={}".format(j,i,j*i),end='  ')
        print("")

num = input("请输入乘法表的数值：")
print_chengfabiao(int(num))

# --- ex20 ----------------
def copy_file(from_file,to_file):
    with open(to_file,'w') as f:
        f.write(open(from_file).read())
    print("Alright，all done.")

# from_file = input("Please input the from file name:")
# to_file = input("Please input the output file name:")
#
copy_file(input("Please input the from file name:"),
            input("Please output the from file name:"))
