"""Check numerical invariances and representative values in the exported data."""
from pathlib import Path
import numpy as np
import pandas as pd
root=Path(__file__).resolve().parents[1]
tab=root/'outputs'/'tables'
f=pd.read_csv(tab/'full_observables_all_scans_public.csv')
assert len(f)==17, f'Expected 17 scan rows, got {len(f)}'
r=f[(f.scan_key=='charge') & np.isclose(f.p,.2) & np.isclose(f.q,.3)].iloc[0]
assert abs(r.Delta_cel_max-0.1490774011757623)<5e-7
assert abs(r.d0-1.1267559983334985)<5e-6
sw=f[(f.scan_key=='charge') & np.isclose(f.Qc, np.hypot(.15,.25))]
assert len(sw)==2
for col in ['r_plus','Delta_cel_max','Delta_scr_max','d0','delta_d_br','w_br','f_br','epsilon_pert']:
    assert np.allclose(sw[col].to_numpy(),sw[col].iloc[0],rtol=2e-9,atol=2e-11),col
m=f[(f.scan_key=='beta')&np.isclose(f.beta,0)].iloc[0]
for col in ['Delta_cel_max','Delta_scr_max','delta_d_br','w_br','f_br']:
    assert abs(m[col])<1e-11,col
assert (f.epsilon_pert<.05).all()
for stem in ['figure_beta_contours_soft_filled','figure_spin_contours_soft_filled']:
    for ext in ['png','pdf']:
        p=root/'outputs'/'figures'/f'{stem}.{ext}'
        assert p.exists() and p.stat().st_size>25_000,p
for stem in ['beta','spin','inclination','charge']:
    assert (tab/f'{stem}_scan_observables.csv').exists()
    assert (tab/f'table_{stem}_scan.tex').exists()
print('Numerical tables, figures and consistency checks: OK.')
