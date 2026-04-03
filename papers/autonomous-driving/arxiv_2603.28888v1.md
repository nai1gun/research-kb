---
id: arxiv_2603.28888v1
source: arxiv
topic: autonomous-driving
title: "A Semantic Observer Layer for Autonomous Vehicles: Pre-Deployment Feasibility Study of VLMs for Low-Latency Anomaly Detection"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# A Semantic Observer Layer for Autonomous Vehicles: Pre-Deployment Feasibility Study of VLMs for Low-Latency Anomaly Detection

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Kunal Runwal, Swaraj Gajare, Daniel Adejumo, Omkar Ankalkope, Siddhant Baroth et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28888v1)
- [PDF](https://arxiv.org/pdf/2603.28888v1)

## Abstract

Semantic anomalies-context-dependent hazards that pixel-level detectors cannot reason about-pose a critical safety risk in autonomous driving. We propose a \emph{semantic observer layer}: a quantized vision-language model (VLM) running at 1--2\,Hz alongside the primary AV control loop, monitoring for semantic edge cases, and triggering fail-safe handoffs when detected. Using Nvidia Cosmos-Reason1-7B with NVFP4 quantization and FlashAttention2, we achieve ~500 ms inference a ~50x speedup over the unoptimized FP16 baseline (no quantization, standard PyTorch attention) on the same hardware--satisfying the observer timing budget. We benchmark accuracy, latency, and quantization behavior in static and video conditions, identify NF4 recall collapse (10.6%) as a hard deployment constraint, and a hazard analysis mapping performance metrics to safety goals. The results establish a pre-deployment feasibility case for the semantic observer architecture on embodied-AI AV platforms.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
