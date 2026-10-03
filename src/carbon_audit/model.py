"""Planning scenario arithmetic only: never quantifies registrable credits."""
from __future__ import annotations
from dataclasses import dataclass,replace
from math import isfinite
from random import Random


def check(x, name, *, max_value=None):
    if not isfinite(float(x)) or x < 0:raise ValueError(name+' must be finite and nonnegative')
    if max_value is not None and x > max_value:raise ValueError(name+' exceeds allowed fraction')
    return float(x)

@dataclass(frozen=True)
class ScreeningCase:
    hectares:float
    years:int
    baseline_proxy_tco2e_ha_yr:float
    project_proxy_tco2e_ha_yr:float
    leakage_proxy_tco2e_ha_yr:float
    nonpermanence_reserve_fraction:float
    data_status:str='ILLUSTRATIVE'

    def __post_init__(self):
        for key in ('hectares','baseline_proxy_tco2e_ha_yr','project_proxy_tco2e_ha_yr','leakage_proxy_tco2e_ha_yr'):
            check(getattr(self,key),key)
        check(self.nonpermanence_reserve_fraction,'nonpermanence_reserve_fraction',max_value=1)
        if not isinstance(self.years,int) or self.years < 1 or self.years > 100:
            raise ValueError('years must be integer in 1..100')
        if self.data_status!='ILLUSTRATIVE':
            raise ValueError('Demo cannot masquerade as observed or certified')


def calculate(case:ScreeningCase)->dict:
    """Net modeled annual difference and a withheld-reserve scenario; not issuance."""
    net_per_ha=(case.baseline_proxy_tco2e_ha_yr-
                case.project_proxy_tco2e_ha_yr-
                case.leakage_proxy_tco2e_ha_yr)
    net_year=net_per_ha*case.hectares
    technical_total=net_year*case.years
    after_reserve=technical_total*(1-case.nonpermanence_reserve_fraction)
    return {'data_status':case.data_status,'hectares':case.hectares,
            'time_horizon_years':case.years,'technical_difference_tco2e_ha_yr':net_per_ha,
            'technical_difference_tco2e_year':net_year,
            'technical_difference_over_horizon_tco2e':technical_total,
            'after_illustrative_reserve_tco2e':after_reserve,
            'credit_units_issued':0,
            'interpretation':'scenario bookkeeping, not registry issuance or credit eligibility'}


def variation(case:ScreeningCase,project_factors:list[float],leakage_factors:list[float])->list[dict]:
    out=[]
    for p in project_factors:
        for l in leakage_factors:
            scenario=replace(case,project_proxy_tco2e_ha_yr=float(p),
                                     leakage_proxy_tco2e_ha_yr=float(l))
            out.append(calculate(scenario)|{'project_factor':p,'leakage_factor':l})
    return out


def monte_carlo(case: ScreeningCase, *, n:int=4000,seed:int=2026,
                baseline_range:tuple=(4.5,5.0,5.5),
                project_range:tuple=(1.5,2.0,2.5),
                leakage_range:tuple=(0.1,.3,.6))->dict:
    if not isinstance(n,int) or n<100 or n>200000:raise ValueError('n 100..200000')
    if not isinstance(seed,int):raise ValueError('seed must be integer')
    for spec in (baseline_range,project_range,leakage_range):
        if len(spec)!=3 or not (0<=spec[0]<=spec[1]<=spec[2]):
            raise ValueError('triangular min <= mode <= max; all nonnegative')
    random=Random(seed)
    draws=[]
    for _ in range(n):
        baseline=random.triangular(baseline_range[0],baseline_range[2],baseline_range[1])
        project=random.triangular(project_range[0],project_range[2],project_range[1])
        leakage=random.triangular(leakage_range[0],leakage_range[2],leakage_range[1])
        draws.append((baseline-project-leakage)*case.hectares*case.years)
    draws.sort()
    def quantile(p):
        index=p*(n-1);low=int(index);high=min(n-1,low+1)
        return draws[low]*(1-index+low)+draws[high]*(index-low)
    return dict(n=n,seed=seed,p05_technical_tco2e=quantile(.05),
                median_technical_tco2e=quantile(.5),p95_technical_tco2e=quantile(.95),
                share_negative_technical=sum(x<0 for x in draws)/n,
                uncertainty_type='ILLUSTRATIVE PARAMETER SENSITIVITY, not confidence interval')
