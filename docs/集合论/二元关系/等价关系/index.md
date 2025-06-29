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
slug: 01 06 《离散数学》复习笔记/集合论/二元关系/等价关系
tags:
- 离散数学
- 计算机科学
title: 等价关系
---

# 等价关系


## 等价关系与划分
若 $R$ 是自反的、对称的、传递的，则称 $R$ 是等价关系。
设 $R$ 是一个等价关系，若 $xRy$，则称 $x$ 与 $y$ 是等价的，记作 $x \sim y$.

### 等价类
设 $R$ 是 $A$ 上的等价关系，$x \in A$，则
$$[x]_R = \{y \ | \ y \in A \land xRy\}$$

$$\forall x \in A, [x]_R \neq \varnothing, [x]_R \subseteq A$$
$$\forall x, y \in A, [x]_R \cap [y]_R = \begin{cases} \varnothing & x \nsim y \\ [x]_R & x \sim y \end{cases}$$
$$\bigcup \{ [x]_R | x \in A \} = A$$

### 商集与划分
$$A/R = \{[x]_R \ | \ x \in A\}$$
实例：$A = \{1, 2, \cdots 8\}$，关于模 $3$ 同余的等价关系 $R$ 的商集 $A/R = \{[1]_R, [2]_R, [3]_R\} = \{\{1, 4, 7\}, \{2, 5, 8\}, \{3, 6\}\}$

若 $A$ 的子集族 $\pi(\pi \subseteq P(A))$ 满足
- $\varnothing \notin \pi$
- $\bigcup \pi = A$
则称 $\pi$ 是 $A$ 的一个覆盖。

若 $A$ 的子集族 $\pi$ 是一个**覆盖**，且
- $\forall x \forall y(x, y \in \pi land x \neq y \to x \cap y = \varnothing)$
则称 $\pi$ 是 $A$ 的一个**划分**，$\pi$ 的元素称为 $A$ 的划分块。


集合 $A$ 上的一个等价关系 $R$ , 决定了 $A$ 的一个划分，该划分就是商集 $A/R$ 

集合 $A$ 的一个划分,确定 $A$ 的元素间的一个等价关系
