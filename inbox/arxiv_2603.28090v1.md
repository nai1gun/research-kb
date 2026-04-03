---
id: arxiv_2603.28090v1
source: arxiv
topic: autonomous-driving
title: "To View Transform or Not to View Transform: NeRF-based Pre-training Perspective"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# To View Transform or Not to View Transform: NeRF-based Pre-training Perspective

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Hyeonjun Jeong, Juyeb Shin, Dongsuk Kum
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28090v1)
- [PDF](https://arxiv.org/pdf/2603.28090v1)

## Abstract

Neural radiance fields (NeRFs) have emerged as a prominent pre-training paradigm for vision-centric autonomous driving, which enhances 3D geometry and appearance understanding in a fully self-supervised manner. To apply NeRF-based pretraining to 3D perception models, recent approaches have simply applied NeRFs to volumetric features obtained from view transformation. However, coupling NeRFs with view transformation inherits conflicting priors; view transformation imposes discrete and rigid representations, whereas radiance fields assume continuous and adaptive functions. When these opposing assumptions are forced into a single pipeline, the misalignment surfaces as blurry and ambiguous 3D representations that ultimately limit 3D scene understanding. Moreover, the NeRF network for pre-training is discarded during downstream tasks, resulting in inefficient utilization of enhanced 3D representations through NeRF. In this paper, we propose a novel NeRF-Resembled Point-based 3D detector that can learn continuous 3D representation and thus avoid the misaligned priors from view transformation. NeRP3D preserves the pre-trained NeRF network regardless of the tasks, inheriting the principle of continuous 3D representation learning and leading to greater potentials for both scene reconstruction and detection tasks. Experiments on nuScenes dataset demonstrate that our proposed approach significantly improves previous state-of-the-art methods, outperforming not only pretext scene reconstruction tasks but also downstream detection tasks.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
