# ip
## IP首部数据报

![](https://lfool.gitbook.io/~gitbook/image?url=https%3A%2F%2F2396550738-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8zvqNNVZctOHx6v8No%252F-MDpHeNZK1ZJ3sjvGplI%252F-MDpKEAybbVOq3EFiV_0%252Fimage.png%3Falt%3Dmedia%26token%3Ddaa5e173-0337-46fa-ace1-db36441d2db8&width=400&dpr=3&quality=100&sign=fc3d3c48&sv=2)

```ad-note
title: 说明

### 版本（Version）
- 占4bit
- 通信双方使用的版本必须一致
- IPv4值为4

    ### 首部长度（IHL）
    - 占4bit
    - 以32位字（4字节）为单位
    - 最小值为5（20字节），最大值为15

    ### 区分服务（DS）
    - 占6bit
    - 1998年由IETF重定义
    - 用于实时数据流（如VoIP）

    ### 显式拥塞通告（ECN）
    - 可选功能
    - 用于网络拥塞通知
    - 需双端支持

    ### 全长（Total Length）
    - 16位字段
    - 包含首部和数据
    - 最小值20字节，最大值65,535字节

    ### 标识符（Identification）
    - 占16位
    - 用于唯一标识分片
    - 每个数据报计数器加1

    ### 标志（Flags）
    - 3位字段，用于分片控制
    - 位0：保留
    - 位1：禁止分片（DF）
    - 位2：更多分片（MF）

    ### 分片偏移（Fragment Offset）
    - 13位字段
    - 以8字节为单位
    - 指明分片相对原始报文的偏移量

    ### 存活时间（TTL）
    - 8位字段
    - 最大值255
    - 每经过一个路由器减1

    ### 协议（Protocol）
    - 占8bit
    - 定义数据区使用的协议
    - 由IANA维护协议列表

    ### 首部检验和（Header Checksum）
    - 16位字段
    - 只检验首部
    - 每一跳都重新计算

    ### 源地址和目的地址
    - 各占32位
    - 由四个字节构成
    - NAT可能会改变实际地址

    ### 选项（Options）
    - 可选字段
    - 1-40字节不等
    - 需要32位对齐
```
	  

## IP地址
IP 编址的历史阶段

1. 分类的 IP 地址

2. 子网的划分

3. 构成超网（无分类编址方式）

### IP 地址的分类
![](https://lfool.gitbook.io/~gitbook/image?url=https%3A%2F%2F2396550738-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8zvqNNVZctOHx6v8No%252F-MDtRZvDdU_WUE-cdQYm%252F-MDuRrDwf_2gKTnEQHqZ%252Fimage.png%3Falt%3Dmedia%26token%3Ddad867ea-9488-4fee-bf6f-841d01cdc551&width=400&dpr=3&quality=100&sign=d559c4a8&sv=2)

### 特殊 IP 地址
![](https://lfool.gitbook.io/~gitbook/image?url=https%3A%2F%2F2396550738-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8zvqNNVZctOHx6v8No%252F-MDtRZvDdU_WUE-cdQYm%252F-MDuSAUxNMqbdZ4Hr258%252Fimage.png%3Falt%3Dmedia%26token%3Df28823e6-4dfc-4075-9c31-943b160e3c99&width=400&dpr=3&quality=100&sign=5b61049c&sv=2)

### 私有 IP 地址
![](https://lfool.gitbook.io/~gitbook/image?url=https%3A%2F%2F2396550738-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8zvqNNVZctOHx6v8No%252F-MDtRZvDdU_WUE-cdQYm%252F-MDuSImBub4uc5sLIFbF%252Fimage.png%3Falt%3Dmedia%26token%3Da2e0600f-5be6-4bf4-bbb1-e10b324bc6f3&width=400&dpr=3&quality=100&sign=9c5623c8&sv=2)

## IPv6

![](https://lfool.gitbook.io/~gitbook/image?url=https%3A%2F%2F2396550738-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M8zvqNNVZctOHx6v8No%252F-ME1CQFgKVsgwxSikc3Q%252F-ME1TRlzE4sgSir3yqUj%252Fimage.png%3Falt%3Dmedia%26token%3D6d44a0b7-da16-4494-b28f-284483e3ddf7&width=400&dpr=3&quality=100&sign=7fa4f219&sv=2)

IPv6 向 IPv4 过渡的策略
1. 双栈协议
2. 隧道技术