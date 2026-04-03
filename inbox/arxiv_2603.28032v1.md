---
id: arxiv_2603.28032v1
source: arxiv
topic: autonomous-driving
title: "CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence"
date: 2026-03-30
discovered: 2026-04-03
status: pending
---

# CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence

**Source:** arxiv
**Date:** 2026-03-30
**Authors:** Tianle Zeng, Hanxuan Chen, Yanci Wen, Hong Zhang
**Topic:** autonomous-driving

## Links

- [Original](https://arxiv.org/abs/2603.28032v1)
- [PDF](https://arxiv.org/pdf/2603.28032v1)

## Abstract

The convergence of low-altitude economies, embodied intelligence, and air-ground cooperative systems creates growing demand for simulation infrastructure capable of jointly modeling aerial and ground agents within a single physically coherent environment. Existing open-source platforms remain domain-segregated: driving simulators lack aerial dynamics, while multirotor simulators lack realistic ground scenes. Bridge-based co-simulation introduces synchronization overhead and cannot guarantee strict spatial-temporal consistency.   We present CARLA-Air, an open-source infrastructure that unifies high-fidelity urban driving and physics-accurate multirotor flight within a single Unreal Engine process. The platform preserves both CARLA and AirSim native Python APIs and ROS 2 interfaces, enabling zero-modification code reuse. Within a shared physics tick and rendering pipeline, CARLA-Air delivers photorealistic environments with rule-compliant traffic, socially-aware pedestrians, and aerodynamically consistent UAV dynamics, synchronously capturing up to 18 sensor modalities across all platforms at each tick. The platform supports representative air-ground embodied intelligence workloads spanning cooperation, embodied navigation and vision-language action, multi-modal perception and dataset construction, and reinforcement-learning-based policy training. An extensible asset pipeline allows integration of custom robot platforms into the shared world. By inheriting AirSim's aerial capabilities -- whose upstream development has been archived -- CARLA-Air ensures this widely adopted flight stack continues to evolve within a modern infrastructure.   Released with prebuilt binaries and full source: https://github.com/louiszengCN/CarlaAir

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
