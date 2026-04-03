---
id: arxiv_2604.00813v1
source: arxiv
topic: autonomous-driving
title: "DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale"
date: 2026-04-01
discovered: 2026-04-03
status: pending
---

# DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale

**Source:** arxiv
**Date:** 2026-04-01
**Authors:** Sicheng Zuo, Zixun Xie, Wenzhao Zheng, Shaoqing Xu, Fang Li et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.00813v1)
- [PDF](https://arxiv.org/pdf/2604.00813v1)

## Abstract

End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilitate planning. In this paper, we propose an alternative Vision-Geometry-Action (VGA) paradigm that advocates dense 3D geometry as the critical cue for autonomous driving. As vehicles operate in a 3D world, we think dense 3D geometry provides the most comprehensive information for decision-making. However, most existing geometry reconstruction methods (e.g., DVGT) rely on computationally expensive batch processing of multi-frame inputs and cannot be applied to online planning. To address this, we introduce a streaming Driving Visual Geometry Transformer (DVGT-2), which processes inputs in an online manner and jointly outputs dense geometry and trajectory planning for the current frame. We employ temporal causal attention and cache historical features to support on-the-fly inference. To further enhance efficiency, we propose a sliding-window streaming strategy and use historical caches within a certain interval to avoid repetitive computations. Despite the faster speed, DVGT-2 achieves superior geometry reconstruction performance on various datasets. The same trained DVGT-2 can be directly applied to planning across diverse camera configurations without fine-tuning, including closed-loop NAVSIM and open-loop nuScenes benchmarks.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
