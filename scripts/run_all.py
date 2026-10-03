from pathlib import Path
import csv,json
from carbon_audit.model import ScreeningCase,calculate,variation,monte_carlo
from carbon_audit.evidence import parse_claim_rows,summarize_claims
ROOT=Path(__file__).resolve().parents[1]

def csv_rows(p):
    with (ROOT/p).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))

def write(path,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    cases=[ScreeningCase(**{k:(v if k=='data_status' else int(v) if k=='years' else float(v)) for k,v in row.items()}) for row in csv_rows('data/illustrative/parameter_scenarios.csv')]
    write(ROOT/'outputs/ILLUSTRATIVE_scenario_arithmetic.csv',[calculate(c) for c in cases])
    write(ROOT/'outputs/ILLUSTRATIVE_grid_sensitivity.csv',variation(cases[0],[1.5,2,3],[.1,.3,.7]))
    mc=monte_carlo(cases[0],n=4000,seed=2026)
    (ROOT/'outputs').mkdir(exist_ok=True)
    (ROOT/'outputs/ILLUSTRATIVE_monte_carlo.json').write_text(json.dumps(mc,indent=2)+'\n')
    claims=parse_claim_rows(csv_rows('data/illustrative/source_claims_to_verify.csv'))
    report=summarize_claims(claims)
    (ROOT/'outputs/evidence_status_counts.json').write_text(json.dumps(report,indent=2)+'\n')
    assert report.get('independently_verified',0)==0
    print('Source claims audit:',report,'; no credit issuance calculated or asserted.')

if __name__=='__main__':main()
