# 在双引号的中间粘贴上executable code, 点击运行即可

text = """
00000000 <mian>:
    0:        00600413        addi x8 x0 6
    4:        00900493        addi x9 x0 9
    8:        00940533        add x10 x8 x9

0000000c <subroute>:
    c:        00600413        addi x8 x0 6
    10:        00900493        addi x9 x0 9
    14:        00940533        add x10 x8 x9
"""
# input("pls input executable code and press enter:")

import re
y = re.findall(":\s+([0-9a-fA-F]+)\s+",text)
y = ["%s %s %s %s"%(i[:2],i[2:4],i[4:6],i[6:]) for i in y]
print("\n".join(y))