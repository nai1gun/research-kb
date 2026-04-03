---
id: arxiv_2604.01570v1
source: arxiv
topic: autonomous-driving
title: "Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior"
date: 2026-04-02
discovered: 2026-04-03
status: pending
---

# Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior

**Source:** arxiv
**Date:** 2026-04-02
**Authors:** Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01570v1)
- [PDF](https://arxiv.org/pdf/2604.01570v1)

## Abstract

In real-world robotic manipulation, states typically admit a neighborhood of near-equivalent actions. That is, for each state, there exist a feasible action neighborhood (FAN) rather than a single correct action, within which motions yield indistinguishable progress. However, prevalent VLA training methodologies are directly inherited from linguistic settings and do not exploit the FAN property, thus leading to poor generalization and low sample efficiency. To address this limitation, we introduce a FAN-guided regularizer that shapes the model's output distribution to align with the geometry of FAN. Concretely, we introduce a Gaussian prior that promotes locally smooth and unimodal predictions around the preferred direction and magnitude. In extensive experiments across both reinforced finetuning (RFT) and supervised finetuning (SFT), our method achieves significant improvement in sample efficiency, and success rate in both in-distribution and out-of-distribution (OOD) scenarios. By aligning with the intrinsic action tolerance of physical manipulation, FAN-guided regularization provides a principled and practical method for sample-efficient, and generalizable VLA adaptation.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
