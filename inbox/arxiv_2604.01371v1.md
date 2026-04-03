---
id: arxiv_2604.01371v1
source: arxiv
topic: autonomous-driving
title: "AffordTissue: Dense Affordance Prediction for Tool-Action Specific Tissue Interaction"
date: 2026-04-01
discovered: 2026-04-03
status: pending
---

# AffordTissue: Dense Affordance Prediction for Tool-Action Specific Tissue Interaction

**Source:** arxiv
**Date:** 2026-04-01
**Authors:** Aiza Maksutova, Lalithkumar Seenivasan, Hao Ding, Jiru Xu, Chenhao Yu et al.
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2604.01371v1)
- [PDF](https://arxiv.org/pdf/2604.01371v1)

## Abstract

Surgical action automation has progressed rapidly toward achieving surgeon-like dexterous control, driven primarily by advances in learning from demonstration and vision-language-action models. While these have demonstrated success in table-top experiments, translating them to clinical deployment remains challenging: current methods offer limited predictability on where instruments will interact on tissue surfaces and lack explicit conditioning inputs to enforce tool-action-specific safe interaction regions. Addressing this gap, we introduce AffordTissue, a multimodal framework for predicting tool-action specific tissue affordance regions as dense heatmaps during cholecystectomy. Our approach combines a temporal vision encoder capturing tool motion and tissue dynamics across multiple viewpoints, language conditioning enabling generalization across diverse instrument-action pairs, and a DiT-style decoder for dense affordance prediction. We establish the first tissue affordance benchmark by curating and annotating 15,638 video clips across 103 cholecystectomy procedures, covering six unique tool-action pairs involving four instruments (hook, grasper, scissors, clipper) and their associated tasks: dissection, grasping, clipping, and cutting. Experiments demonstrate substantial improvement over vision-language model baselines (20.6 px ASSD vs. 60.2 px for Molmo-VLM), showing that our task-specific architecture outperforms large-scale foundation models for dense surgical affordance prediction. By predicting tool-action specific tissue affordance regions, AffordTissue provides explicit spatial reasoning for safe surgical automation, potentially unlocking explicit policy guidance toward appropriate tissue regions and early safe stop when instruments deviate outside predicted safe zones.

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
