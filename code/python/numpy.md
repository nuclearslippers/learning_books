# Numpy库学习笔记

## 1. 简介

NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

官网：https://www.numpy.org/
源码：https://github.com/numpy/numpy

## 2. 基础数据结构

numpy.array 是 numpy 的核心数据结构。

<div style="text-align: center; margin: 0 auto;">

| 属性 | 描述 |
| :---: | :---: |
| `ndarray.ndim` | 数组维度 |
| `ndarray.shape` | 数组形状 |
| `ndarray.size` | 数组元素个数（各个维度乘积） |
| `ndarray.dtype` | 数组元素数据类型 |

</div>

## 3. 数组的基础使用

__1. 创建数组__

`numpy.empty(shape, dtype)` 创建一个空(未初始化)的数组。

`numpy.zeros(shape, dtype)` 创建一个全零数组。

`numpy.ones(shape, dtype)` 创建一个全一数组。

`numpy.zeros_like(array)` 模仿给定数组创建一个全零数组。

`numpy.arange(start, stop, step, dtype)` 创建一个范围数组。

__2. 数组索引/切片__

ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。

(1) 普通索引

`start:stop:step` 分别设置起始，终止和步长。注意冒号`:`包括开头不包括结尾。`...`代表长度跟该轴相同

(2) 布尔索引

`x[x > 3]` 该方法会将数组展品，返回一个1D数组

`dim1, dim2 = np.where(x > 3)` 该方法返回元素的具体索引位置

__3. 广播机制__

我们提到Numpy库是数组计算的工具，那么两个数组怎么进行加减乘除呢？

一般而言，进行数值计算的两个数组形状相同，此时计算为位运算（对应位做运算）。当数组形状不同时，Numpy引入广播机制来处理。

广播流程和原则：
1. 判断数组形状是否相同，不相同的小数组往前面补1，直到相同。实际上，Numpy会智能匹配，即可能也会往后补1。
2. 判断能否广播，同一纬度要么相同，要么为1。不然就不能广播。
3. 广播即将低纬度的内容多次复制，使得当前维度的大小和另一个数组相同。

_对于[1,2,3]（3，）的理解：这是一个一维数组，实际上它的维度是(3)。但是这样不好看/容易混淆，所以加个逗号说明这是shape属性_

__4. 数组操作__

1. 修改形状：`numpy.ndarray.reshape`

注意，`-1`代表自动计算该维度的大小。而且这是原地操作。

2. 展平数组：`numpy.ndarray.flatten`

将数组变为一维数组。

3. 数组转置：`numpy.ndarray.transpose`

可以用于高纬数组，默认完全反转([2,3,4]-->[4,3,2])。还可以通过`axes`指定反转维度。它和`reshape`不同的地方是，它传入的参数是序号，而不是具体的维度大小。

4. 扩展维度：`numpy.expand_dims`

`numpy.expand_dims(arr, axis)` 在`axis`处增加一个维度。

5. 删除维度：`numpy.squeeze`

`numpy.squeeze(arr)` 删除数组中大小为1的维度。

6. 拼接数组：`numpy.concatenate`

`numpy.concatenate((arr1, arr2), axis)` 将两个数组在`axis`方向上拼接。

7. 沿着新轴堆叠数组：`numpy.stack`

`numpy.stack((arr1, arr2), axis)` 将两个数组在`axis`方向上堆叠。
