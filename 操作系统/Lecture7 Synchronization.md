

## 并发进程的关系

- 独立关系
- **交互关系**
    - 竞争和协作

### 竞争 (RACE)

critical section

RACE CONDITION

### 写作 (COOPERATION)

## 异步产生的错误

## 同步

a mechanism to maintain the consistency of data shared in cooperative processes.

- Synchronization Tool Kits
    - Mutex lock    互斥锁
    - Semaphore     信号量

# 锁

- 互斥锁加锁失败后，线程会释放 CPU ，给其他线程；
- 自旋锁加锁失败后，线程会忙等待，直到它拿到锁；
对于互斥锁加锁失败而阻塞的现象，是由操作系统内核实现的。
**如果你能确定被锁住的代码执行时间很短，就不应该用互斥锁，而应该选用自旋锁，否则使用互斥锁。**

## 进程进出临界区协议

- 进入临界区前在entry section 要请求许可
- 离开临界区后要在exit section要归还许可

## 临界区管理准则

-  Mutual exclusion (Mutex)互斥
-  Progress         前进
-  Bounded waiting  有限等待


# 临界区管理

## 软件实现
1. 单标志法
P0
```c
while(turn!=0);
critical section;
turn = 1;
remainder section;
```
P1
```c
while(turn!=1);
critical section;
turn = 0;
remainder section;
```

2. 双标志先检查法
```c
while (flag [1]);
flag[0]=true;
critical section;
flag[0]=false;
remainder section;
```
```c
while (flag [0]);
flag[1]=true;
critical section;
flag[1]=false;
remainder section;
```

3. 双标志后检查法
```c
flag[0]=true; 
while (flag [1]); 
critical section; 
flag[0]=false; 
remainder section;
```
```c
flag[1]=true; 
while (flag [2]); 
critical section; 
flag[1]=false; 
remainder section;
```

4. Peterson 算法

##  硬件实现

1. 中断屏蔽方法
2. 硬件指令方法——TestAnd Set 指令

## MUTEX　LOCKS

- 上锁
    - 等待锁至打开状态
    - 获得锁并锁上
- 解锁
- 原子操作

## 原子操作

- Atomic operations mean the operation can NOT ne interrupted while it's running.

- 原子操作(原语)

## 忙式等待 (BUSY WAITING)

- 指占用CPU执行空循环实现等待
- 也称"自旋锁"(spin lock)
    - 浪费CPU周期 (-)
    - 没有上下文切换,在多处理器系统中优势更明显