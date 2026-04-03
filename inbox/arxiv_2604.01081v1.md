---
id: arxiv_2604.01081v1
source: arxiv
topic: autonomous-driving
title: "ProOOD: Prototype-Guided Out-of-Distribution 3D Occupancy Prediction"
date: 2026-04-01
discovered: 2026-04-03
status: pending
---

# ProOOD: Prototype-Guided Out-of-Distribution 3D Occupancy Prediction

**Source:** arxiv
**Date:** 2026-04-01
**Authors:** Yuheng Zhang, Mengfei Duan, Kunyu Peng, Yuhang Wang, Di Wen et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01081v1)
- [PDF](https://arxiv.org/pdf/2604.01081v1)

## Abstract

3D semantic occupancy prediction is central to autonomous driving, yet current methods are vulnerable to long-tailed class bias and out-of-distribution (OOD) inputs, often overconfidently assigning anomalies to rare classes. We present ProOOD, a lightweight, plug-and-play method that couples prototype-guided refinement with training-free OOD scoring. ProOOD comprises (i) prototype-guided semantic imputation that fills occluded regions with class-consistent features, (ii) prototype-guided tail mining that strengthens rare-class representations to curb OOD absorption, and (iii) EchoOOD, which fuses local logit coherence with local and global prototype matching to produce reliable voxel-level OOD scores. Extensive experiments on five datasets demonstrate that ProOOD achieves state-of-the-art performance on both in-distribution 3D occupancy prediction and OOD detection. On SemanticKITTI, it surpasses baselines by +3.57% mIoU overall and +24.80% tail-class mIoU; on VAA-KITTI, it improves AuPRCr by +19.34 points, with consistent gains across benchmarks. These improvements yield more calibrated occupancy estimates and more reliable OOD detection in safety-critical urban driving. The source code is publicly available at https://github.com/7uHeng/ProOOD.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
