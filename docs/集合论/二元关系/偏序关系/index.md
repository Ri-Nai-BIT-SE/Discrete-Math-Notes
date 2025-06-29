---
author: Ri-Nai
categories:
- 学习笔记
date: '2025-01-06T22:32:26+08:00'
description: null
draft: false
hidden: true
lastmod: '2025-01-06T22:32:26+08:00'
license: null
math: null
slug: 01 06 《离散数学》复习笔记/集合论/二元关系/偏序关系
tags:
- 离散数学
- 计算机科学
title: 偏序关系
---


# 偏序关系
若 $R$ 是自反的、反对称的、传递的，则称 $R$ 是偏序关系。记作 $\preccurlyeq$。
设 $\preccurlyeq$ 是一个偏序关系，若 $<x, y> \in \preccurlyeq$，则称 $x$ 小于等于 $y$，记作 $x \preccurlyeq y$。

## 偏序关系的性质
设 $R$ 是 $A$ 上的偏序关系
1. $\forall x, y \in A, x \prec y \Leftrightarrow x \preccurlyeq y \land x \neq y$
2. $\forall x, y \in A, x 与 y \textcolor{orange}{可比} \Leftrightarrow x \preccurlyeq y \lor y \preccurlyeq x$
    - 若 $\forall x, y \in A, x 与 y \textcolor{orange}{可比}$，则称 $R$ 是**全序关系** 
    - 实例：数集上的小于或等于关系是全序关系，整除关系不是正整数集合上的全序关系
3. 若 $x \prec y \land \neg\exists z(x \prec z \prec y)$，则称 $y$ **覆盖** $x$


## 偏序集
集合 $A$ 与其上的偏序关系 $\preccurlyeq$ 称为偏序集，记作 $\langle A, \preccurlyeq \rangle$
如：$\langle \mathbb{Z}, \leq \rangle$，$<P(A), \subseteq>,  \langle \mathbb{N}, | \rangle$

### 哈斯图
在 $\langle A, \preccurlyeq \rangle$ ，若 $y$ 覆盖 $x$，则 $y$ 在哈斯图中位于 $x$ 的上方，且用一条从 $x$ 指向 $y$ 的有向边表示。（绘制时忽略箭头）

哈斯图是简化的关系图，是由偏序关系的性质而省略的：
1. 自反性：每个顶点都有自环，故省略自环。
2. 反对称性：从小到大的有向边只有一条，故省略箭头。
3. 传递性：$<a, b>, <b, c> \in R \Rightarrow <a, c> \in R$，故省略 $\langle a, c \rangle$ 的有向边。

### 特殊元素

#### 最大元、最小元、极大元、极小元
设 $\langle A, \preccurlyeq \rangle$ 是一个偏序集， $B \subseteq A$，$\color{cyan}y \in B$，则
1. **最大元**：若 $\forall x(x \in B \to x \preccurlyeq y)$，则称 $y$ 是 $B$ 的最大元
2. **最小元**：若 $\forall x(x \in B \to y \preccurlyeq x)$，则称 $y$ 是 $B$ 的最小元
3. **极大元**：若 $\forall x(x \in B \to (y \preccurlyeq x \to x = y))$，则称 $y$ 是 $B$ 的极大元
4. **极小元**：若 $\forall x(x \in B \to (x \preccurlyeq y \to x = y))$，则称 $y$ 是 $B$ 的极小元

最大元和极小元要求集合中所有元素与其有偏序关系  
极大元和极小元仅要求没有比它更大或更小的元素。  

最大元和最小元不一定存在，但若存在则唯一。  
极大元和极小元一定存在，但不一定唯一。  

最大元一定是极大元，最小元一定是极小元。  

#### 上界、下界、上确界、下确界
设 $\langle A, \preccurlyeq \rangle$ 是一个偏序集，$B \subseteq A$，$\color{cyan}y \in A$，则
1. **上界**：若 $\forall x(x \in B \to x \preccurlyeq y)$，则称 $y$ 是 $B$ 的上界
2. **下界**：若 $\forall x(x \in B \to y \preccurlyeq x)$，则称 $y$ 是 $B$ 的下界
3. **上确界**：若 $C = \{y \ | \ y \text{ 是 } B \text{ 的上界}\}$，则 $C$ 的最小元称为 $B$ 的上确界或最小上界，记作 $\text{sup}B$
4. **下确界**：若 $C = \{y \ | \ y \text{ 是 } B \text{ 的下界}\}$，则 $C$ 的最大元称为 $B$ 的下确界或最大下界，记作 $\text{inf}B$

上下界与最大最小元的区别在于，上下界是在整个偏序集中寻找，而最大最小元是在指定的子集中寻找。

上界和下界不一定存在，若存在也不一定唯一。
上确界和下确界不一定存在，若存在一定唯一。

一个集合的最小元是它的下确界，最大元是它的上确界。反之不一定成立。

![偏序集的特殊元素](../../../imgs/偏序集的特殊元素.png)

