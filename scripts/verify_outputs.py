"""Check consistency of the exported optical observables and figures."""

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
FIGURES = ROOT / "outputs" / "figures"

all_rows = pd.read_csv(TABLES / "full_observables_all_scans_public.csv")
assert len(all_rows) == 17, "Expected 17 parameter configurations"
assert set(all_rows.scan_key) == {"beta", "spin", "inclination", "charge"}
assert all_rows.groupby("scan_key").size().to_dict() == {
    "beta": 5, "charge": 4, "inclination": 4, "spin": 4
}

for key in ("beta", "spin", "inclination", "charge"):
    one = pd.read_csv(TABLES / f"{key}_scan_observables.csv")
    assert len(one) == len(all_rows[all_rows.scan_key == key])
    assert (TABLES / f"table_{key}_scan.tex").is_file()
    for col in ("Delta_cel_max", "Delta_scr_max", "d0", "delta_d_br", "w_br", "f_br", "epsilon_pert"):
        assert np.allclose(one[col], all_rows.loc[all_rows.scan_key == key, col],
                           rtol=1e-10, atol=2e-12), (key, col)

charge = pd.read_csv(TABLES / "charge_scan_observables.csv")
assert "min_rpp" in charge, "Missing radial-curvature minimum from charge CSV"
assert charge.min_rpp.notna().all(), "Blank radial-curvature minimum"
assert np.isfinite(charge.min_rpp).all() and (charge.min_rpp > 0).all()
assert np.allclose(charge.min_rpp, [10.9142, 7.9802, 7.9802, 3.1533],
                   rtol=0, atol=0.001), "Unexpected radial instability minima"
tex = (TABLES / "table_charge_scan.tex").read_text(encoding="utf-8")
for _, r in charge.iterrows():
    row_tex = (f"{r.p:.2f} & {r.q:.2f} & {r.Qc:.5f} & "
               f"{r.r_plus:.5f} & {r.Delta_cel_max:.5f} & "
               f"{r.delta_d_br:.5f} & {r.f_br:.5f} & "
               f"{r.epsilon_pert:.5f} & {r.min_rpp:.4f}")
    assert row_tex in tex, f"LaTeX/CSV mismatch: ({r.p}, {r.q})"

swapped = charge.loc[np.isclose(charge.Qc, np.hypot(.15, .25))]
assert len(swapped) == 2
for col in ("r_plus", "Delta_cel_max", "Delta_scr_max", "d0",
            "delta_d_br", "w_br", "f_br", "epsilon_pert", "min_rpp"):
    assert np.allclose(swapped[col], swapped[col].iloc[0],
                       rtol=2e-9, atol=2e-11), col

maxwell = all_rows.loc[(all_rows.scan_key == "beta") & np.isclose(all_rows.beta, 0)]
assert len(maxwell) == 1
for col in ("Delta_cel_max", "Delta_scr_max", "delta_d_br", "w_br", "f_br"):
    assert abs(maxwell.iloc[0][col]) < 1e-11, col
assert (all_rows.epsilon_pert < 0.05).all()

reference = charge.loc[np.isclose(charge.p, .2) & np.isclose(charge.q, .3)]
assert len(reference) == 1
assert abs(reference.iloc[0].Delta_cel_max - 0.1490774011757623) < 5e-7
assert abs(reference.iloc[0].d0 - 1.1267559983334985) < 5e-6
for stem in ("figure_beta_contours_soft_filled", "figure_spin_contours_soft_filled"):
    for ext in ("png", "pdf"):
        f = FIGURES / f"{stem}.{ext}"
        assert f.is_file() and f.stat().st_size > 25_000, f

print("All 17 scans, four radial minima, table exports and figures: OK.")
