# PAER: Parallel Auto-Encoding Residual Module for Spectral Dissipation Suppression

This repository contains the official implementation of the **Parallel Auto-Encoding Residual (PAER)** module. PAER is a "non-invasive" refinement strategy designed to recover high-frequency spatial gradients and restore the energy spectrum in AI-driven weather forecasting models (e.g., GraphCast).

[[DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18360899.svg)](https://doi.org/10.5281/zenodo.18360899)

## Key Features
- **Spectral Recovery**: Specifically addresses the "oversmoothing" (Spectral Dissipation) caused by MSE loss.
- **Dynamic Awareness**: Utilizes temporal differences as momentum proxies to capture advancing frontal zones.
- **Plug-and-Play**: Compatible with pre-trained backbones (GraphCast/Pangu-Weather) without altering the master weights.

---

## Reproduction Guide (Reproduce Paper Results)

To reproduce the results presented in the manuscript, follow the configuration below in the provided Jupyter Notebook (`Parallel_Auto_Encoding_Error_Correction_Module.ipynb`).

### 1. Data Configuration
The module is validated using the ERA5 reanalysis dataset. Ensure your data loader is configured as follows:
- **Source**: ERA5 (via Copernicus CDS)
- **Reference Date**: `2022-01-01`
- **Spatial Resolution**: `1.0°` (Global grid)
- **Vertical Levels**: `13` (Standard pressure levels)
- **Time Steps**: `40` (For training/diagnostic sequences)

### 2. Evaluation & Rollout Settings
To verify the **72-hour forecast performance** (the primary benchmark in the paper):
- **Evaluation Steps**: Set `eval_steps = 12`
- **Temporal Resolution**: 6 hours per step ($6 \times 12 = 72$ hours total).

### 3. Running the Code
1. **Environment**: Install dependencies (JAX, Haiku, Cartopy, Xarray).
2. **Initialization**: Load the pre-trained master model weights.
3. **Execution**: Run the PAER refinement cells. The script will automatically generate:
   - RMSE and ACC metrics for 2m Temperature and 10m V-Wind.
   - Spatial gradient maps comparing "Master Model" vs "PAER Refined" vs "ERA5 Truth".
   - Power Spectral Density (PSD) analysis plots.

---

## Expected Performance
By implementing PAER with the above settings, you should observe:
- **RMSE Reduction**: ~43.16% improvement in 2m Temperature at the 72h mark.
- **Gradient Recovery**: Local gradient spans in 10m V-wind recovered by up to 32.74 m/s.
- **Physical Fidelity**: The energy spectrum will align more closely with the $k^{-3}$ enstrophy cascade law.



---

##  Repository Structure
- `Parallel_Auto_Encoding_Error_Correction_Module.ipynb`: Main implementation and reproduction notebook.
- `results/`: Contains generated diagnostic maps and PDF reports.
- `metadata_fix.py`: Utility script to ensure Colab compatibility.

## Citation
If you use this code or the PAER module in your research, please cite:

**Software Citation:**
> Wang, Y. (2026). Parallel Auto-Encoding Residual (PAER) Module Implementation (Version 1.0.0). Zenodo. https://doi.org/10.5281/zenodo.18360899

**Paper Citation:**
> Wang, Y. (2026). Dissipation Suppression of the Atmospheric Dynamical Field Spectrum Based on Parallel Auto-Encoding Error Correction. *Journal of Advances in Modeling Earth Systems (JAMES)*. (Manuscript submitted).

---
**Contact**: Yuzhi Wang ([wangyzh267@mail2.sysu.edu.cn](mailto:wangyzh267@mail2.sysu.edu.cn))
