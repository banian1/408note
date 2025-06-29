## 什么是操作系统

```ad-note title: 
角色      中间人
```
```ad-note title:
用户      run app
```
```ad-note title:
硬件      管理
```
## 计算机组成

1. Harddisk->boot sector

(MBR)

bootstrap

2. wait for random event
3. interrupt
4. storage
5. I/O devices

## 系统体系结构

1. single 
2. multiprocessor
3. clustered 集群
4. 操作系统结构  理念
    1. 多道程序设计
    2. 分时操作  多用户

    之前人共享,现在程序共享机器

    CPU调度

    内存管理->harddisk
    -> file -> 同步/异步(随机)->控制异步时间

# 内容

操作系统的服务:

1. 用户 (使用)
2. 程序员 (创造)

操作系统的构建方式 (设计标准)

GNU/Linux

## 服务

user interface 

1. GUI
2. batch (批处理)
3. commmand line

for programer 

1. systemcall

services:

1. program execution
2. I/O
3. file systems
4. communication
5. resource allocation
6. accounting 记录
7. error detection
8. security

### user interface

1. CLI

    command interpreter (shell)壳  zsh bash fish

2. GUI
3. Batch

a file which contains commands and directives(指示)(if /while)

## systemcall

实现代码是操作系统级的 面向程序员

API 
    程序员通过API间接访问了系统调用

    集合 : Windows API/POSIX API/JAVA API  标准


|用户态     |     内核态                |
|---|---|
|1      |         0|
|printf API |     write systemcall|

trap 陷入   中断

### 实现

- 系统调用号 (唯一)
- API 向系统调用接口指明系统调用号,内核维护了一张索引表,查表找代码在内核中的位置

### 设计模式

MULTICS -> UNIX

如何处理硬件复杂性

设计思路 

- 用户目标
- 系统目标

机制和策略分离

如何做 和 做什么

eg 接口和实现

微内核操作系统 Mach -> Drawin -> macos

### GNU/Linux

Open-source closed-source hybrid

linux       windows         macOS

GPL(GNU General Public License)


