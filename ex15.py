# ---- ex15 文件操作----------------

from sys import argv

script,filename = argv

txt = open(filename)
# txt 文件指针的值
# <_io.TextIOWrapper name='ex15_sample.txt' mode='r' encoding='cp936'>
#

print(txt.read())

# 中文的文件要改编码，要不运行结果会报错
#  UnicodeDecodeError: 'gbk' codec can't decode
#  byte 0xaf in position 113: illegal multibyte sequence
#

filename_cn = input("请输入中文文本文件名：")
# 用encode() 序列化
txt_cn = open(filename_cn,encoding='utf-8')
print(txt_cn.read())


# ----- ex16 文件读写 ----------------
