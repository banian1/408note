
## 死锁与饥饿

- 饥饿:进程长时间等待
- 死锁:循环等待资源

- 死锁->饥饿
    - 饥饿可能终止
    - 无外部干涉,死锁无法终止

## 产生死锁的四个必要条件

- 互斥使用
- 不可剥夺
- 占有和等待
- 循环等待(结果)

## HANDE DEAKLOCKS

- 银行家算法
    - 已知系统中所有资源
    - 已知进程所需最大资源

    - 缺乏使用价值 (-)


## 安全状态

- A state is safe if the system can allocate resources to each process (up to its maximum) in some order and still avoid a deadlock . More formally ,a system is in a safe state if there exists a safe sequence

- If no such sequence exists,then it's said to unsafe

## 解除死锁

- 终止进程
- 剥夺资源
- 进程回退 (roll back)
- 重启
