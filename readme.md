# 功能

将Ripes的executable code转换为hex ram

1. 输入内容

```text
00000000 <mian>:
    0:        00600413        addi x8 x0 6
    4:        00900493        addi x9 x0 9
    8:        00940533        add x10 x8 x9

0000000c <subroute>:
    c:        00600413        addi x8 x0 6
    10:        00900493        addi x9 x0 9
    14:        00940533        add x10 x8 x9
```

2. 输出内容

```text
00 60 04 13
00 90 04 93
00 94 05 33
00 60 04 13
00 90 04 93
00 94 05 33
```

# 使用方法

## 1. 使用文件保存和输出代码（推荐）

主程序： main_by_file.py

将代码内容放在executable_code.txt中， 执行python3 main_by_file.py, 结果将会保存在mem.txt

## 2. 直接修改代码

主程序： main.py

修改main.py中的text变量，存放executable code, 执行，结果会打印在console中。