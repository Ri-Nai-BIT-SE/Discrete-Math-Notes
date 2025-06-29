---
author: Ri-Nai
categories:
- 学习笔记
date: '2025-01-07T12:18:45+08:00'
description: null
draft: false
hidden: true
lastmod: '2025-01-07T12:18:45+08:00'
license: null
math: null
slug: 01 06 《离散数学》复习笔记/图论/二部图
tags:
- 离散数学
- 计算机科学
title: 二部图
---

# 二部图


## 二部图
$G = \langle V, E \rangle$ 为无向图，若 $V$ 可分为两个互不相交的子集 $V_1$ 和 $V_2$，使得 $E$ 中的每条边的两个端点分别属于 $V_1$ 和 $V_2$，则称 $G$ 为**二部图**（也称**二分图** 或 **偶图**）。  
称 $V_1$ 和 $V_2$ 为 $G$ 的**互补顶点子集**。  
常将二部图记作 $G = \langle V_1, V_2, E \rangle$。  

### 完全二部图
$\forall v_1 \in V_1, v_2 \in V_2$，$(v_1, v_2) \in E$，则称 $G$ 为**完全二部图**。
记为 $K_{r, s}$，其中 $r = |V_1|$，$s = |V_2|$。

### 二部图的判定
$G$ 为二部图当且仅当 $G$ 中不含**奇圈**。

