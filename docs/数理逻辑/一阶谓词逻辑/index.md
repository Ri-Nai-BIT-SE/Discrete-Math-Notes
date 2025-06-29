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
slug: 01 06 《离散数学》复习笔记/数理逻辑/一阶谓词逻辑
tags:
- 离散数学
- 计算机科学
title: 一阶谓词逻辑
---

# 一阶谓词逻辑

## 一阶逻辑命题符号化
### 客体
- **客体**：客观存在的实体，如人、物、事物等。
- **个体词**：所研究对象中独立存在的客体。
    - **个体常项**：具体的事物，用 $a$ 、 $b$ 、 $c$ 等表示 。
    - **个体变项**：抽象的事物，用 $x$ 、 $y$ 、 $z$ 等表示。
- **个体域**：个体变项的取值范围。
    - **有限个体域**：如 $\{a,b,c\}$，$\{1, 2\}$ 等。
    - **无限个体域**：如全体自然数 $\mathbb{N}$，全体实数 $\mathbb{R}$ 等。
    - **全总个体域**：由宇宙间一切事物组成的个体域。

### 谓词
- **谓词**：对客体的性质、特征、关系等进行描述的符号。常用大写字母表示，如 $P$ 、 $Q$ 、 $R$ 等。
例如 $A(x)$ 表示 $x$ 满足性质 $A$。
    - **谓词常项**：如，$F(a):a$ 是男性。
    - **谓词变项**：如，$F(x):x$ 是男性。
    - $n$ 元谓词：含有 $n$ 个变项的谓词。 
        - 一元谓词：表示一个客体的性质。
        - 多元谓词：表示多个客体之间的关系。
        - 零元谓词：不含个体变项的谓词，即命题常项或命题变项。

### 量词
$\forall$ 和 $\exists$ 称为**量词**。
- **全称量词**：$\forall$，表示“对任意”、“对一切”。
- **存在量词**：$\exists$，表示“存在”、“至少有一个”。
如 $\forall x P(x)$ 表示“对任意 $x$，$x$ 满足性质 $P$”。

对于 $\forall$ 用 $\to$ 而不是 $\land$
对于 $\exists$ 用 $\land$ 而不是 $\to$

### 变元的约束
在公式 $\forall x A$ 和 $\exists x A$ 中，$x$ 称为**指导变元**，$A$ 为对应量词的 **辖域**。
在辖域内，$x$ 称为**约束出现**，$A$ 中不是约束出现的其他变项称为**自由出现**。
若 $A$ 中没有自由出现的变项，则称 $A$ 为**闭式**。

## [公式的解释](../公式的解释/)

若公式在任何解释和该解释下的任何赋值下都为真，则称该公式为**永真式**。
若公式在任何解释和该解释下的任何赋值下都为假，则称该公式为**永假式**。
若公式在某个解释和该解释下的某个赋值下为真，则称该公式为**可满足式**。

一阶逻辑公式是不可判定的，即无法判断一个公式是否永真、永假或可满足。


### 代换实例
设 $A_0$ 是含命题变项 $p_1, p_2, \ldots, p_n$ 的命题公式，$A_1, A_2, \ldots, A_n$ 是 $n$ 个谓词公式，用 $A_i$ ($1 \leq i \leq n$) 处处代替 $A_0$ 中的 $p_i$，所得公式 $A$ 称为 $A_0$ 的代换实例。

例如，$F(x) \to G(x)$，$\forall x F(x) \to \exists y G(y)$ 等都是 $p \to q$ 的代换实例。

重言式的代换实例都是永真式，矛盾式的代换实例都是矛盾式。

