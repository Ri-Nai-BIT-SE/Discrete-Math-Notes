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
slug: 01 06 《离散数学》复习笔记/图论/扩大路径法
tags:
- 离散数学
- 计算机科学
title: 扩大路径法
---

# 扩大路径法

$G = \langle V, E \rangle$ 为无向图，且 $E \neq \varnothing$，取一条初始路径 $\varGamma_l$，将该路径外与该路径的**始点**和**终点**相邻的顶点加入路径，得到新路径 $\varGamma_{l+1}$，重复该过程，直到无法再加入新的顶点为止。  
最后得到的路径为 $\varGamma_{l + k}$，称为**极大路径**。  
使用该方法证明问题的方法称为**扩大路径法**。  
