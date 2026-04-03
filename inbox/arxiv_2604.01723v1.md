---
id: arxiv_2604.01723v1
source: arxiv
topic: autonomous-driving
title: "Causal Scene Narration with Runtime Safety Supervision for Vision-Language-Action Driving"
date: 2026-04-02
discovered: 2026-04-03
status: pending
---

# Causal Scene Narration with Runtime Safety Supervision for Vision-Language-Action Driving

**Source:** arxiv
**Date:** 2026-04-02
**Authors:** Yun Li, Yidu Zhang, Simon Thompson, Ehsan Javanmardi, Manabu Tsukada
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01723v1)
- [PDF](https://arxiv.org/pdf/2604.01723v1)

## Abstract

Vision-Language-Action (VLA) models for autonomous driving must integrate diverse textual inputs, including navigation commands, hazard warnings, and traffic state descriptions, yet current systems often present these as disconnected fragments, forcing the model to discover on its own which environmental constraints are relevant to the current maneuver. We introduce Causal Scene Narration (CSN), which restructures VLA text inputs through intent-constraint alignment, quantitative grounding, and structured separation, at inference time with zero GPU cost. We complement CSN with Simplex-based runtime safety supervision and training-time alignment via Plackett-Luce DPO with negative log-likelihood (NLL) regularization. A multi-town closed-loop CARLA evaluation shows that CSN improves Driving Score by +31.1% on original LMDrive and +24.5% on the preference-aligned variant. A controlled ablation reveals that causal structure accounts for 39.1% of this gain, with the remainder attributable to information content alone. A perception noise ablation confirms that CSN's benefit is robust to realistic sensing errors. Semantic safety supervision improves Infraction Score, while reactive Time-To-Collision monitoring degrades performance, demonstrating that intent-aware monitoring is needed for VLA systems.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
