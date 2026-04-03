---
id: arxiv_2604.01765v1
source: arxiv
topic: autonomous-driving
title: "DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning"
date: 2026-04-02
discovered: 2026-04-03
status: pending
---

# DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning

**Source:** arxiv
**Date:** 2026-04-02
**Authors:** Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01765v1)
- [PDF](https://arxiv.org/pdf/2604.01765v1)

## Abstract

Recently, world-action models (WAM) have emerged to bridge vision-language-action (VLA) models and world models, unifying their reasoning and instruction-following capabilities and spatio-temporal world modeling. However, existing WAM approaches often focus on modeling 2D appearance or latent representations, with limited geometric grounding-an essential element for embodied systems operating in the physical world. We present DriveDreamer-Policy, a unified driving world-action model that integrates depth generation, future video generation, and motion planning within a single modular architecture. The model employs a large language model to process language instructions, multi-view images, and actions, followed by three lightweight generators that produce depth, future video, and actions. By learning a geometry-aware world representation and using it to guide both future prediction and planning within a unified framework, the proposed model produces more coherent imagined futures and more informed driving actions, while maintaining modularity and controllable latency. Experiments on the Navsim v1 and v2 benchmarks demonstrate that DriveDreamer-Policy achieves strong performance on both closed-loop planning and world generation tasks. In particular, our model reaches 89.2 PDMS on Navsim v1 and 88.7 EPDMS on Navsim v2, outperforming existing world-model-based approaches while producing higher-quality future video and depth predictions. Ablation studies further show that explicit depth learning provides complementary benefits to video imagination and improves planning robustness.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
