import re,sys

_LOW_END = False # 是否根据进行大小端的反向 

def get_argument():
    # 判断参数
    argument = sys.argv
    print(argument)
    flag = False
    if "--low_end" in argument:
        global _LOW_END
        _LOW_END = True

# 将代码内容放在executable_code.txt中， 执行python3 main_by_file.py, 结果将会保存在mem.txt


import re
def tranlate(text):
    get_argument()
    # 通过正则表达式将hex code提取出来
    hex_code_list = re.findall("([0-9a-fA-F]+):\s+([0-9a-fA-F]+)\s+(\w[^\n]+)",text)
    hex_code_list = [(int(i[0],16),)+i for i in hex_code_list]
    output_list = dict([[i,"00 00 00 00 // %s:"%hex(i)] for i in range(0,max([i[0] for i in hex_code_list]),4)])
    for index,hex_index,hex_code,comment in hex_code_list:
        if _LOW_END:
            hex_code = " ".join([hex_code[j-2:j] for j in range((len(hex_code)),0,-2)])
        else:
            hex_code = " ".join([hex_code[j:j+2] for j in range(0,(len(hex_code)),2)])
        output_list[index] = "%s //\t %s: %s"%(hex_code,hex(index),comment) 
    # for index,hex_index, in hex_code_list:
    return "\n".join(output_list.values())


if __name__ == "__main__":
    with open("executable_code.txt", "r") as f:
        text = f.read()
    mem = tranlate(text)
    with open("mem.txt", "w") as f:
        f.write(mem)

    print("success!! pls check the file named mem.txt")