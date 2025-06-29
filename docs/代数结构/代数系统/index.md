---
author: Ri-Nai
categories:
- 学习笔记
date: '2025-01-06T15:47:03+08:00'
description: null
draft: false
hidden: true
lastmod: '2025-01-06T15:47:03+08:00'
license: null
math: null
slug: 01 06 《离散数学》复习笔记/代数结构/代数系统
tags:
- 离散数学
- 计算机科学
title: 代数系统
---

# 代数系统

## 二元运算及其性质
### 一元运算的定义
设 $S$ 为集合，函数 $f: S \to S$ 称为 $S$ 上的**一元运算**，简称为一元运算。

### 二元运算的定义
设 $S$ 为集合，函数 $f: S \times S \to S$ 称为 $S$ 上的**二元运算**，简称为二元运算。
- $S$ 中任意两个元素都可以进行运算，且运算结果唯一。
- 二元运算的运算结果仍然属于 $S$，即运算**封闭**。

### 一元运算和二元运算的表示方法
1. 算符：$\oplus, \odot, \cdots$，$x \oplus y, \Delta x, \cdots$
2. 解析公式
3. 运算表

### 二元运算的性质
#### 单个二元运算的性质
- **交换律**：若 $\forall x, y \in S, x \circ y = y \circ x$，则称 $\circ$ 满足交换律。
- **结合律**：若 $\forall x, y, z \in S, (x \circ y) \circ z = x \circ (y \circ z)$，则称 $\circ$ 满足结合律。
- **幂等律**：若 $\forall x \in S, x \circ x = x$，则称 $\circ$ 满足幂等律。

#### 多个二元运算的性质
- **分配律**：若 $\forall x, y, z \in S, x \circ (y \bullet z) = (x \circ y) \bullet (x \circ z) 且 (y \bullet z) \circ x = (y \circ x) \bullet (z \circ x)$，则称 $\circ$ 对 $\bullet$ 满足分配律。
- **吸收律**：若 $\forall x, y \in S, x \circ (x \bullet y) = x$，则称 $\circ$ 对 $\bullet$ 满足吸收律。


### 特异元素
#### 单位元
- **左单位元**：若 $\forall x \in S, e_l \circ x = x$，则称 $e_l$ 为 $\circ$ 的左单位元。
- **右单位元**：若 $\forall x \in S, x \circ e_r = x$，则称 $e_r$ 为 $\circ$ 的右单位元。
- **单位元**：若 $e$ 既是左单位元又是右单位元，则称 $e$ 为 $\circ$ 的单位元，也称为**幺元**。

#### 零元
- **左零元**：若 $\forall x \in S, \theta_l \circ x = \theta_l$，则称 $\theta_l$ 为 $\circ$ 的左零元。
- **右零元**：若 $\forall x \in S, x \circ \theta_r = \theta_r$，则称 $\theta_r$ 为 $\circ$ 的右零元。
- **零元**：若 $\theta$ 既是左零元又是右零元，则称 $\theta$ 为 $\circ$ 的零元。

#### 逆元
若二元运算存在单位元 $e$：
- **左逆元**：若 $\forall x \in S, x \circ x^{-1} = e$，则称 $x^{-1}$ 为 $x$ 的左逆元。
- **右逆元**：若 $\forall x \in S, x^{-1} \circ x = e$，则称 $x^{-1}$ 为 $x$ 的右逆元。
- **逆元**：若 $x$ 既有左逆元又有右逆元，则称 $x^{-1}$ 为 $x$ 的逆元。

- **可逆的**：若 $\forall x \in S, \exists x^{-1} \in S, x \circ x^{-1} = x^{-1} \circ x = e$，则称 $x$ 可逆。

唯一性定理：若 $x$ 有左逆元 $y_l$ 和右逆元 $y_r$，则 $y_l = y_r$，且 $y_l$ 为 $x$ 的逆元。

### 运算表
#### 运算表与运算性质
- **封闭性**：运算表中的元素都在集合中。
- **交换律**：运算表关于主对角线对称。
- **幂等性**：运算表主对角线上的元素均与表头元素相同。
- **结合律**：判断比较复杂，一般通过运算表无法判断。
    - 需要针对运算元素的每种选择进行验证，若 $|A| = n$，一般需要验证 $n^3$ 个等式.
  

