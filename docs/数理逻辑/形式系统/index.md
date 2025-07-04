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
slug: 01 06 《离散数学》复习笔记/数理逻辑/形式系统
tags:
- 离散数学
- 计算机科学
title: 形式系统
---

# 形式系统

定义 3.2 介绍了**形式系统**（formal system）的组成及其分类，形式系统通常用于刻画形式化逻辑和数学推理的规则结构。下面是对定义 3.2 的详细解释：

## 1. **形式系统 I 的组成部分**

形式系统$I$是由以下四个部分构成的集合：

### (1) **字母表 A(I)** 
这是形式系统中的符号集合，通常是一个非空集合，表示构成系统中表达式或公式的基本符号。这个集合中的符号可以包括变量、常数、逻辑符号（如$\wedge$和$\vee$）、关系符号、函数符号等。

- **记作**：$A(I)$
- **作用**：字母表中的符号是构建系统中合式公式（well-formed formulas, WFF）的基本成分。
  
### (2) **合式公式集 E(I)**
合式公式集是由字母表中的符号通过一定的语法规则构造出来的公式集合。只有符合语法规则的符号组合才能称为合式公式。

- **记作**：$E(I)$
- **作用**：合式公式是形式系统中的合法表达式。系统的推理与演算都基于这些合式公式进行。
- **例子**：在一阶逻辑中，合式公式可以是像$P(x)$,$x = y$这样的符号组合。

### (3) **公理集 AX(I)**
公理集是合式公式集中的某些特殊公式，这些公式不需要通过推理规则推导而来，而是被直接假设为系统的基础命题。公理是形式系统中推理的起点，所有的推导都从公理出发。

- **记作**：$AX(I)$
- **作用**：公理是形式系统的基础，它们是被直接假设为真、不需要证明的公式。
- **例子**：在算术公理系统中，像“零不是任何数的后继”这样的命题可以作为公理。

### (4) **推理规则集 R(I)**
推理规则是形式系统中从一个或多个已知公式（前提）推导出新公式（结论）的规则。推理规则规定了在什么条件下，合式公式之间的关系可以被用于推导新的公式。

- **记作**：$R(I)$
- **作用**：推理规则定义了系统内的推导方式，确保从公理或之前推导出的结论能够生成新的定理。
- **例子**：最常见的推理规则之一是**蕴涵分离规则**，如果$A \to B$和$A$都成立，则可以推导出$B$。

## 2. **形式语言系统和形式演算系统**

形式系统$I$可以进一步分为两部分：

- **形式语言系统**：$\langle A(I), E(I) \rangle$
    - 这部分定义了系统中的符号（字母表）和如何用这些符号构造合法的表达式（合式公式）。
  
- **形式演算系统**：$\langle AX(I), R(I) \rangle$
    - 这部分定义了系统中的公理和推理规则。通过这些规则和公理，系统可以推导出新的结论。

## 3. **形式系统的两类：自然推理系统与公理推理系统**

根据公理集是否为空，可以将形式系统分为两类：

### (1) **自然推理系统**
在自然推理系统中，**没有公理**，即$AX(I) = \emptyset$。这种系统依赖于推理规则，从前提（假设）出发进行推导，通常用于更自由和直观的推理过程。

- **特点**：没有预设的真命题（公理），一切推导都是从假设出发。

### (2) **公理推理系统**
在公理推理系统中，推导是从公理和推理规则出发的，推导出的结论通常被称为**定理**（theorems）。这些定理可以看作是公理的逻辑后果。

- **特点**：推导从公理开始，所有的结论都是基于公理通过推理规则得出的。
- **定理**：在公理推理系统中，系统中所有推导出的结论都被称为定理。每个定理都是公理的逻辑推论。

## 4. **形式系统的应用**

形式系统广泛应用于数学、逻辑、计算机科学中的形式化推理，如：

- **命题逻辑与一阶逻辑**：通过公理和推理规则，形式化地描述逻辑推理过程。
- **证明论**：分析数学定理的推导过程，形式化研究证明的结构。
- **计算机科学中的自动定理证明**：利用形式系统推导定理，验证程序的正确性。

## 总结
形式系统$I$是一套形式化的规则系统，用来定义符号、构造公式、设定公理，并通过推理规则进行推导。不同的形式系统有不同的结构，公理推理系统通过设定公理来推导定理，而自然推理系统则没有公理，仅通过推理规则进行推导。
