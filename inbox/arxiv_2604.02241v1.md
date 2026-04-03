---
id: arxiv_2604.02241v1
source: arxiv
topic: autonomous-driving
title: "UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models"
date: 2026-04-02
discovered: 2026-04-03
status: pending
---

# UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models

**Source:** arxiv
**Date:** 2026-04-02
**Authors:** Qiyao Zhang, Shuhua Zheng, Jianli Sun, Chengxiang Li, Xianke Wu et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.02241v1)
- [PDF](https://arxiv.org/pdf/2604.02241v1)

## Abstract

Embodied visual tracking is crucial for Unmanned Aerial Vehicles (UAVs) executing complex real-world tasks. In dynamic urban scenarios with complex semantic requirements, Vision-Language-Action (VLA) models show great promise due to their cross-modal fusion and continuous action generation capabilities. To benchmark multimodal tracking in such environments, we construct a dedicated evaluation benchmark and a large-scale dataset encompassing over 890K frames, 176 tasks, and 85 diverse objects. Furthermore, to address temporal feature redundancy and the lack of spatial geometric priors in existing VLA models, we propose an improved VLA tracking model, UAV-Track VLA. Built upon the $π_{0.5}$ architecture, our model introduces a temporal compression net to efficiently capture inter-frame dynamics. Additionally, a parallel dual-branch decoder comprising a spatial-aware auxiliary grounding head and a flow matching action expert is designed to decouple cross-modal features and generate fine-grained continuous actions. Systematic experiments in the CARLA simulator validate the superior end-to-end performance of our method. Notably, in challenging long-distance pedestrian tracking tasks, UAV-Track VLA achieves a 61.76\% success rate and 269.65 average tracking frames, significantly outperforming existing baselines. Furthermore, it demonstrates robust zero-shot generalization in unseen environments and reduces single-step inference latency by 33.4\% (to 0.0571s) compared to the original $π_{0.5}$, enabling highly efficient, real-time UAV control. Data samples and demonstration videos are available at: https://github.com/Hub-Tian/UAV-Track\_VLA.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
