---
id: arxiv_2603.28233v1
source: arxiv
topic: autonomous-driving
title: "TwinMixing: A Shuffle-Aware Feature Interaction Model for Multi-Task Segmentation"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# TwinMixing: A Shuffle-Aware Feature Interaction Model for Multi-Task Segmentation

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Minh-Khoi Do, Huy Che, Dinh-Duy Phan, Duc-Khai Lam, Duc-Lung Vu
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28233v1)
- [PDF](https://arxiv.org/pdf/2603.28233v1)

## Abstract

Accurate and efficient perception is essential for autonomous driving, where segmentation tasks such as drivable-area and lane segmentation provide critical cues for motion planning and control. However, achieving high segmentation accuracy while maintaining real-time performance on low-cost hardware remains a challenging problem. To address this issue, we introduce TwinMixing, a lightweight multi-task segmentation model designed explicitly for drivable-area and lane segmentation. The proposed network features a shared encoder and task-specific decoders, enabling both feature sharing and task specialization. Within the encoder, we propose an Efficient Pyramid Mixing (EPM) module that enhances multi-scale feature extraction through a combination of grouped convolutions, depthwise dilated convolutions and channel shuffle operations, effectively expanding the receptive field while minimizing computational cost. Each decoder adopts a Dual-Branch Upsampling (DBU) Block composed of a learnable transposed convolution-based Fine detailed branch and a parameter-free bilinear interpolation-based Coarse grained branch, achieving detailed yet spatially consistent feature reconstruction. Extensive experiments on the BDD100K dataset validate the effectiveness of TwinMixing across three configurations - tiny, base, and large. Among them, the base configuration achieves the best trade-off between accuracy and computational efficiency, reaching 92.0% mIoU for drivable-area segmentation and 32.3% IoU for lane segmentation with only 0.43M parameters and 3.95 GFLOPs. Moreover, TwinMixing consistently outperforms existing segmentation models on the same tasks, as illustrated in Fig. 1. Thanks to its compact and modular design, TwinMixing demonstrates strong potential for real-time deployment in autonomous driving and embedded perception systems. The source code: https://github.com/Jun0se7en/TwinMixing.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
