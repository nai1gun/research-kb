---
id: arxiv_2603.27995v1
source: arxiv
topic: autonomous-driving
title: "UniDA3D: A Unified Domain-Adaptive Framework for Multi-View 3D Object Detection"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# UniDA3D: A Unified Domain-Adaptive Framework for Multi-View 3D Object Detection

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Hongjing Wu, Cheng Chi, Jinlin Wu, Yanzhao Su, Zhen Lei et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.27995v1)
- [PDF](https://arxiv.org/pdf/2603.27995v1)

## Abstract

Camera-only 3D object detection is critical for autonomous driving, offering a cost-effective alternative to LiDAR based methods. In particular, multi-view 3D object detection has emerged as a promising direction due to its balanced trade-off between performance and cost. However, existing methods often suffer significant performance degradation under complex environmental conditions such as nighttime, fog, and rain, primarily due to their reliance on training data collected mostly in ideal conditions. To address this challenge, we propose UniDA3D, a unified domain-adaptive multi-view 3D object detector designed for robust perception under diverse adverse conditions. UniDA3D formulates nighttime, rainy, and foggy scenes as a unified multi target domain adaptation problem and leverages a novel query guided domain discrepancy mitigation (QDDM) module to align object features between source and target domains at both batch and global levels via query-centric adversarial and contrastive learning. Furthermore, we introduce a domain-adaptive teacher student training pipeline with an exponential-moving-average teacher and dynamically updated high-quality pseudo labels to enhance consistency learning and suppress background noise in unlabeled target domains. In contrast to prior approaches that require separate training for each condition, UniDA3D performs a single unified training process across multiple domains, enabling robust all-weather 3D perception. On a synthesized multi-view 3D benchmark constructed by generating nighttime, rainy, and foggy counterparts from nuScenes (nuScenes-Night, nuScenes-Rain, and nuScenes-Haze), UniDA3D consistently outperforms state of-the-art camera-only multi-view 3D detectors under extreme conditions, achieving substantial gains in mAP and NDS while maintaining real-time inference efficiency.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
