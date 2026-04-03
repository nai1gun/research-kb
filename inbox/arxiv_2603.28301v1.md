---
id: arxiv_2603.28301v1
source: arxiv
topic: autonomous-driving
title: "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, Dahuin Jung
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28301v1)
- [PDF](https://arxiv.org/pdf/2603.28301v1)

## Abstract

Vision-Language-Action (VLA) models achieve strong performance in robotic manipulation by leveraging pre-trained vision-language backbones. However, in downstream robotic settings, they are typically fine-tuned with limited data, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored. To study this gap, we introduce LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization. Across seven VLA configurations (0.6B-7.5B), we observe consistent performance degradation of 22-52 pp under paraphrasing. This degradation is primarily driven by object-level lexical variation: even simple synonym substitutions cause large drops, indicating reliance on surface-level matching rather than semantic grounding. Moreover, 80-96% of failures arise from planning-level trajectory divergence rather than execution errors, showing that paraphrasing disrupts task identification. Binary success rate treats all paraphrases equally, obscuring whether models perform consistently across difficulty levels or rely on easier cases. To address this, we propose PRIDE, a metric that quantifies paraphrase difficulty using semantic and syntactic factors. Our benchmark and corresponding code are available at: https://github.com/cau-hai-lab/LIBERO-Para

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
