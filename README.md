<h1 align="center">Constitutive birefringence and critical curves in the rotating García--Díaz black hole</h1>

<p align="center">
  Numerical notebook, figures, and tables accompanying a theoretical study of
  optical birefringence, critical curves, and geometrical observables in a rotating
  black-hole spacetime sourced by nonlinear electrodynamics.
</p>

---

## Overview

This repository contains the numerical notebook and the output files used to compute the birefringent critical curves and the associated geometrical diagnostics in the rotating García--Díaz black hole.

The underlying physical problem is the splitting of the optical structure into two effective branches, denoted by $\Gamma_+$ and $\Gamma_-$,  induced by the constitutive response of nonlinear electrodynamics. The notebook reproduces the critical curves, the corresponding finite-distance observables, and the tables and figures used in the accompanying manuscript.

Rather than serving as a generic code archive, this repository is intended as a compact and reproducible scientific companion to the theoretical analysis.

---

## Physical setting

We consider the rotating García--Díaz geometry with mass $(M)$, magnetic charge $(p)$, electric charge $(q)$, spin parameter $(a)$, and nonlinear coupling $(\beta)$. The radial structure is governed by

$$ \Delta(r) = r^2+a^2-2Mr + (p^2+q^2)\left[1-\beta(r^2+a^2)\right]^2 . $$

At first order in the constitutive deformation, the two optical branches are encoded through the factors

$$
A_s(r)=1+\beta \alpha_s r^2,
\qquad
B_s(\theta)=1-\beta \alpha_s a^2\cos^2\theta,
\qquad
s=\pm,
$$

with

$$
\alpha_+ = 8,
\qquad
\alpha_- = -4 .
$$

The critical curves are obtained from the double-root conditions on the branch-dependent radial potential,

$$
\mathcal{R}_s(r_c;\xi_s,\kappa_s)=0,
\qquad
\partial_r \mathcal{R}_s(r_c;\xi_s,\kappa_s)=0,
$$

which determine the critical impact parameters and their projection onto the local celestial sky of a finite-distance observer.

---

## Geometrical observables

The repository reproduces the observables used to quantify birefringent splitting between the two critical branches. These include:

$$
\Delta_{\rm cel}^{\max},
\qquad
\langle \Delta_{\rm cel} \rangle,
\qquad
\Delta_{\rm scr}^{\max},
\qquad
\langle \Delta_{\rm scr} \rangle,
$$

together with the effective-diameter and width diagnostics

$$
\delta d_{\rm br},
\qquad
w_{\rm br},
\qquad
f_{\rm br}.
$$

These quantities measure, respectively, the local angular separation on the celestial sphere, the projected separation on the stereographic screen, the relative diameter mismatch between the two branches, and the effective unresolved birefringent width.

---

## Repository structure

```text
garcia-diaz-birefringence-critical-curves/
├── notebooks/
│   └── garcia_diaz_birefringence.ipynb
├── outputs/
│   ├── figures/
│   └── tables/
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
└── .gitignore
