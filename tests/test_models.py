import pytest
from dataclasses import replace
from math import nan,isclose
from carbon_audit.model import ScreeningCase,calculate,variation,monte_carlo
from carbon_audit.evidence import Claim,summarize_claims

@pytest.fixture
def case():return ScreeningCase(600,10,5,2,.3,.2)

def test_arithmetic(case):
    d=calculate(case)
    assert isclose(d['technical_difference_tco2e_ha_yr'],2.7)
    assert isclose(d['technical_difference_over_horizon_tco2e'],16200)
    assert isclose(d['after_illustrative_reserve_tco2e'],12960)
    assert d['credit_units_issued']==0

def test_negative_model_difference(case):
    d=calculate(replace(case,project_proxy_tco2e_ha_yr=9))
    assert d['technical_difference_tco2e_year'] < 0
    assert d['credit_units_issued']==0

@pytest.mark.parametrize('params',[{'hectares':-1},{'hectares':nan},{'years':0},{'years':110},
    {'baseline_proxy_tco2e_ha_yr':-1},{'nonpermanence_reserve_fraction':1.5},
    {'data_status':'MEASURED'}])
def test_invalid(case,params):
    with pytest.raises(ValueError):replace(case,**params)

def test_variation_cardinality(case):assert len(variation(case,[1,2],[.1,.2]))==4

def test_monte_carlo_deterministic(case):
    a=monte_carlo(case,n=500,seed=77);b=monte_carlo(case,n=500,seed=77)
    assert a==b
    assert a['p05_technical_tco2e']<=a['median_technical_tco2e']<=a['p95_technical_tco2e']

def test_monte_carlo_rejects_bad_n(case):
    with pytest.raises(ValueError):monte_carlo(case,n=10)

def test_monte_carlo_rejects_bad_support(case):
    with pytest.raises(ValueError):monte_carlo(case,baseline_range=(3,2,5))

def test_claim_validation():
    c=Claim('A','Claim','Source','pricing_unverified')
    assert summarize_claims([c])=={'pricing_unverified':1}

def test_claims_not_auto_verified():
    with pytest.raises(ValueError):Claim('A','Claim','Source','independently_verified')

def test_claim_malformed_evidence():
    with pytest.raises(ValueError):Claim('A','Claim','Source','independently_verified','source document','editor','2026-10-03')

def test_claim_duplicate():
    c=Claim('A','Claim','Source','planning_assumption_unverified')
    with pytest.raises(ValueError):summarize_claims([c,c])
