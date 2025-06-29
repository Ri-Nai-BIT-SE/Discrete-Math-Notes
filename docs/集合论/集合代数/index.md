---
author: Ri-Nai
categories:
- 学习笔记
date: '2025-01-06T12:00:18+08:00'
description: null
draft: false
hidden: true
lastmod: '2025-01-06T12:00:18+08:00'
license: null
math: null
slug: 01 06 《离散数学》复习笔记/集合论/集合代数
tags:
- 离散数学
- 计算机科学
title: 集合代数
---

# 集合代数

## 集合的基本概念
### 集合的定义
由一些个体构成的整体称为**集合**。称为集合的个体为**元素**。

### 集合的表示
- **枚举法**：列举出集合中的所有元素。
- **谓词表示法**：通过谓词概括集合中的元素。
例如：
- 枚举法：自然数集合：$\mathbb{N} = \{1, 2, 3, \cdots\}$
- 谓词表示法：偶数集合：$A = \{x | x = 2k, k \in \mathbb{N}\}$

- 集合的树形结构表示：
```   
          A
         /|\
        / | \
       /  |  \
      /   |   \
     /    |    \
  {a, b}{{b}}   d
   /  \   |
  a    b {b}
          |
          b
``` 

### 集合的元素具有的性质
- **无序性**：集合中的元素之间没有先后次序之分。
- **相异性**：集合中的元素各不相同。
- **确定性**：一个元素要么属于一个集合，要么不属于一个集合。
- **任意性**：集合中的元素可以是任意的，也可以是集合。

### 元素和集合的关系
$\in$：元素属于集合。
$\notin$：元素不属于集合。

### 集合与集合的关系
$$A \subseteq B \Leftrightarrow \forall x(x \in A \Rightarrow x \in B)$$
$$A = B \Leftrightarrow A \subseteq B \land B \subseteq A$$
$$A \varsubsetneqq B \Leftrightarrow A \subseteq B \land A \neq B$$
$$A \nsubseteq B \Leftrightarrow \exists x(x\in A \land x \notin B)$$

### 空集
不包含任何元素的集合称为**空集**，记作 $\varnothing$
空集是任何集合的子集，即 $\varnothing \subseteq A$
空集是唯一的。

### 全集
包含一切可能元素的集合称为**全集**，记作 $E$。

全集具有相对性，与讨论的问题有关，不存在绝对的全集。

### 幂集
$$P(A) = \{ x \ | \ x \subseteq A \}$$
例如：$A = \{a, b\}$，则 $P(A) = \{\varnothing, \{a\}, \{b\}, \{a, b\}\}$

## 集合的运算
$$\begin{aligned}
并 & & A \cup B &= \{x \ | \ x \in A \lor x \in B\} \\
交 & & A \cap B &= \{x \ | \ x \in A \land x \in B\} \\
相对补\ /\ 差 & & A - B &= \{x \ | \ x \in A \land x \notin B\} \\
绝对补 & & \overline{A} &= ~A = E - A \\
对称差 & & A \oplus B &= (A - B) \cup (B - A) \\ \\ 

广义并 & & \bigcup_{i=1}^n A_i &= \{x \ | \ \exists z(z \in A \land x \in z)\} \\
广义交 & & \bigcap_{i=1}^n A_i &= \{x \ | \ \forall z(z \in A \to x \in z)\} \\
\end{aligned}$$

1. $\displaystyle \bigcup \varnothing = \varnothing$，$\displaystyle \bigcap \varnothing$ 无意义
2. 广义运算减少集合的层次（括弧减少一层）
3. 广义运算的计算：一般情况下可以转变成初级运算

### 运算顺序
一类运算：广义并，广义交，幂集，绝对补，运算由右向左进行
二类运算：初级运算 $\cup$，$\cap$，$-$，$\oplus$，运算由左向右进行
混合运算：一类运算优先于二类运算

