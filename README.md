# PAER-GraphCast: Spectral Dissipation Suppression in AI Weather Forecasting

This repository contains the official implementation of the **Parallel Auto-Encoding Residual (PAER)** module, integrated directly into the **GraphCast** backbone. 

[[DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18360899.svg)](https://doi.org/10.5281/zenodo.18360899)

## Overview
Traditional AI weather models (like standard GraphCast) often suffer from **Spectral Dissipation**—a smoothing effect that erases sharp gradients in frontal zones. **PAER** is a parallel refinement module that:
- Uses the pre-trained GraphCast as the master predictor.
- Re-injects high-frequency energy via a bottleneck autoencoder.
- Preserves the $k^{-3}$ enstrophy cascade law in the dynamic fields.

---

## Reproduction Path 

To reproduce the results presented in the paper (e.g., the 72-hour forecast performance), follow these steps:

### 1. Data Selection
Select the benchmark ERA5 sample data with the following parameters (pre-configured in the notebook):
- **Source**: ERA5 Reanalysis
- **Test Date**: `2022-01-01`
- **Spatial Resolution**: `1.0°`
- **Vertical Levels**: `13` pressure levels
- **Input Sequence**: `40` time steps

### 2. Module Execution
Open the primary notebook `Parallel_Auto_Encoding_Error_Correction_Module.ipynb` The code is structured as an integrated pipeline:
1. **Initialize Master Model**: Loads the pre-trained GraphCast weights.
2. **Apply PAER Layer**: Activates the parallel residual correction.

### 3. Key Parameter for Evaluation
To verify the **72-hour rollout** accuracy mentioned in the manuscript:
- Locate the evaluation cell and ensure: **`eval_steps = 12`** - *Note: Since each step represents 6 hours, 12 steps = 72 hours.*

### 4. Expected Results
Upon completion, the notebook will generate:
- **RMSE/ACC Metrics**: Confirming the drop in 2m Temperature RMSE from ~8.78 to **4.99** (43.16% improvement).
- **Spectral Diagnostics**: Power Spectral Density (PSD) plots showing energy restoration at high wavenumbers.
- **Visualization**: Comparison maps showing the sharpened 10m V-wind gradients.
---
### 5. Acknowledgements & Data Sources

## 1. Model Backbone (GraphCast)
This project utilizes the **GraphCast** model as its primary forecasting backbone. We express our gratitude to the **Google DeepMind** team for open-sourcing the GraphCast framework and providing the pre-trained weights.
- **Official Repository**: [google-deepmind/graphcast](https://github.com/google-deepmind/graphcast)
- **Reference**: Lam, R., et al. (2023). "Learning skillful medium-range global weather forecasting." *Science*.

## 2. Data Source (ERA5)
The training and evaluation of the PAER module are conducted using the **ERA5 reanalysis dataset**. We thank the **European Centre for Medium-Range Weather Forecasts (ECMWF)** and the **Copernicus Climate Change Service (C3S)** for providing this open-access high-quality meteorological data.
- **Data Access**: [Copernicus CDS](https://cds.climate.copernicus.eu/)
- **Reference**: Hersbach, H., et al. (2020). "The ERA5 global reanalysis." *QJRMS*.

## Citation
If you utilize this code or the PAER module, please cite the software archive:

> Wang, Y. (2026). Parallel Auto-Encoding Residual (PAER) Module Implementation (Version 1.0.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.18360899

---
**Contact**: Yuzhi Wang ([wangyzh267@mail2.sysu.edu.cn](mailto:wangyzh267@mail2.sysu.edu.cn))
**Institution**: College of Atmospheric Sciences, Sun Yat-sen University
