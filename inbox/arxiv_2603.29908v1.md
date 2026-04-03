---
id: arxiv_2603.29908v1
source: arxiv
topic: autonomous-driving
title: "C-TRAIL: A Commonsense World Framework for Trajectory Planning in Autonomous Driving"
date: 2026-03-31
discovered: 2026-04-03
status: pending
---

# C-TRAIL: A Commonsense World Framework for Trajectory Planning in Autonomous Driving

**Source:** arxiv
**Date:** 2026-03-31
**Authors:** Zhihong Cui, Haoran Tang, Tianyi Li, Yushuai Li, Peiyuan Guan et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.29908v1)
- [PDF](https://arxiv.org/pdf/2603.29908v1)

## Abstract

Trajectory planning for autonomous driving increasingly leverages large language models (LLMs) for commonsense reasoning, yet LLM outputs are inherently unreliable, posing risks in safety-critical applications. We propose C-TRAIL, a framework built on a Commonsense World that couples LLM-derived commonsense with a trust mechanism to guide trajectory planning. C-TRAIL operates through a closed-loop Recall, Plan, and Update cycle: the Recall module queries an LLM for semantic relations and quantifies their reliability via a dual-trust mechanism; the Plan module injects trust-weighted commonsense into Monte Carlo Tree Search (MCTS) through a Dirichlet trust policy; and the Update module adaptively refines trust scores and policy parameters from environmental feedback. Experiments on four simulated scenarios in Highway-env and two real-world levelXData datasets (highD, rounD) show that C-TRAIL consistently outperforms state-of-the-art baselines, reducing ADE by 40.2%, FDE by 51.7%, and improving SR by 16.9 percentage points on average. The source code is available at https://github.com/ZhihongCui/CTRAIL.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
