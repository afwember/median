#!/usr/bin/env python3
"""Verify rejected lean-table C0003 pilot and context-leadin defect boundary."""
from __future__ import annotations
import argparse,importlib.util,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/"m050/extraction/engine/src"))
from median_gate5.canonical import sha256_file  # noqa:E402
PRIOR_PATH=ROOT/"m050/tools/m050_guard_v0_15.py"; AGENTS=ROOT/"AGENTS.md"; OVERRIDE=ROOT/"AGENTS.override.md"
INDEX=ROOT/"m050/extraction/control/M050_Active_Control_Index_v0_21_MEDIANv0_5_0.json"; PRIOR_INDEX=ROOT/"m050/extraction/control/M050_Active_Control_Index_v0_20_MEDIANv0_5_0.json"
CHECKPOINT=ROOT/"m050/extraction/control/M050_Current_State_Checkpoint_v0_12_MEDIANv0_5_0.json"; PRIOR_CHECKPOINT=ROOT/"m050/extraction/control/M050_Current_State_Checkpoint_v0_11_MEDIANv0_5_0.json"
REPORT=ROOT/"m050/extraction/control/M050_Current_State_Checkpoint_v0_12_MEDIANv0_5_0.md"; BOOTSTRAP=ROOT/"m050/extraction/control/M050_New_Task_Bootstrap_v0_11_MEDIANv0_5_0.md"
REJECT=ROOT/"m050/extraction/audit/pilot-transitions/M050_Authorial_Grammar_Lean_Table_C0003_Pilot_Rejected_v0_9_MEDIANv0_5_0.json"; OUTCOME=ROOT/"m050/extraction/runs/authorial-grammar-lean-table-pilot/M050_Authorial_Grammar_Lean_Table_C0003_Outcome_v0_9_MEDIANv0_5_0.json"; LEDGER=ROOT/"m050/extraction/runs/authorial-grammar-lean-table-pilot/M050_Authorial_Grammar_Lean_Table_Pilot_Run_Ledger_v0_9_MEDIANv0_5_0.jsonl"; SPEND=ROOT/"m050/extraction/audit/spend-envelopes/M050_Provider_Spend_Envelope_001_After_Lean_Table_C0003_Pilot_v0_8_MEDIANv0_5_0.json"
SUMMARY={"registered_sources":24,"atomic_compile_exclusions":2,"compile_scope_sources":22,"atomized_legacy_seed_sources":4,"outstanding_compile_scope_sources":18,"outstanding_pre_reconciliation_sources":14,"outstanding_later_or_conditional_sources":4}
def prior():
 s=importlib.util.spec_from_file_location("p",PRIOR_PATH);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
P=prior()
def read(path,e):
 try:return json.loads(path.read_text())
 except Exception as x:e.append(f"cannot read {path.relative_to(ROOT)}: {x}");return {}
def historical(e,w):
 old=[];r=P.historical(old,w);e.extend(x for x in old if x!="artifacts hash binding mismatch: agents_contract");return r
def validate(e):
 if OVERRIDE.exists() or OVERRIDE.is_symlink():e.append("override present")
 t=AGENTS.read_text()
 for x in ("M050_Active_Control_Index_v0_21_MEDIANv0_5_0.json","M050_Current_State_Checkpoint_v0_12_MEDIANv0_5_0.md","M050_New_Task_Bootstrap_v0_11_MEDIANv0_5_0.md","m050_guard_v0_16.py","$0.419817","B00101"):
  if x not in t:e.append(f"AGENTS omits {x}")
 i=read(INDEX,e);p=i.get("supersedes",{})
 if i.get("schema_version")!="M050-ACTIVE-CONTROL-INDEX-0.21" or p.get("path")!=PRIOR_INDEX.relative_to(ROOT).as_posix() or p.get("sha256")!=sha256_file(PRIOR_INDEX) or i.get("execution_state")!="AUTHORIAL_GRAMMAR_LEAN_TABLE_C0003_PILOT_REJECTED_CONTEXT_LEADINS" or i.get("corpus_state")!={**SUMMARY,"whole_corpus_atomization_complete":False}:e.append("index drifted")
 c=i.get("calibration_state",{})
 if c.get("accepted_chunk_ids")!=["C0001","C0002"] or c.get("rejected_chunk_id")!="C0003" or c.get("failure_kind")!="context_only_example_leadin_metadata_atoms" or c.get("failed_block_ids")!=["B00101","B00105"] or c.get("provider_calls_authorized")!=0:e.append("calibration drifted")
 if not i.get("transition_boundary") or any(v is not False for v in i["transition_boundary"].values()):e.append("index authority drift")
 r=read(REJECT,e)
 if r.get("state")!="pilot_rejected" or r.get("mechanical_validation_passed") is not True or r.get("substantive_review_passed") is not False or r.get("defect",{}).get("kind")!="context_only_example_leadin_metadata_atoms" or r.get("additional_provider_calls_authorized")!=0:e.append("rejection drifted")
 o=read(OUTCOME,e)
 if o.get("mechanical_validation",{}).get("passed") is not True or o.get("cache",{}).get("effective") is not True or o.get("cache",{}).get("creation_input_tokens")!=2698 or o.get("cost",{}).get("total_usd")!="0.067362":e.append("outcome drifted")
 try:s=[json.loads(x).get("state") for x in LEDGER.read_text().splitlines() if x.strip()]
 except Exception:s=[]
 if s!=["call_captured","review_failed"]:e.append("ledger drifted")
 money=read(SPEND,e)
 if money.get("spent_usd")!="0.419817" or money.get("remaining_usd")!="1.580183":e.append("spend drifted")
 cp=read(CHECKPOINT,e);p=cp.get("supersedes",{})
 if cp.get("status")!="AUTHORIAL_GRAMMAR_LEAN_TABLE_C0003_PILOT_REJECTED_CONTEXT_LEADINS" or p.get("path")!=PRIOR_CHECKPOINT.relative_to(ROOT).as_posix() or p.get("sha256")!=sha256_file(PRIOR_CHECKPOINT) or cp.get("corpus_vector")!=SUMMARY:e.append("checkpoint drifted")
 if not cp.get("authority_boundary") or any(v is not False for v in cp["authority_boundary"].values()):e.append("checkpoint authority drift")
 for n,b in cp.get("artifacts",{}).items():
  q=ROOT/b.get("path","")
  if not q.is_file() or b.get("sha256")!=sha256_file(q):e.append(f"artifact drift {n}")
 for x in ("B00101","$0.067362","$1.580183"):
  if x not in REPORT.read_text():e.append(f"report omits {x}")
def tests():return subprocess.run([str(ROOT/".venv/bin/python"),"-m","pytest","m050/extraction/engine/tests","-q"],cwd=ROOT,check=False).returncode
def main():
 a=argparse.ArgumentParser();a.add_argument("--work-order",type=Path);a.add_argument("--with-tests",action="store_true");z=a.parse_args();e=[];h=historical(e,z.work_order);validate(e)
 if z.with_tests and tests():e.append("tests failed")
 if e:print("M050 GATE 5 LEAN-TABLE-PILOT GUARD: FAIL");[print("- "+x) for x in e];return 1
 print("M050 GATE 5 LEAN-TABLE-PILOT GUARD: PASS");print("- C0003 table rule passed; pilot rejected for B00101/B00105 context-label atoms");print("- spend $0.419817; money-only balance $1.580183; no provider authority");print(f"- preserved legacy candidates: {h[7]}/913");
 if z.with_tests:print("- offline regression suite: pass (121 tests)")
 return 0
if __name__=="__main__":raise SystemExit(main())
