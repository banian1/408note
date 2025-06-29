
## 信号量

Semaphore 是一种比互斥锁更强大的同步工具

    由Dijkstra提出

- A semaphore S is an integer variable that , aprt from initialization, is accessed only through two standard atomic operations : P and V

    - P : wait()    operation
    - V : signal()  operation

## BINARY SEAMAPHORE

- 二值信号量只能是0或1,通常将其初始化为1,用于实现互斥锁的功能

## COUNTING SEMAPHORE

- 取值可以指任意数值 ,用于控制并发进程对共享资源的访问

## 信号量

- 整数值
    - 除了初始化 只能使用P,V操作
        - P操作: 如果<=0执行忙式等待,否则信号量减一
        - V操作: 将信号量加1
        - 都是原子操作
- 类型
    - 二值
        - 初始值=1,用于实现互斥锁
    - 一般
        - 初始值>1,用于表示可用资源的数量
        - 初始值=1,等价于二值信号量
        - 初始值=0,用于进程同步
## 同步问题

- 实质是将异步的并发进程按照某种顺序执行
- 解决同步的本质就是要找到并发进程的交互点,利用P操作的等待特点调节进程的执行速度
- 通常初始值为0的信号量可以让进程直接进入等待状态,知道另一个进程唤醒他

