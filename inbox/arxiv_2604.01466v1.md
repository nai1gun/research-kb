---
id: arxiv_2604.01466v1
source: arxiv
topic: autonomous-driving
title: "Efficient Equivariant Transformer for Self-Driving Agent Modeling"
date: 2026-04-01
discovered: 2026-04-03
status: pending
---

# Efficient Equivariant Transformer for Self-Driving Agent Modeling

**Source:** arxiv
**Date:** 2026-04-01
**Authors:** Scott Xu, Dian Chen, Kelvin Wong, Chris Zhang, Kion Fallah et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01466v1)
- [PDF](https://arxiv.org/pdf/2604.01466v1)

## Abstract

Accurately modeling agent behaviors is an important task in self-driving. It is also a task with many symmetries, such as equivariance to the order of agents and objects in the scene or equivariance to arbitrary roto-translations of the entire scene as a whole; i.e., SE(2)-equivariance. The transformer architecture is a ubiquitous tool for modeling these symmetries. While standard self-attention is inherently permutation equivariant, explicit pairwise relative positional encodings have been the standard for introducing SE(2)-equivariance. However, this approach introduces an additional cost that is quadratic in the number of agents, limiting its scalability to larger scenes and batch sizes. In this work, we propose DriveGATr, a novel transformer-based architecture for agent modeling that achieves SE(2)-equivariance without the computational cost of existing methods. Inspired by recent advances in geometric deep learning, DriveGATr encodes scene elements as multivectors in the 2D projective geometric algebra $\mathbb{R}^*_{2,0,1}$ and processes them with a stack of equivariant transformer blocks. Crucially, DriveGATr models geometric relationships using standard attention between multivectors, eliminating the need for costly explicit pairwise relative positional encodings. Experiments on the Waymo Open Motion Dataset demonstrate that DriveGATr is comparable to the state-of-the-art in traffic simulation and establishes a superior Pareto front for performance vs computational cost.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
