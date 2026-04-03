---
id: arxiv_2603.27818v1
source: arxiv
topic: autonomous-driving
title: "Benchmarking Multi-View BEV Object Detection with Mixed Pinhole and Fisheye Cameras"
date: 2026-03-29
discovered: 2026-04-03
status: pending
---

# Benchmarking Multi-View BEV Object Detection with Mixed Pinhole and Fisheye Cameras

**Source:** arxiv
**Date:** 2026-03-29
**Authors:** Xiangzhong Liu, Hao Shen
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.27818v1)
- [PDF](https://arxiv.org/pdf/2603.27818v1)

## Abstract

Modern autonomous driving systems increasingly rely on mixed camera configurations with pinhole and fisheye cameras for full view perception. However, Bird's-Eye View (BEV) 3D object detection models are predominantly designed for pinhole cameras, leading to performance degradation under fisheye distortion. To bridge this gap, we introduce a multi-view BEV detection benchmark with mixed cameras by converting KITTI-360 into nuScenes format. Our study encompasses three adaptations: rectification for zero-shot evaluation and fine-tuning of nuScenes-trained models, distortion-aware view transformation modules (VTMs) via the MEI camera model, and polar coordinate representations to better align with radial distortion. We systematically evaluate three representative BEV architectures, BEVFormer, BEVDet and PETR, across these strategies. We demonstrate that projection-free architectures are inherently more robust and effective against fisheye distortion than other VTMs. This work establishes the first real-data 3D detection benchmark with fisheye and pinhole images and provides systematic adaptation and practical guidelines for designing robust and cost-effective 3D perception systems. The code is available at https://github.com/CesarLiu/FishBEVOD.git.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
