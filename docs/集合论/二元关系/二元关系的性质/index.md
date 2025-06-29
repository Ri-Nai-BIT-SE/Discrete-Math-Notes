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
slug: 01 06 《离散数学》复习笔记/集合论/二元关系/二元关系的性质
tags:
- 离散数学
- 计算机科学
title: 二元关系的性质
---

# 二元关系的性质

## 有序对与笛卡尔积
### 有序对
由两个元素 $x$ 和 $y$，按照一定的顺序组成的二元组称为有序对，记作 $\langle x,y \rangle$.

有序对性质：
- 有序性：$<x,y> \neq  \langle y,x \rangle$
- 相等性：$<x,y> = <u,v> \Leftrightarrow x = u \land y = v$

### 笛卡尔积
$$A \times B = \{<x,y> \ | \ x \in A \land y \in B\}$$

笛卡尔积的性质：
- 不适合交换律：
- 不适合结合律：
- 对于并和交运算满足分配律：
$$A \times (B \cup C) = (A \times B) \cup (A \times C)$$
$$A \times (B \cap C) = (A \times B) \cap (A \times C)$$
- $A \times \varnothing = \varnothing \times B = \varnothing$
- $\left|A \times B\right| = \left|A\right| \times \left|B\right|$

## 二元关系
### 二元关系的定义
集合 $R$ 称为一个二元关系，当：
- $R$ 是空集
- $R$ 中的所有元素都是有序对
若 $<x,y> \in R$，则称 $x$ 与 $y$ 有关系 $R$，记作 $xRy$.
若 $<x,y> \notin R$，则称 $x$ 与 $y$ 无关系 $R$，记作 $x \cancel{R} y$.

设 $A$ 和 $B$ 是两个集合，$A \times B$ 的任意子集所定义的二元关系称为从 $A$ 到 $B$ 的二元关系.
当 $A = B$ 时，称为 $A$ 上的二元关系.

### 重要关系的实例
设 $A$ 为集合
- **空关系**：$\varnothing$ 是 $A$ 上的关系，称为**空关系**
- **全域关系**：$E_A = \{<x, y> \ | \ x in A \land y \in A\} = A \times A$ 是 $A$ 上的关系，称为**全域关系**
- **相等关系**：$I_A = \{<x, x> \ | \ x \in A\}$ 是 $A$ 上的关系，称为**相等关系**
- **小于等于关系**：$L_A = \{<x, y> \ | \ x, y \in A \land x \leq y\}$ 是 $A$ 上的关系，称为**小于等于关系**
- **整除关系**：$D_A = \{ <x, y> \ | \ x, y \in A \land x | y \}$ 是 $A$ 上的关系，称为**整除关系**
- **包含关系**：$R_\subseteq = \{<x, y> \ | \ x, y \in A \land x \subseteq y\}$ 是 $A$ 上的关系，称为**包含关系**

### 关系的表示
#### 关系矩阵
$A = \{x_1, x_2, \cdots, x_m\}$，$B = \{y_1, y_2, \cdots, y_n\}$，$R$ 是 $A$ 到 $B$ 的关系，$R$ 的关系矩阵是一个 $m \times n$ 的布尔矩阵 $M_R = [r_{ij}]_{m \times n}$，其中
$$r_{ij} = 1 \Leftrightarrow x_i R y_j$$

#### 关系图
$G_R = (A, R)$，$A$ 是顶点集，$R$ 是边集，$R$ 是 $A$ 到 $A$ 的关系，$G_R$ 是一个有向图.

关系矩阵适合表示从 $A$ 到 $B$ 的关系或 $A$ 上的关系（ $A$，$B$ 为有穷集）
关系图适合表示有穷集 $A$ 上的关系 

## 关系的运算
- **定义域**：$domR = \{x \ | \ \exists y(xRy)\}$
- **值域**：$ranR = \{y \ | \ \exists x(xRy)\}$
- **域**：$fldR = domR \cup ranR$

- **逆运算**：$R^{-1} = \{<y, x> \ | \ <x, y> \in R\}$
- **复合运算**：$R \circ S = \{<x, z> \ | \ \exists y(xRy \land ySz)\}$
    - $R \circ S \neq S \circ R$
