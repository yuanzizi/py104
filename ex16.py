
from sys import argv
script, filename = argv

print("你确认要删除文件 {} 的内容么？".format(filename))
print("确认要回车，取消按CTRL+C......")
input("?")

print ("opening file.....")
target = open(filename,'w')

print ("删除文件中.....")
target.truncate()

print("请重新输入新的内容.......")

line1 = input("Input the first line:")
# python3 默认使用unicode，可以通过encode来进行编码
line1_cn = line1.encode('gbk')
print(line1,line1_cn)

line2 = input("Input the second line:")
line3 = input("Input the third line:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finished，closing file.....")
target.close()