#### 运算表与特异元素
- **有幺元**：该元素所对应的行和列依次与运算表的行和列相一致；
- **有零元**：该元素所对应的行和列中的元素都与该元素相同；
- 设 $A$ 中有幺元，$a$ 和 $b$ 互逆，当且仅当位于 $a$ 所在行，$b$ 所在列的元素以及 b 所在行，a 所在列的元素都是幺元。


## 代数系统
非空集合 $S$ 与 $S$ 上的 $k$ 一元或二元运算构成的系统称为**代数系统**，简称**代数**。记作：$\langle S, f_1, f_2, \cdots, f_k \rangle$。

### 代数系统的成分
- **非空集合**：$S$，也叫 **载体**。
- **运算**：$S$ 上的一元或二元运算。
- **代数常数**：代数系统中的特异元素。

实例：
$V_1 =  \langle \mathbb{Z},+,0 \rangle$, $V_2 = P(S), \cup, \cap, \varnothing, S$

### 同类型的代数系统
若两个代数系统中**运算**的**个数**以及对应的**元数**相同，且**代数常数**的个数也相同，则称这两个代数系统是**同类型的**。

如 $V_1 =  \langle \mathbb{R}, +, \cdot, 0, 1 \rangle$ 和 $V_2 =  \langle P(B), \cup, cap, \varnothing, B \rangle$ 是同类型的代数系统。

同类型的代数系统仅仅是具有相同的成分，不一定具有相同的运算性质！

### 子代数系统
设 $V =  \langle S, f_1, f_2, \cdots, f_k \rangle$ 是一个代数系统，若 $S' \subseteq S$，且 $S'$ 与 $V$ 中的运算在 $S'$ 上封闭，则称 $V' =  \langle S', f_1, f_2, \cdots, f_k \rangle$ 是 $V$ 的**子代数系统**，简称**子代数**。

有时会将子代数系统简记为 $S'$。

#### 特殊的子代数系统
- **最大的**子代数：$V$ 本身。
- **最小的**子代数：若 $V$ 中所有的代数常数构成的代数系统对 $V$ 中的运算封闭，则该代数系统是 $V$ 的最小子代数。
- **平凡的**子代数：**最大的**子代数和**最小的**子代数。
- **真**子代数：不是 $V$ 本身的子代数。即 $S' \varsubsetneqq S$。


### 积代数
设 $V_1 =  \langle A, \circ \rangle$ 和 $V_2 =  \langle B, \bullet \rangle$ 是同类型的代数系统，在 $A \times B$ 上定义二元运算 $\odot$：
$$\forall <a_1, b_1>, <a_2, b_2> \in A \times B, <a_1, b_1> \odot <a_2, b_2> =  \langle a_1 \circ a_2, b_1 \bullet b_2 \rangle$$
称 $V =  \langle A \times B, \odot \rangle$ 为 $V_1$ 和 $V_2$ 的**积代数**，记作 $V = V_1 \times V_2$，此时也称 $V_1$ 和 $V_2$ 是 $V$ 的**因子代数**。

### 代数系统的同态与同构
#### 代数系统的同态
$V_1 =  \langle A, \circ \rangle$ 和 $V_2 =  \langle B, \bullet \rangle$ 是同类型的代数系统，若存在映射 $f: A \to B$，且满足：
$$\forall x, y \in A, f(x \circ y) = f(x) \bullet f(y)$$
则称 $f$ 是 $V_1$ 到 $V_2$ 的**同态映射**，简称**同态**。

##### 同态的分类
- **单同态**：若 $f$ 是单射，则称 $f$ 是**单同态**。
- **满同态**：若 $f$ 是满射，则称 $f$ 是**满同态**，此时称 $V_2$ 是 $V_1$ 的**同态像**。记作 $V_1 \sim V_2$。
- **同构**：若 $f$ 是双射，则称 $f$ 是**同构映射**，$V_1$ 和 $V_2$ 是**同构的**，记作 $V_1 \cong V_2$。 
- **自同态**：若 $V_1 = V_2$，则称 $f$ 是 $V_1$ 的**自同态**。
