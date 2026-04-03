---
id: arxiv_2603.28565v1
source: arxiv
topic: autonomous-driving
title: "StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Yiran Shi, Dongqi Guo, Tianchen Zhao, Feng Gao, Liangzhi Shi et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28565v1)
- [PDF](https://arxiv.org/pdf/2603.28565v1)

## Abstract

Vision-language-action (VLA) models have demonstrated exceptional performance in natural language-driven perception and control. However, the high computational cost of VLA models poses significant efficiency challenges, particularly for resource-constrained edge platforms in real-world deployments. However, since different stages of VLA (observation, action generation and execution) must proceed sequentially, and wait for the completion of the preceding stage, the system suffers from frequent halting and high latency. To address this, We conduct a systematic analysis to identify the challenges for fast and fluent generation, and propose enabling VLAs with the ability to asynchronously parallelize across VLA stages in a "streaming" manner. First, we eliminate the reliance on action chunking and adopt action flow matching, which learns the trajectory of action flows rather than denoising chunk-wise actions. It overlaps the latency of action generation and execution. Second, we design an action saliency-aware adaptive observation mechanism, thereby overlapping the latency of execution and observation. Without sacrificing performance, StreamingVLA achieves substantial speedup and improves the fluency of execution. It achieves a 2.4 $\times$ latency speedup and reduces execution halting by 6.5 $\times$.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
