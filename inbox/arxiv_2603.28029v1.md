---
id: arxiv_2603.28029v1
source: arxiv
topic: autonomous-driving
title: "Effort-Based Criticality Metrics for Evaluating 3D Perception Errors in Autonomous Driving"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# Effort-Based Criticality Metrics for Evaluating 3D Perception Errors in Autonomous Driving

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Sharang Kaul, Simon Bultmann, Mario Berk, Abhinav Valada
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28029v1)
- [PDF](https://arxiv.org/pdf/2603.28029v1)

## Abstract

Criticality metrics such as time-to-collision (TTC) quantify collision urgency but conflate the consequences of false-positive (FP) and false-negative (FN) perception errors. We propose two novel effort-based metrics: False Speed Reduction (FSR), the cumulative velocity loss from persistent phantom detections, and Maximum Deceleration Rate (MDR), the peak braking demand from missed objects under a constant-acceleration model. These longitudinal metrics are complemented by Lateral Evasion Acceleration (LEA), adapted from prior lateral evasion kinematics and coupled with reachability-based collision timing to quantify the minimum steering effort to avoid a predicted collision. A reachability-based ellipsoidal collision filter ensures only dynamically plausible threats are scored, with frame-level matching and track-level aggregation. Evaluation of different perception pipelines on nuScenes and Argoverse~2 shows that 65-93% of errors are non-critical, and Spearman correlation analysis confirms that all three metrics capture safety-relevant information inaccessible to established time-based, deceleration-based, or normalized criticality measures, enabling targeted mining of the most critical perception failures.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
