---
id: arxiv_2604.01259v1
source: arxiv
topic: autonomous-driving
title: "Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models"
date: 2026-04-01
discovered: 2026-04-03
status: pending
---

# Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models

**Source:** arxiv
**Date:** 2026-04-01
**Authors:** Xiaosong Jia, Yuqian Shao, Zhenjie Yang, Qifeng Li, Zhiyuan Zhang et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01259v1)
- [PDF](https://arxiv.org/pdf/2604.01259v1)

## Abstract

With the rise of vision-language models (VLM), their application for autonomous driving (VLM4AD) has gained significant attention. Meanwhile, in autonomous driving, closed-loop evaluation has become widely recognized as a more reliable validation method than open-loop evaluation, as it can evaluate the performance of the model under cumulative errors and out-of-distribution inputs. However, existing VLM4AD benchmarks evaluate the model`s scene understanding ability under open-loop, i.e., via static question-answer (QA) dataset. This kind of evaluation fails to assess the VLMs performance under out-of-distribution states rarely appeared in the human collected datasets.To this end, we present Bench2Drive-VL, an extension of Bench2Drive that brings closed-loop evaluation to VLM-based driving, which introduces: (1) DriveCommenter, a closed-loop generator that automatically generates diverse, behavior-grounded question-answer pairs for all driving situations in CARLA,including severe off-route and off-road deviations previously unassessable in simulation. (2) A unified protocol and interface that allows modern VLMs to be directly plugged into the Bench2Drive closed-loop environment to compare with traditional agents. (3) A flexible reasoning and control framework, supporting multi-format visual inputs and configurable graph-based chain-of-thought execution. (4) A complete development ecosystem. Together, these components form a comprehensive closed-loop benchmark for VLM4AD. All codes and annotated datasets are open sourced.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
