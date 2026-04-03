---
id: arxiv_2603.29941v1
source: arxiv
topic: autonomous-driving
title: "Better than Average: Spatially-Aware Aggregation of Segmentation Uncertainty Improves Downstream Performance"
date: 2026-03-31
discovered: 2026-04-03
status: pending
---

# Better than Average: Spatially-Aware Aggregation of Segmentation Uncertainty Improves Downstream Performance

**Source:** arxiv
**Date:** 2026-03-31
**Authors:** Vanessa Emanuela Guarino, Claudia Winklmayr, Jannik Franzen, Josef Lorenz Rumberger, Manuel Pfeuffer et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.29941v1)
- [PDF](https://arxiv.org/pdf/2603.29941v1)

## Abstract

Uncertainty Quantification (UQ) is crucial for ensuring the reliability of automated image segmentations in safety-critical domains like biomedical image analysis or autonomous driving. In segmentation, UQ generates pixel-wise uncertainty scores that must be aggregated into image-level scores for downstream tasks like Out-of-Distribution (OoD) or failure detection. Despite routine use of aggregation strategies, their properties and impact on downstream task performance have not yet been comprehensively studied. Global Average is the default choice, yet it does not account for spatial and structural features of segmentation uncertainty. Alternatives like patch-, class- and threshold-based strategies exist, but lack systematic comparison, leading to inconsistent reporting and unclear best practices. We address this gap by (1) formally analyzing properties, limitations, and pitfalls of common strategies; (2) proposing novel strategies that incorporate spatial uncertainty structure and (3) benchmarking their performance on OoD and failure detection across ten datasets that vary in image geometry and structure. We find that aggregators leveraging spatial structure yield stronger performance in both downstream tasks studied. However, the performance of individual aggregators depends heavily on dataset characteristics, so we (4) propose a meta-aggregator that integrates multiple aggregators and performs robustly across datasets.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
