"""Validate Codee MCR/MVC *metadata* and dependency logic, not mathematics.
Requires jsonschema; e.g. python validate_metadata.py --mcr mcr-sample.json --mvc mvc-sample.json
"""
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent


def load(path):
    with open(path, encoding="utf8") as f:
        return json.load(f)


def acyclic(items, id_name):
    by_id = {x[id_name]:x for x in items}
    assert len(by_id) == len(items), f"duplicate {id_name}"
    visited, active = set(), set()
    def dfs(k):
        assert k in by_id, f"missing dependency {k}"
        assert k not in active, f"cyclic dependency {k}"
        if k in visited:return
        active.add(k)
        for dep in by_id[k].get("depends_on", []):dfs(dep)
        active.remove(k); visited.add(k)
    for k in by_id:dfs(k)
    return by_id


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mcr", type=Path, default=Path(__file__).with_name("mcr-sample.json"))
    p.add_argument("--mvc", type=Path, default=Path(__file__).with_name("mvc-sample.json"))
    a=p.parse_args()
    mcr,mvc=load(a.mcr),load(a.mvc)
    for name,data in [("mcr",mcr),("mvc",mvc)]:
        schema=load(ROOT/"schemas"/f"{name}-v1.schema.json")
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(data)
    claims=acyclic(mcr["claims"],"id")
    obligations=acyclic(mvc["obligations"],"obligation_id")
    assert all(t in claims for t in mcr["targets"])
    assert all(t in claims for t in mvc["target_claim_ids"])
    assert all(o["claim_id"] in claims for o in obligations.values())
    if mvc["project_status"] == "CERTIFIED":
        assert mvc["implementation_fidelity"] == "VERIFIED"
        assert mvc["mathematical_validity"] == "VERIFIED"
        assert obligations and all(o["status"] == "VERIFIED" for o in obligations.values())
        assert all(o["evidence"] and all(e.get("checked") is True and e.get("kind") != "NUMERICAL_EXPERIMENT" for e in o["evidence"]) for o in obligations.values())
    print("PASS: JSON schemas, identifiers and dependency DAG; mathematical proof NOT assessed")

if __name__ == "__main__":main()
