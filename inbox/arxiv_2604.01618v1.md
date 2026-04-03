---
id: arxiv_2604.01618v1
source: arxiv
topic: autonomous-driving
title: "Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models"
date: 2026-04-02
discovered: 2026-04-03
status: pending
---

# Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models

**Source:** arxiv
**Date:** 2026-04-02
**Authors:** Jiawei Chen, Simin Huang, Jiawei Du, Shuaihang Chen, Yu Tian et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01618v1)
- [PDF](https://arxiv.org/pdf/2604.01618v1)

## Abstract

Vision-language-action (VLA) models have shown strong performance in robotic manipulation, yet their robustness to physically realizable adversarial attacks remains underexplored. Existing studies reveal vulnerabilities through language perturbations and 2D visual attacks, but these attack surfaces are either less representative of real deployment or limited in physical realism. In contrast, adversarial 3D textures pose a more physically plausible and damaging threat, as they are naturally attached to manipulated objects and are easier to deploy in physical environments. Bringing adversarial 3D textures to VLA systems is nevertheless nontrivial. A central obstacle is that standard 3D simulators do not provide a differentiable optimization path from the VLA objective function back to object appearance, making it difficult to optimize through an end-to-end manner. To address this, we introduce Foreground-Background Decoupling (FBD), which enables differentiable texture optimization through dual-renderer alignment while preserving the original simulation environment. To further ensure that the attack remains effective across long-horizon and diverse viewpoints in the physical world, we propose Trajectory-Aware Adversarial Optimization (TAAO), which prioritizes behaviorally critical frames and stabilizes optimization with a vertex-based parameterization. Built on these designs, we present Tex3D, the first framework for end-to-end optimization of 3D adversarial textures directly within the VLA simulation environment. Experiments in both simulation and real-robot settings show that Tex3D significantly degrades VLA performance across multiple manipulation tasks, achieving task failure rates of up to 96.7\%. Our empirical results expose critical vulnerabilities of VLA systems to physically grounded 3D adversarial attacks and highlight the need for robustness-aware training.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
