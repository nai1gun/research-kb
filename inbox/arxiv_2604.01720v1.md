---
id: arxiv_2604.01720v1
source: arxiv
topic: autonomous-driving
title: "Hi-LOAM: Hierarchical Implicit Neural Fields for LiDAR Odometry and Mapping"
date: 2026-04-02
discovered: 2026-04-03
status: pending
---

# Hi-LOAM: Hierarchical Implicit Neural Fields for LiDAR Odometry and Mapping

**Source:** arxiv
**Date:** 2026-04-02
**Authors:** Zhiliu Yang, Jianyuan Zhang, Lianhui Zhao, Jinyu Dai, Zhu Yang
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01720v1)
- [PDF](https://arxiv.org/pdf/2604.01720v1)

## Abstract

LiDAR Odometry and Mapping (LOAM) is a pivotal technique for embodied-AI applications such as autonomous driving and robot navigation. Most existing LOAM frameworks are either contingent on the supervision signal, or lack of the reconstruction fidelity, which are deficient in depicting details of large-scale complex scenes. To overcome these limitations, we propose a multi-scale implicit neural localization and mapping framework using LiDAR sensor, called Hi-LOAM. Hi-LOAM receives LiDAR point cloud as the input data modality, learns and stores hierarchical latent features in multiple levels of hash tables based on an octree structure, then these multi-scale latent features are decoded into signed distance value through shallow Multilayer Perceptrons (MLPs) in the mapping procedure. For pose estimation procedure, we rely on a correspondence-free, scan-to-implicit matching paradigm to estimate optimal pose and register current scan into the submap. The entire training process is conducted in a self-supervised manner, which waives the model pre-training and manifests its generalizability when applied to diverse environments. Extensive experiments on multiple real-world and synthetic datasets demonstrate the superior performance, in terms of the effectiveness and generalization capabilities, of our Hi-LOAM compared to existing state-of-the-art methods.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
