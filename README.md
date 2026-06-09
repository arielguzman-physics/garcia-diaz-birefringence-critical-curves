````markdown
# Birefringent critical curves in the rotating García–Díaz black hole

This repository contains the computational material accompanying the manuscript

**Constitutive birefringence and critical curves in the rotating García–Díaz black hole**.

The notebook implements the numerical construction of the two effective optical branches associated with nonlinear electrodynamics and follows their projection onto the local sky of a finite-distance observer. In this setting, the birefringent splitting of the optical cones is translated into two critical contours, denoted by Γ₊ and Γ₋, together with a set of geometrical diagnostics that quantify their angular and screen-level separation.

## Scope

The repository is intended as a reproducibility companion to the paper. It contains the routines used to generate the critical curves, the numerical tables, and the publication figures discussed in the manuscript.

The computation includes:

- construction of the García–Díaz background functions;
- branch-dependent optical factors;
- critical constants for the rotating case;
- spherical-limit treatment for `a = 0`;
- finite-distance projection onto the observer screen;
- geometrical observables for the birefringent splitting;
- CSV and LaTeX table generation;
- PDF and PNG figure export.

## Repository structure

```text
notebooks/
  GD_birefringence_critical_curves_es.ipynb

outputs/
  figures/
    figure_beta_contours_soft_filled.pdf
    figure_beta_contours_soft_filled.png
    figure_spin_contours_soft_filled.pdf
    figure_spin_contours_soft_filled.png

  tables/
    full_observables_all_scans_raw.csv
    full_observables_all_scans_public.csv
    beta_scan_observables.csv
    spin_scan_observables.csv
    inclination_scan_observables.csv
    table_beta_scan.tex
    table_spin_scan.tex
    table_inclination_scan.tex
    tables_all.tex
````

## Physical configuration

Unless otherwise stated, the numerical runs use

```text
M = 1
p = 0.2
q = 0.3
r_o = 8
```

The reported scans vary the nonlinear coupling, the rotation parameter, and the observer inclination:

```text
10^4 beta M^2
a/M
theta_o
```

The notebook keeps the raw floating-point outputs and separately produces publication-level tables where only exact-limit numerical residues are cleaned. In particular, the Maxwell limit is treated as a consistency check: when `beta = 0`, the two optical branches collapse and the birefringent observables vanish.

## Main outputs

The generated observables include:

* maximum angular separation on the local celestial sphere;
* mean angular separation along the critical contour;
* maximum and mean screen separation;
* effective diameters of Γ₊ and Γ₋;
* fractional birefringent diameter shift;
* effective birefringent width;
* perturbative-control diagnostics.

## Reproducing the results

The notebook was prepared in Python and can be executed in Google Colab or in a local Jupyter environment.

To install the minimal local dependencies, use

```bash
pip install -r requirements.txt
```

Then open

```text
notebooks/GD_birefringence_critical_curves_es.ipynb
```

and run all cells from top to bottom. The figures and tables are written to the `outputs/` directory.

## Citation

If you use this repository, please cite the associated paper and the archived Zenodo release of this repository once available.

## License

This repository is distributed under the MIT License.

```
```
