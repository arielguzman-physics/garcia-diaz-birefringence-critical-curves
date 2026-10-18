# Constitutive birefringence and critical curves in the rotating García-Díaz black hole

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arielguzman-physics/garcia-diaz-birefringence-critical-curves/blob/main/notebooks/GD_birefringence_critical_curves_es.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

This repository contains the reproducible numerical notebook and output files associated with a theoretical study of constitutive birefringence and critical curves in the rotating García-Díaz black hole of Einstein gravity coupled to nonlinear electrodynamics.

The repository is not intended as a general-purpose ray-tracing library. Its purpose is to reproduce the critical contours, parameter scans, figures, and geometrical diagnostics used in the accompanying manuscript.

---

## Scientific scope

In nonlinear electrodynamics, high-frequency electromagnetic propagation depends on both the spacetime metric and the local constitutive response. For the rotating García-Díaz branch considered in the manuscript, the first-order Fresnel analysis yields two effective optical branches whose critical contours are denoted by

$$
\Gamma_+ , \qquad \Gamma_- .
$$

The numerical construction follows the sequence

$$
\Delta(r),\ A_s(r),\ B_s(\theta)
\longrightarrow \{\xi_s(r_c),k_s(r_c)\}
\longrightarrow \Gamma_s
\longrightarrow \{\Delta_{\rm cel},\Delta_{\rm scr},d_s,w_{\rm br},f_{\rm br}\}.
$$

These contours describe the critical geometry seen by a finite-distance observer. They are not synthetic emission images: plasma propagation, radiative transfer, and instrumental response are outside the scope of this calculation.

---

## Physical model

The rotating García-Díaz background is characterized by the mass $M$, spin $a$, magnetic charge $p$, electric charge $q$, and nonlinear coupling $\beta$. The radial function is

$$
\Delta(r)=r^2+a^2-2Mr+(p^2+q^2)\left[1-\beta(r^2+a^2)\right]^2.
$$

To first order in the optical constitutive deformation, the branch-dependent separated factors are

$$
A_s(r)=1+\beta\alpha_s r^2,
\qquad
B_s(\theta)=1-\beta\alpha_s a^2\cos^2\theta,
\qquad s=\pm,
$$

with

$$
\alpha_+=8,\qquad\alpha_-=-4.
$$

The critical families follow from the radial double-root conditions

$$
\mathcal R_s(r_c;\xi_s,k_s)=0,
\qquad
\partial_r\mathcal R_s(r_c;\xi_s,k_s)=0,
$$

and are projected onto the celestial sphere of a finite-distance observer. The background geometry is kept in its exact form; the optical constitutive corrections are evaluated at the perturbative order established in the manuscript.

---

## Geometrical diagnostics

The splitting between $\Gamma_+$ and $\Gamma_-$ is quantified by the maximum celestial and stereographic-screen separations,

$$
\Delta_{\rm cel}^{\max},\qquad\Delta_{\rm scr}^{\max},
$$

together with the effective-diameter and width diagnostics,

$$
\delta d_{\rm br},\qquad w_{\rm br},\qquad f_{\rm br}.
$$

The celestial separation measures the difference between local sky directions, whereas the screen observables characterize the projected contour geometry. The charge scan also records the minimum radial curvature $\min\mathcal R_s''$ of the visible critical families as a numerical check of radial instability.

---

## Repository structure

```text
garcia-diaz-birefringence-critical-curves/
├── notebooks/
│   └── GD_birefringence_critical_curves_es.ipynb
├── outputs/
│   ├── figures/
│   │   ├── figure_beta_contours_soft_filled.pdf
│   │   ├── figure_beta_contours_soft_filled.png
│   │   ├── figure_spin_contours_soft_filled.pdf
│   │   └── figure_spin_contours_soft_filled.png
│   └── tables/
│       ├── beta_scan_observables.csv
│       ├── spin_scan_observables.csv
│       ├── inclination_scan_observables.csv
│       ├── charge_scan_observables.csv
│       ├── full_observables_all_scans_public.csv
│       ├── full_observables_all_scans_raw.csv
│       ├── table_beta_scan.tex
│       ├── table_spin_scan.tex
│       ├── table_inclination_scan.tex
│       ├── table_charge_scan.tex
│       └── tables_all.tex
├── scripts/
│   ├── reproduce.py
│   └── verify_outputs.py
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Quick start

The notebook can be opened directly in Google Colab using the badge at the top of this page.

For a local run, clone the repository and install the Python dependencies:

```bash
git clone https://github.com/arielguzman-physics/garcia-diaz-birefringence-critical-curves.git
cd garcia-diaz-birefringence-critical-curves
python -m pip install -r requirements.txt
```

Open `notebooks/GD_birefringence_critical_curves_es.ipynb` and run the notebook from top to bottom. Alternatively, execute the notebook and regenerate its outputs from the repository root:

```bash
python scripts/reproduce.py
python scripts/verify_outputs.py
```

The verification script checks the numerical tables, the radial-instability minima, the Maxwell limit, the charge-interchange consistency, and the presence of the exported figures.

---

## Numerical outputs

The figure files are stored in `outputs/figures/`, and the numerical results in `outputs/tables/`. Four parameter scans are provided: nonlinear coupling, spin, observer inclination, and electric–magnetic charge configurations.

The charge scan includes four representative pairs $(p,q)$ at fixed $a/M=0.93$, $\beta M^2=10^{-4}$, $r_o=8M$, and $\theta_o=85^\circ$. In the two configurations with equal $Q_c=\sqrt{p^2+q^2}$ obtained by exchanging $p$ and $q$, the computed critical-contour diagnostics agree at the retained optical order. This does not establish charge-composition independence beyond that order or for arbitrary constitutive branches.

The CSV exports preserve the numerical values used to generate the corresponding LaTeX tables. `full_observables_all_scans_public.csv` collects all 17 parameter configurations; the individual scan files provide the results by parameter family.

---

## Reproducibility notes

Calculations use geometrized units $G=c=1$. Unless varied by a particular scan, the reference configuration is

$$
M=1,\qquad p=0.2,\qquad q=0.3,\qquad r_o=8.
$$

The perturbative indicator $\epsilon_{\rm pert}$ is reported to monitor the retained first-order optical corrections. It is not, by itself, a certified bound on the complete higher-order remainder. The nonrotating case is evaluated separately rather than by substituting $a=0$ into expressions containing $1/a$.

---

## Citation

If this repository contributes to your work, please cite the accompanying manuscript and the archived software release once a DOI becomes available. Machine-readable citation metadata are provided in `CITATION.cff`. A Zenodo DOI may be added after the first stable release.

---

## License

This repository is released under the MIT License; see [LICENSE](LICENSE).
