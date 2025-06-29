---
author: Ri-Nai
categories:
- 学习笔记
date: '2025-01-06T21:14:24+08:00'
description: null
draft: false
hidden: true
lastmod: '2025-01-06T21:14:24+08:00'
license: null
math: null
slug: 01 06 《离散数学》复习笔记/代数结构/群与环/群、子群与陪集
tags:
- 离散数学
- 计算机科学
title: 群、子群与陪集
---

# 群、子群与陪集

## 群的定义
- **半群**：设 $V =  \langle S, \circ \rangle$ 是一个代数系统，若 $\circ$ 是**可结合**的，则称 $V$ 是一个**半群**。
- **独异点**：设 $V =  \langle S, \circ \rangle$ 是一个半群，若 $V$ 中存在**单位元** $e$，则称 $V$ 是一个**含幺半群**，也称为**独异点**。
- **群**：设 $V =  \langle S, \circ \rangle$ 独异点，若 $V$ 中任意元素 $a$ 都有**逆元**，则称 $V$ 是一个**群**，通常将群记作 $G$。

实例：
- $\langle \mathbb{Z}^+, + \rangle$ 是半群
- $\langle \mathbb{N}, + \rangle$ 是含幺半群
- $\langle \mathbb{Z}, + \rangle$ 是群
- Klein 四元群 $G = \{e, a, b, c\}$，满足交换律，每个元素都是自己的逆元，$a, b, c$ 中任意两个元素的运算结果都是第三个元素。

