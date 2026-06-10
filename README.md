# Constitutive birefringence and critical curves in the rotating García-Díaz black hole

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arielguzman-physics/garcia-diaz-birefringence-critical-curves/blob/main/notebooks/GD_birefringence_critical_curves_es.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

This repository contains the reproducible numerical notebook and output files associated with a theoretical study of constitutive birefringence and critical curves in the rotating García-Díaz black hole of Einstein gravity coupled to nonlinear electrodynamics.

The repository is not intended as a general-purpose ray-tracing library. Its purpose is narrower and more precise: to reproduce the critical contours, parameter scans, figures, and geometrical diagnostics used in the accompanying manuscript.

---

## Scientific scope

In nonlinear electrodynamics, high-frequency electromagnetic propagation is governed not only by the spacetime metric, but also by the local constitutive response of the electromagnetic sector. For the rotating García-Díaz branch considered in the manuscript, the Fresnel structure splits into two optical branches. These branches define two effective critical contours on the local screen of a finite-distance observer,

$$
\Gamma_+ ,
\qquad
\Gamma_- .
$$

The notebook follows the numerical part of the chain

$$
\Delta(r),\ A_s(r),\ B_s(\theta)
\longrightarrow
{\xi_s(r_c),k_s(r_c)}
\longrightarrow
\Gamma_s
\longrightarrow
{\Delta_{\rm cel},\Delta_{\rm scr},d_s,w_{\rm br},f_{\rm br}}.
$$

The resulting contours are geometrical critical curves of the effective optical branches. They should not be interpreted as full synthetic images, since emission, plasma propagation, radiative transfer, and instrumental response are not included at this stage.

---

## Physical model

The background is the rotating García-Díaz geometry, parametrized by the mass $(M)$, spin $(a)$, magnetic charge $(p)$, electric charge $(q)$, and nonlinear coupling $(\beta)$. The radial function used in the numerical construction is

$$
\Delta(r)
=========

r^2+a^2-2Mr
+
(p^2+q^2)
\left[
1-\beta(r^2+a^2)
\right]^2 .
$$

At the perturbative optical order used in the manuscript, the two branches are encoded through

$$
A_s(r)=1+\beta\alpha_s r^2,
\qquad
B_s(\theta)=1-\beta\alpha_s a^2\cos^2\theta,
\qquad
s=\pm ,
$$

with

$$
\alpha_+=8,
\qquad
\alpha_-=-4 .
$$

The branch-dependent critical family is obtained from the double-root conditions

$$
\mathcal R_s(r_c;\xi_s,k_s)=0,
\qquad
\partial_r\mathcal R_s(r_c;\xi_s,k_s)=0,
$$

and is then projected onto the local celestial sphere of a finite-distance observer.

---

## Geometrical diagnostics

The notebook reproduces the geometrical diagnostics used to quantify the splitting between $\Gamma_+$ and $\Gamma_-$. The local angular diagnostics are

$$
\Delta_{\rm cel}^{\max},
\qquad
\langle \Delta_{\rm cel}\rangle ,
$$

while the screen-based diagnostics are

$$
\Delta_{\rm scr}^{\max},
\qquad
\delta d_{\rm br},
\qquad
w_{\rm br},
\qquad
f_{\rm br}.
$$

Here $\Delta_{\rm cel}^{\max}$ is intrinsic to the local celestial sphere. The quantities $\delta d_{\rm br}$, $w_{\rm br}$, and $f_{\rm br}$ summarize the global screen-scale imprint of the unresolved birefringent splitting.

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
│       ├── full_observables_all_scans_public.csv
│       ├── full_observables_all_scans_raw.csv
│       ├── table_beta_scan.tex
│       ├── table_spin_scan.tex
│       ├── table_inclination_scan.tex
│       └── tables_all.tex
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Quick start

The notebook can be opened directly in Google Colab using the badge at the top of this page.

For a local run, clone the repository and install the minimal Python environment:

```bash
git clone https://github.com/arielguzman-physics/garcia-diaz-birefringence-critical-curves.git
cd garcia-diaz-birefringence-critical-curves
python -m pip install -r requirements.txt
```

Then open

```text
notebooks/GD_birefringence_critical_curves_es.ipynb
```

and run the notebook from top to bottom.

---

## Numerical outputs

The exported figures are stored in

```text
outputs/figures/
```

and the numerical tables are stored in

```text
outputs/tables/
```

The tables include the scan in the nonlinear coupling, the scan in the spin parameter, and the scan in the observer inclination. The public tables are formatted for direct use in the manuscript, while the raw tables preserve additional numerical information useful for checking the calculation.

---

## Reproducibility notes

The reference runs use geometrized units with (G=c=1). Unless explicitly varied in a scan, the representative parameters are

$$
M=1,\qquad p=0.2,\qquad q=0.3,\qquad r_o=8.
$$

The numerical construction keeps the perturbative optical domain under control through the diagnostic $(\epsilon_{\rm pert})$. The notebook also treats the nonrotating limit separately from the rotating critical parametrization, avoiding the singular use of formulas that contain divisions by $(a)$.

---

## Citation

If this repository contributes to your work, please cite the associated manuscript and the archived software release once the DOI is available.

A machine-readable citation file is provided in

```text
CITATION.cff
```

A Zenodo DOI will be added after the first stable release.

---

## License

This repository is released under the MIT License. See

```text
LICENSE
```

for details.
