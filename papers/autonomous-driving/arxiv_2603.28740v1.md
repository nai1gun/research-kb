---
id: arxiv_2603.28740v1
source: arxiv
topic: autonomous-driving
title: "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# FocusVLA: Focused Visual Utilization for Vision-Language-Action Models

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28740v1)
- [PDF](https://arxiv.org/pdf/2603.28740v1)

## Abstract

Vision-Language-Action (VLA) models improve action generation by conditioning policies on rich vision-language information. However, current auto-regressive policies are constrained by three bottlenecks: (1) architectural bias drives models to overlook visual details, (2) an excessive number of visual tokens makes attention difficult to focus on the correct regions, and (3) task-irrelevant visual information introduces substantial noise - together severely impairing the quality of action. In this paper, we investigate how to effectively utilize different visual representations for action generation. To this end, we first empirically validate the above issues and show that VLA performance is primarily limited by how visual information is utilized, rather than by the quality of visual representations. Based on these insights, we introduce FocusVLA, a novel paradigm that directs the model's attention to task-relevant visual regions to effectively bridge vision to action. Specifically, we first propose Modality Cascaded Attention to eliminate shortcut pathways, thereby compelling VLA models to rely on task-relevant visual details for action generation. Furthermore, we propose Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that FocusVLA not only effectively leverages visual details to perform dexterous manipulations, but also substantially improves performance and accelerates convergence across a variety of tasks.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