### 有关群的术语与性质
- **有限群**：群 $G$ 是有限集。
- **群的阶**：群 $G$ 的[基数](../../../集合论/函数/#集合基数)称为 $G$ 的**阶**，记作 $|G|$。
- **平凡群**：只有一个元素的群。（即只含单位元的群）
- **阿贝尔群**：满足交换律的群，也称为**交换群**。

- **元素的幂**：设 $a \in G, n \in \mathbb{Z}$，定义 $a^n$ 为：$a^n = \begin{cases} a^{n -1} a & n > 0 \\ e & n = 0 \\ (a^{-1})^n & n < 0 \end{cases}$
- **元素的阶**：设 $a \in G$，若存在最小的正整数 $n$ 使得 $a^n = e$，则称 $n$ 为 $a$ 的**阶**，称 $a$ 为 $n$ 阶元，若不存在这样的 $n$，称 $a$ 为**无限阶元**。
    - $e$ 是 $\color{cyan}1$ 阶元 

#### 幂运算的性质
1. $\forall a \in G, \left(a^{-1}\right)^{-1} = a$
2. $\forall a, b \in G, (ab)^{-1} = b^{-1} a^{-1}$
3. $\forall a \in G, a^n a^m = a^{n + m}$
4. $\forall a \in G, (a^n)^m = a^{nm}$
5. $G 是交换群 \Rightarrow \forall a, b \in G, (ab)^n = a^n b^n$

#### 阶的性质
1. $\forall a \in G, a^k = e \Rightarrow |a| | k$
2. $\forall a \in G, |a| = |a^{-1}|$

- $a, b \in G 且是有限阶元 \left|b^{-1} a b\right| = |a|$


#### 消去律
$a, b, c \in G$
1. $ab = ac \Rightarrow b = c$
2. $ba = ca \Rightarrow b = c$

$$G = {a_1, a_2, \cdots, a_n}, a_iG = \{a_i a_j \ | \ a_j \in G\} = G$$


设群 $G$ 为有限群，则 $G$ 中阶大于 $2$ 的元素有偶数个。

- 若 $a^2 = e$，则 $a = a^{-1}$
- 故 $G$ 中阶大于 $2$ 的元素要成对出现。

$\forall x, b \in G$, 方程 $ax = b$ 和 $ya = b$ 在 $G$ 中存在唯一解。

#### 无零元
若 $G$ 中存在零元 $\theta$，则有 $\forall x \in G, x \theta = \theta x = \theta \neq x$，故 $G$ 中不存在零元。

## 子群与群的陪集分解
### 子群
设 $G$ 是一个群，若 $H$ 是 $G$ 的一个**非空子集**，且 $H$ 对 $G$ 的运算构成一个群，则称 $H$ 是 $G$ 的一个**子群**，记作 $H \leq G$。
若 $H$ 是 $G$ 的子群，且 $H \neq G$，则称 $H$ 是 $G$ 的**真子群**，记作 $H < G$。

对任何群 $G$ 都存在子群。$G$ 和 $\{e\}$ 都是 $G$ 的子群，称为 $G$ 的**平凡子群**。

#### 子群的判定
1. 使用定义验证：
    - $\forall a, b \in H, ab \in H$
    - $\forall a \in H, a^{-1} \in H$
2. $H \neq \varnothing, \forall a, b \in H, ab^{-1} \in H$
3. $H \neq \varnothing$，且 $H$ 是有穷的，$\forall a, b \in H, ab \in H$

#### 生成子群
设 $G$ 是一个群，$a \in G$，令 $H = \{a^k \ | \ k \in \mathbb{Z}\}$，则 $H$ 是 $G$ 的一个子群，称 $H$ 是由 $a$ 生成的子群，记作 $H = \langle a \rangle$。

##### 由子集生成的子群
$B \subseteq G$
$$\langle B \rangle = \bigcap \{H \ | \ B \subseteq H \land H \leq G\}$$

##### 中心
$$C = \{a \in G \ | \ \forall x \in G, ax = xa\}$$
称 $C$ 为 $G$ 的**中心**，$C$ 是 $G$ 的一个子群。

#### 子群的并和交
设 $G$ 是一个群，$H_1, H_2$ 是 $G$ 的两个子群，则
1. $H_1 \cap H_2$ 是 $G$ 的子群
2. $H_1 \cup H_2$ 当且仅当 $H_1 \subseteq H_2$ 或 $H_2 \subseteq H_1$ 时是 $G$ 的子群

#### 子群格
$$L(G) = \{H \ | \ H \leq G\}$$
则偏序集 $\langle L(G), \subseteq \rangle$ 称为 $G$ 的**子群格**。

[子群格](../格与布尔代数/#子群格)

### 陪集
有 $a \in G, H \leq G$
- $Ha = \{ha \ | \ h \in H\}$ 称为 $H$ 的**右陪集**
- $aH = \{ah \ | \ h \in H\}$ 称为 $H$ 的**左陪集**

下面主要讨论右陪集。

$a$ 为 $Ha$ 或 $aH$ 的**代表元素**。

#### 陪集的性质
1. $H = H$
2. $\forall a \in G, a \in Ha$
3. $a \in Hb \Leftrightarrow ab^{-1} \in H \Leftrightarrow Ha = Hb$

定义等价关系 $R$：
$$aRb \Leftrightarrow a \in Hb \Leftrightarrow ab^{-1} \in H$$
$$[a]_R = Ha$$

1. $\forall a, b \in G, Ha = Hb \overline{\lor} Ha \cap Hb = \varnothing$
2. $\bigcup \{Ha \ | \ a \in G\} = G$
3. $H \approx Ha$，即 $|H| = |Ha|$

- **正规子群**：若 $H$ 是 $G$ 的子群，且 $\forall a \in G, Ha = aH = H$，则称 $H$ 是 $G$ 的**正规子群**，也称 **不变子群**。

#### Lagrange 定理
设 $G$ 是一个**有限群**，$H$ 是 $G$ 的一个**子群**，有：
$$|G| = |H| \cdot [G : H]$$
其中 $[G : H]$ 称为 $G$ 对 $H$ 的**指数**，是 $H$ 在 $G$ 中的不同右陪集的个数。

##### 推论
1. 对有限群 $G$，$\forall a \in G, |a| \ \mathbf{\Big|} \ |G|$
2. 对于阶是素数的群，其子群只有平凡子群和本身，即 $\forall a \in G, \langle a \rangle = G$