- **幂运算**：
$$R^n = \begin{cases}
{<x, x> \ | \ x \in A} = I_A & n = 0 \\
R \circ R^{n-1} & n > 0
\end{cases}$$

- **限制**：$R \upharpoonright A = R \cap (A \times A) = \{<x, y> \ | \ <x, y> \in R \land x \in A\}$
    - $R$ 在 $A$ 上的限制 $R \upharpoonright A$ 是 $R$ 在 $A$ 上的部分，是 $R$ 的子关系，即 $R \upharpoonright A \subseteq R$
- **像**：$R[A] = \{y \ | \ \exists x(x \in A \land xRy)\} = ran(R \upharpoonright A)$
    - A 在 $R$ 下的像 $R[A]$ 是 $ranR$ 的子集，即 $R[A] \subseteq ranR$           

	
#### 关系的运算性质
- 逆运算的逆运算：$(F^{-1})^{-1} = F$
- 逆运算的域：$domR^{-1} = ranR, \quad ranR^{-1} = domR$

- 复合运算的逆运算：$(F \circ G)^{-1} = G^{-1} \circ F^{-1}$
- 复合运算的结合律：$(F \circ G) \circ H = F \circ (G \circ H)$
- 复合运算的分配律：
$$\begin{aligned}
F \circ (G \cup H) = (F \circ G) \cup (F \circ H) & & 
(G \cup H) \circ F = (G \circ F) \cup (H \circ F)\\
F \circ (G \cap H) \subseteq (F \circ G) \cap (F \circ H)& & 
F \circ (G \cap H) \supseteq (F \circ G) \cap (F \circ H)
\end{aligned}$$
可以推广到有限个集合的并和交

- 相等关系上的复合运算：$I_A \circ R = R \circ I_A = R$

- 限制与像运算的分配律：
$$\begin{aligned}
F \upharpoonright (A \cup B) &= F \upharpoonright A \cup F \upharpoonright B &
F \upharpoonright (A \cap B) &= F \upharpoonright A \cap F \upharpoonright B \\
F [A \cup B] &= F[A] \cup F[B] &
F [A \cap B] &\subseteq F[A] \cap F[B]
\end{aligned}$$

#### 幂运算的性质
不同的幂运算只有有限个

$$R^m \circ R^n = R^{m+n}$$
$$(R^m)^n = R^{mn}$$

## 关系的性质
- **自反性**：$R$ 是自反的，当 $\forall x(x \in A \to xRx)$
- **反自反性**：$R$ 是反自反的，当 $\forall x(x \in A \to x \cancel{R} x)$
- **对称性**：$R$ 是对称的，当 $\forall x \forall y(xRy \to yRx)$
- **反对称性**：$R$ 是反对称的，当 $\forall x \forall y(xRy \land yRx \to x = y)$

- **传递性**：$R$ 是传递的，当 $\forall x \forall y \forall z(xRy \land yRz \to xRz)$

| 表示 | 自反 | 反自反 | 对称 | 反对称 | 传递 |
| :--: | :--: | :----: | :--: | :----: | :--: |
| 集合表达式 | $I_A \subseteq R$ | $I_A \cap R = \varnothing$ | $R = R^{-1}$ | $R \cap R^{-1} \subseteq I_A$ | $R \circ R \subseteq R$ |
| 关系矩阵 | 对角线全为 1 | 对角线全为 0 | 对称 | $r_{ij} + r_{ji} \leq 1$ | $r_{ij} = 1 \land r_{jk} = 1 \Rightarrow r_{ik} = 1$ |
| 关系图 | 每个顶点都有自环 | 没有自环 | 无向图对称 | 有向图 | 有向图传递 |

|       运算        |      自反      |     反自反      |      对称      |     反对称      |      传递      |
| :-------------: | :----------: | :----------: | :----------: | :----------: | :----------: |
|   $R_1^{-1}$    | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| $R_1 \cap R_2$  | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| $R_1 \cup R_2$  | $\checkmark$ | $\checkmark$ | $\checkmark$ |   $\times$   |   $\times$   |
|   $R_1 - R_2$   |   $\times$   | $\checkmark$ | $\checkmark$ | $\checkmark$ |   $\times$   |
| $R_1 \circ R_2$ |   $\times$   |   $\times$   |   $\times$   |   $\times$   | $\checkmark$ |