## 一阶逻辑的等值演算与推理
### 基本等值式
#### 命题逻辑的基本等值式
[基本等值式](../命题逻辑/#基本等值式)在一阶逻辑中仍然成立，如双重否定律、德摩根律等。需要代换实例。

#### 量词的等值式
##### 消去量词等值式
设 $D = \{ a_1, a_2, \ldots, a_n \}$
1. $\forall x A(x) \Leftrightarrow A(a_1) \land A(a_2) \land \cdots \land A(a_n)$
2. $\exists x A(x) \Leftrightarrow A(a_1) \lor A(a_2) \lor \cdots \lor A(a_n)$

##### 量词否定等值式
1. $\neg \forall x A(x) \Leftrightarrow \exists x \neg A(x)$
2. $\neg \exists x A(x) \Leftrightarrow \forall x \neg A(x)$

##### 量词辖域收缩与扩张等值式
$A(x)$ 是含 $x$ 的自由出现的公式，$B$ 中不含 $x$ 的自由出现的公式。

- 关于全称量词的：
    - $\forall x (A(x) \land B) \Leftrightarrow \forall x A(x) \land B$
    - $\forall x (A(x) \lor B) \Leftrightarrow \forall x A(x) \lor B$
    - $\textcolor{orange}{\forall x} (A(x) \to B) \Leftrightarrow \textcolor{orange}{\exists x} A(x) \to B$
    - $\forall x (B \to A(x)) \Leftrightarrow B \to \forall x A(x)$

- 关于存在量词的：
    - $\exists x (A(x) \land B) \Leftrightarrow \exists x A(x) \land B$
    - $\exists x (A(x) \lor B) \Leftrightarrow \exists x A(x) \lor B$
    - $\textcolor{orange}{\exists x} (A(x) \to B) \Leftrightarrow \textcolor{orange}{\forall x} A(x) \to B$
    - $\exists x (B \to A(x)) \Leftrightarrow B \to \exists x A(x)$

##### 量词分配等值式
- $\forall x (A(x) \land B(x)) \Leftrightarrow \forall x A(x) \land \forall x B(x)$
- $\exists x (A(x) \lor B(x)) \Leftrightarrow \exists x A(x) \lor \exists x B(x)$
- $\exists x (A(x) \to B(x)) \Leftrightarrow \forall x A(x) \to \exists x B(x)$

形式类似的重演蕴含式
- $\forall x (A(x) \lor B(x)) \Leftarrow \forall x A(x) \lor \forall x B(x)$
- $\exists x (A(x) \land B(x)) \Rightarrow \exists x A(x) \land \exists x B(x)$
- $$\begin{aligned}\exists x A(x) \to \forall x B(x) &\Rightarrow \forall x (A(x) \to B(x)) \\ \Rightarrow \forall x A(x) \to \forall x B(x) &\Rightarrow \exists x A(x) \to \exists x B(x)\end{aligned}$$


### 置换规则、换名规则、代替规则
#### 置换规则
若 $A \Leftrightarrow B$ 则 $F(A) \Leftrightarrow F(B)$

#### 换名规则
将公式 $A$ 中某量词辖域内的所有**约束变元**替换为该辖域中**未出现**的个体变项符号，得到的公式 $A'$ 与 $A$ 等值。

#### 代替规则
设 $A$ 为一公式，将 $A$ 中的某个自由出现的变项用未曾出现在 $A$ 中的个体常项符号代替，得到的公式 $A'$ 与 $A$ 等值。



## 一阶逻辑前束范式
设 $A$ 为一阶逻辑公式，若 $A$ 的量词部分出现在公式的最前面，则称 $A$ 为**前束范式**。即 $A$ 可以表示为：
$$Q_1 x_1 Q_2 x_2 \cdots Q_n x_n B$$
其中 $Q_i$ 为量词，$x_i$ 为变项，$B$ 为不含量词的公式。

一阶逻辑中的任何公式都存在与之等值的前束范式

## 一阶逻辑的推理理论
### 量词规则
1. US：全称引入规则（Universal Specification）
   $$\forall x A(x) \Rightarrow A(c)$$
2. UG：全称推广规则（Universal Generalization）
   $$A(c) \Rightarrow \forall x A(x)$$
3. ES：存在引入规则（Existential Specification）
   $$A(c) \Rightarrow \exists x A(x)$$
4. EG：存在推广规则（Existential Generalization）
   $$\exists x A(x) \Rightarrow A(c)$$

### 自然推理系统
定义5.3 自然推理系统 $N_\mathcal{L}$ 定义如下：
1. 字母表：同一阶语言 $\mathcal{L}$ 的字母表。
2. 合式公式：同 $\mathcal{L}$ 的合式公式。
3. 推理规则：[基本等值式](#基本等值式)、[量词规则](#量词规则)。

