"""Generate clearly labelled model-only charts from local illustrative outputs."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
def load(file):
    with (ROOT/'outputs'/file).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))
def export(fig,name):
    fig.text(.01,.012,'SCENARIO DATA ONLY  |  No observed project outcome or validated compliance',size=8)
    fig.tight_layout(rect=(0,.025,1,1))
    dest=ROOT/'figures'/name
    fig.savefig(dest,format='svg',metadata={'Title':name,'Date':'2026-10-04'})
    plt.close(fig)
    print('Wrote reproducible figure',dest)
def main():
    rows=load('ILLUSTRATIVE_grid_sensitivity.csv')
    groups=sorted(set(float(r['project_factor']) for r in rows))
    fig,ax=plt.subplots(figsize=(10.5,5.5))
    for p in groups:
        z=[r for r in rows if float(r['project_factor'])==p]
        ax.plot([float(r['leakage_factor']) for r in z],[float(r['technical_difference_over_horizon_tco2e']) for r in z],marker='o',label=f'Project proxy {p:g}')
    ax.set(xlabel='Leakage proxy (tCO2e / ha / yr)',ylabel='Technical arithmetic (tCO2e)',title='ILLUSTRATIVE | Emission-factor sensitivity, NOT credits')
    ax.legend(title='Project factor');export(fig,'ILLUSTRATIVE_carbon_uncertainty.svg')

if __name__ == "__main__":main()
