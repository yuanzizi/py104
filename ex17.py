# -----ex17 文件操作 ------------

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#  原始代码
print("Copy from {} to {}".format(from_file,to_file))
print("Does the input files exist? {}".
        format(repr(exists(from_file))))
print("Does the output files exist? {}".
        format(repr(exists(to_file))))

indata = open(from_file).read()
print("The input file is {} bytes long".format(len(indata)))

input("Ready to copy? Return to continue or CTRL+C to abort")

out_file = open(to_file,'w+')
out_file.write(indata)

print("Alright, all done.")

out_file.close()

# 用一行代码来拷贝文件2
open(to_file,'w').write(open(from_file).read())

# 用一行来拷贝文件 1
with open(to_file,'w') as out_file:
        out_file.write(open(from_file,'r').read())
