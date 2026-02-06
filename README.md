# PAER-GraphCast: Spectral Dissipation Suppression in AI Weather Forecasting

This repository contains the official implementation of the **Parallel Auto-Encoding Residual (PAER)** module, integrated directly into the **GraphCast** backbone.

[[DOI](https://doi.org/10.5281/zenodo.18360899)]

## Overview

Traditional AI weather models (like standard GraphCast) often suffer from **Spectral Dissipation**—a smoothing effect that erases sharp gradients in frontal zones. **PAER** is a parallel refinement module that:

* Uses the pre-trained GraphCast as the master predictor.
* Re-injects high-frequency energy via a bottleneck autoencoder.
* Preserves the  enstrophy cascade law in the dynamic fields.

---

## Version 2.0 Updates: Physics-Augmented Spectral Matching

Building upon the version 1.0 residual framework, PAER v2.0 introduces **Physics-Augmented Energy Refinement**. This version moves beyond simple error correction by implementing a dual-objective training strategy that explicitly aligns the model with atmospheric kinetic energy spectra.

### New Features in v2.0

* **Spectral Matching Loss**: Integration of a Log-Power Spectral Density (PSD) penalty to suppress non-physical noise and ensure alignment with the Kolmogorov  and enstrophy  laws.
* **Adaptive Gradient Mapping**: Enhanced capability to maintain peak gradients comparable to ERA5 ground truth.
* **Universal Variable Support**: Refined architectural bottleneck that supports joint optimization of both surface variables and multi-level volumetric fields.

---

## Reproduction Path

### 1. Data Selection

Select the benchmark ERA5 sample data with the following parameters:

* **Source**: ERA5 Reanalysis
* **Test Date**: 2022-01-01
* **Spatial Resolution**: 1.0 degree
* **Vertical Levels**: 13 pressure levels
* **Input Sequence**: 40 time steps

### 2. Module Execution

Open the primary notebook `Parallel_Auto_Encoding_Error_Correction_Module.ipynb`. The pipeline is structured as follows:

1. **Initialize Master Model**: Loads the pre-trained GraphCast weights.
2. **Apply PAER Layer**: Activates the parallel residual correction.
3. **Spectral Training (v2.0)**: Executes 20 iterations of fine-tuning with the combined MSE and Spectral Loss.

### 3. Key Parameter for Evaluation

To verify the **72-hour rollout** accuracy mentioned in the manuscript:

* Locate the evaluation cell and ensure: **eval_steps = 12** (Note: 12 steps * 6 hours/step = 72 hours).

### 4. Expected Results

The following benchmarks represent the performance evolution from v1.0 to v2.0:

#### Version 1.0 (Engineering Correction)

* **RMSE (2m Temp)**: Reduction from 8.78 to 4.99 (43.16% improvement).
* **Visuals**: Sharpened frontal zones but potential for high-frequency noise.

#### Version 2.0 (Physics-Augmented)

* **RMSE (72h Lead)**: Reduction from 13.74 to **6.53** (52.46% improvement).
* **ACC (72h Lead)**: Improvement from 0.804 to **0.919**.
* **Spectral Alignment**: Near-perfect matching of the energy spectrum across all wavenumbers.

---

## Acknowledgements & Data Sources

### 1. Model Backbone (GraphCast)

This project utilizes the **GraphCast** model as its primary forecasting backbone. We express our gratitude to the **Google DeepMind** team for open-sourcing the GraphCast framework and providing the pre-trained weights.

* **Official Repository**: google-deepmind/graphcast
* **Reference**: Lam, R., et al. (2023). "Learning skillful medium-range global weather forecasting." Science.

### 2. Data Source (ERA5)

The training and evaluation of the PAER module are conducted using the **ERA5 reanalysis dataset**. We thank the **European Centre for Medium-Range Weather Forecasts (ECMWF)** and the **Copernicus Climate Change Service (C3S)** for providing this open-access high-quality meteorological data.

* **Data Access**: Copernicus CDS
* **Reference**: Hersbach, H., et al. (2020). "The ERA5 global reanalysis." QJRMS.

## Citation

If you utilize this code or the PAER module, please cite the software archive:

> Wang, Y. (2026). Parallel Auto-Encoding Residual (PAER) Module Implementation (Version 2.0.0) [Software]. Zenodo. [https://doi.org/10.5281/zenodo.18360899](https://doi.org/10.5281/zenodo.18360899)

---

**Contact**: Yuzhi Wang (wangyzh267@mail2.sysu.edu.cn)
**Institution**: College of Atmospheric Sciences, Sun Yat-sen University
