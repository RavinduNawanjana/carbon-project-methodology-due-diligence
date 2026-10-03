"""No claim becomes verified from draft provenance alone."""
from dataclasses import dataclass
from collections import Counter
VALID={'source_assertion_unverified','planning_assumption_unverified',
       'pricing_unverified','requires_methodology_check','illustrative_only',
       'independently_verified'}

@dataclass(frozen=True)
class Claim:
    claim_id:str
    claim_text:str
    origin_document:str
    status:str
    independent_evidence_link:str=''
    reviewer:str=''
    review_date:str=''

    def __post_init__(self):
        if not all((self.claim_id.strip(),self.claim_text.strip(),self.origin_document.strip())):
            raise ValueError('claim id/text/origin are required')
        if self.status not in VALID:raise ValueError('unrecognised evidence status')
        if self.status=='independently_verified':
            if not all((self.independent_evidence_link,self.reviewer,self.review_date)):
                raise ValueError('verified claim needs external locator, reviewer and review date')
            if not self.independent_evidence_link.startswith(('https://','evidence://')):
                raise ValueError('independent evidence must have an inspectable URI')

def summarize_claims(claims:list[Claim])->dict:
    ids=[c.claim_id for c in claims]
    if len(ids)!=len(set(ids)):raise ValueError('duplicate claims')
    return dict(Counter(c.status for c in claims))


def parse_claim_rows(rows:list[dict])->list[Claim]:
    return [Claim(**{k:v for k,v in row.items() if k in Claim.__dataclass_fields__}) for row in rows]
