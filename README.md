# Birefringent critical curves in the rotating García--Díaz black hole

This repository contains the numerical notebook and output files used to generate
the critical curves, geometrical diagnostics, tables, and figures reported in the manuscript:

**Constitutive birefringence and critical curves in the rotating García--Díaz black hole**

## Contents

- `notebooks/`: Jupyter notebook used to compute the birefringent critical curves and geometrical observables.
- `outputs/figures/`: PDF and PNG versions of the generated figures.
- `outputs/tables/`: CSV data files and LaTeX tables used in the manuscript.

## Reproducibility

The notebook is written in Python and uses NumPy, pandas, SciPy, and Matplotlib.
Running the notebook regenerates the numerical tables and figures reported in the paper.

## Physical setup

Unless otherwise stated, the numerical runs use

\[
M=1,\qquad p=0.2,\qquad q=0.3,\qquad r_o=8.
\]

The scans vary \(10^4\beta M^2\), \(a/M\), and the observer inclination \(\theta_o\).

## Output files

The notebook generates:

- critical-curve figures in PDF and PNG format;
- raw CSV files preserving floating-point output;
- publication-level CSV files with display-level zero cleanup;
- LaTeX tables compatible with REVTeX/PRD.

## Citation

If you use this repository, please cite the associated paper and the archived Zenodo version of this repository.
