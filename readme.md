# 功能

* 将Ripes的executable code转换为hex ram

* 通过命令`--low_end`可以输出小端内容的ram(一行内按word反向), 默认为大端输出(不反向)

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

* 大端输出

`python main.py`

```text
00 60 04 13 //   0x0: addi x8 x0 6
00 90 04 93 //   0x4: addi x9 x0 9
00 94 05 33 //   0x8: add x10 x8 x9
00 60 04 13 //   0xc: addi x8 x0 6
00 90 04 93 //   0x10: addi x9 x0 9
00 94 05 33 //   0x14: add x10 x8 x9
```
* 小端输出

`python main.py --low_end`

```text
13 04 60 00 //   0x0: addi x8 x0 6
93 04 90 00 //   0x4: addi x9 x0 9
33 05 94 00 //   0x8: add x10 x8 x9
13 04 60 00 //   0xc: addi x8 x0 6
93 04 90 00 //   0x10: addi x9 x0 9
33 05 94 00 //   0x14: add x10 x8 x9
```


# 使用方法

## 1. 使用文件保存和输出代码（推荐）

主程序： main_by_file.py

将代码内容放在executable_code.txt中， 执行python3 main_by_file.py, 结果将会保存在mem.txt

## 2. 直接修改代码

主程序： main.py

修改main.py中的text变量，存放executable code, 执行，结果会打印在console中。

# 更新日志

## 20220828

* 修复一部分C代码转换的问题, 给不存在的代码填0x00
* 添加可切换大小端的命令`--low_end`

## 20220826

* 自动做大小端byte的转换
* 自动在mem文件中添加asm指令comment
* 兼容非0地址起始的程序, 如C语言编译的程序

