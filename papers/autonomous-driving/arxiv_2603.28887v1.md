---
id: arxiv_2603.28887v1
source: arxiv
topic: autonomous-driving
title: "OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Tianran Liu, Shengwen Zhao, Mozhgan Pourkeshavarz, Weican Li, Nicholas Rhinehart
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28887v1)
- [PDF](https://arxiv.org/pdf/2603.28887v1)

## Abstract

Data-driven autonomous driving simulation has long been constrained by its heavy reliance on pre-recorded driving logs or spatial priors, such as HD maps. This fundamental dependency severely limits scalability, restricting open-ended generation capabilities to the finite scale of existing collected datasets. To break this bottleneck, we present OccSim, the first occupancy world model-driven 3D simulator. OccSim obviates the requirement for continuous logs or HD maps; conditioned only on a single initial frame and a sequence of future ego-actions, it can stably generate over 3,000 continuous frames, enabling the continuous construction of large-scale 3D occupancy maps spanning over 4 kilometers for simulation. This represents an >80x improvement in stable generation length over previous state-of-the-art occupancy world models. OccSim is powered by two modules: W-DiT based static occupancy world model and the Layout Generator. W-DiT handles the ultra-long-horizon generation of static environments by explicitly introducing known rigid transformations in architecture design, while the Layout Generator populates the dynamic foreground with reactive agents based on the synthesized road topology. With these designs, OccSim can synthesize massive, diverse simulation streams. Extensive experiments demonstrate its downstream utility: data collected directly from OccSim can pre-train 4D semantic occupancy forecasting models to achieve up to 67% zero-shot performance on unseen data, outperforming previous asset-based simulator by 11%. When scaling the OccSim dataset to 5x the size, the zero-shot performance increases to about 74%, while the improvement over asset-based simulators expands to 22.1%.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
