---
id: arxiv_2603.28963v1
source: arxiv
topic: autonomous-driving
title: "AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Mozhgan Pourkeshavatz, Tianran Liu, Nicholas Rhinehart
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28963v1)
- [PDF](https://arxiv.org/pdf/2603.28963v1)

## Abstract

Multi-agent traffic simulation is central to developing and testing autonomous driving systems. Recent data-driven simulators have achieved promising results, but rely heavily on supervised learning from labeled trajectories or semantic annotations, making it costly to scale their performance. Meanwhile, large amounts of unlabeled sensor data can be collected at scale but remain largely unused by existing traffic simulation frameworks. This raises a key question: How can a method harness unlabeled data to improve traffic simulation performance? In this work, we propose AutoWorld, a traffic simulation framework that employs a world model learned from unlabeled occupancy representations of LiDAR data. Given world model samples, AutoWorld constructs a coarse-to-fine predictive scene context as input to a multi-agent motion generation model. To promote sample diversity, AutoWorld uses a cascaded Determinantal Point Process framework to guide the sampling processes of both the world model and the motion model. Furthermore, we designed a motion-aware latent supervision objective that enhances AutoWorld's representation of scene dynamics. Experiments on the WOSAC benchmark show that AutoWorld ranks first on the leaderboard according to the primary Realism Meta Metric (RMM). We further show that simulation performance consistently improves with the inclusion of unlabeled LiDAR data, and study the efficacy of each component with ablations. Our method paves the way for scaling traffic simulation realism without additional labeling. Our project page contains additional visualizations and released code.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