### 有穷集合的计数
1. 文氏图法
2. 包含排斥原理（容斥原理）
$$\begin{aligned}
\left| \overline{A_1} \cap \overline{A_2} \cap \cdots \cap \overline{A_n} \right| =& \left| E \right| \\ &- \sum_{i=1}^n \left| A_i \right| \\ &+ \sum_{1 \leq i < j \leq n} \left| A_i \cap A_j \right| \\ &- \cdots  \\ &+ (-1)^n \left| A_1 \cap A_2 \cap \cdots \cap A_n \right|
\end{aligned}$$
推论：$n$ 个集合的并的元素个数
$$\begin{aligned}
\left| A_1 \cup A_2 \cup \cdots \cup A_n \right| =& \sum_{i=1}^n \left| A_i \right| \\ &- \sum_{1 \leq i < j \leq n} \left| A_i \cap A_j \right| \\ &+ \cdots  \\ &+ (-1)^{n-1} \left| A_1 \cap A_2 \cap \cdots \cap A_n \right|
\end{aligned}$$

$$\left| A_1 \cup A_2 \cup \cdots \cup A_n \right| = \left|E\right| - \left| \overline{A_1} \cap \overline{A_2} \cap \cdots \cap \overline{A_n} \right|$$

## 集合恒等式
### 只涉及一个运算符的恒等式

| 运算律 |                 $\cup$                  |                 $\cap$                  |                    $\oplus$                     |
| :-: | :-------------------------------------: | :-------------------------------------: | :---------------------------------------------: |
| 交换律 |          $A \cup B = B \cup A$          |          $A \cap B = B \cap A$          |            $A \oplus B = B \oplus A$            |
| 结合律 | $(A \cup B) \cup C = A \cup (B \cup C)$ | $(A \cap B) \cap C = A \cap (B \cap C)$ | $(A \oplus B) \oplus C = A \oplus (B \oplus C)$ |
| 幂等律 |             $A \cup A = A$              |             $A \cap A = A$              |           $A \oplus A = \varnothing$            |

### 涉及两个不同运算符的恒等式

| 运算律 | $\cup$ 与 $\cap$ | $\cap$ 与 $\oplus$ |
| :-: | :--------------: | :----------------: |
| 分配律 | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ | $A \cap (B \oplus C) = (A \cap B) \oplus (A \cap C)$ |
| 吸收律 | $A \cup (A \cap B) = A$<br>$A \cap (A \cup B) = A$   | |

### 涉及补运算的恒等式

| 运算律 |                            $-$                            |                                                      $\sim$                                                      |
| :-: | :-------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------: |
| DM律 | $A - (B \cup C) = (A - B) \cap (A - C)$<br>$A - (B \cap C) = (A - B) \cup (A - C)$ | $\overline{A \cup B} = \overline{A} \cap \overline{B}$<br>$\overline{A \cap B} = \overline{A} \cup \overline{B}$<br>$\sim(B \cup C) = \sim B \cap \sim C$<br>$\sim(B \cap C) = \sim B \cup \sim C$ |
| 双重否定律 | | $\overline{\overline{A}} = A$, $\sim \sim A = A$ |

### 涉及空集和全集的恒等式 
| | $\varnothing$ | $E$ |
| :-: | :-----------: | :-: |
| 补元律 | $A \cap \sim A = \varnothing$ | $A \cup \sim A = E$ |
| 零律 | $A \cap \varnothing = \varnothing$ | $A \cup E = E$ |
| 同一律 | $A \cup \varnothing = A$ | $A \cap E = A$ |
| 否定律 | $\sim \varnothing = E$ | $\sim E = \varnothing$ |


## 集合等式的证明
### 命题演算法

例3  证明 $A \cup (A \cap B) = A$ （吸收律）

$$\begin{aligned}
\text{证：任取 } x\\
x \in A \cup (A \cap B) \Leftrightarrow &x \in A \lor x \in A \cap B \\
\Leftrightarrow &x \in A \lor (x \in A \land x \in B) \\
\Leftrightarrow &(x \in A \land x \in E) \lor (x \in A \land x \in B) \\
\Leftrightarrow &x \in A \land (x \in E \lor x \in B) \\
\Leftrightarrow &x \in A \\
\text{因此得 } A \cup (A \cap B) = A.
\end{aligned}$$

### 等式置换法
直接运用集合恒等式演算。

