---
id: arxiv_2603.29163v1
source: arxiv
topic: autonomous-driving
title: "SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving"
date: 2026-03-31
discovered: 2026-04-03
status: pending
---

# SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving

**Source:** arxiv
**Date:** 2026-03-31
**Authors:** Wenchao Sun, Xuewu Lin, Keyu Chen, Zixiang Pei, Xiang Li et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.29163v1)
- [PDF](https://arxiv.org/pdf/2603.29163v1)

## Abstract

End-to-end multi-modal planning has been widely adopted to model the uncertainty of driving behavior, typically by scoring candidate trajectories and selecting the optimal one. Existing approaches generally fall into two categories: scoring a large static trajectory vocabulary, or scoring a small set of dynamically generated proposals. While static vocabularies often suffer from coarse discretization of the action space, dynamic proposals provide finer-grained precision and have shown stronger empirical performance on existing benchmarks. However, it remains unclear whether dynamic generation is fundamentally necessary, or whether static vocabularies can already achieve comparable performance when they are sufficiently dense to cover the action space. In this work, we start with a systematic scaling study of Hydra-MDP, a representative scoring-based method, revealing that performance consistently improves as trajectory anchors become denser, without exhibiting saturation before computational constraints are reached. Motivated by this observation, we propose SparseDriveV2 to push the performance boundary of scoring-based planning through two complementary innovations: (1) a scalable vocabulary representation with a factorized structure that decomposes trajectories into geometric paths and velocity profiles, enabling combinatorial coverage of the action space, and (2) a scalable scoring strategy with coarse factorized scoring over paths and velocity profiles followed by fine-grained scoring on a small set of composed trajectories. By combining these two techniques, SparseDriveV2 achieves 92.0 PDMS and 90.1 EPDMS on NAVSIM, with 89.15 Driving Score and 70.00 Success Rate on Bench2Drive with a lightweight ResNet-34 as backbone. Code and model are released at https://github.com/swc-17/SparseDriveV2.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
