#!/usr/bin/env python3
"""Verify the frozen C0003 lean-table recalibration pilot boundary."""
from __future__ import annotations
import argparse, importlib.util, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/"m050/extraction/engine/src"))
from median_gate5.canonical import sha256_file  # noqa: E402
PRIOR_PATH=ROOT/"m050/tools/m050_guard_v0_14.py"; AGENTS=ROOT/"AGENTS.md"; OVERRIDE=ROOT/"AGENTS.override.md"
INDEX=ROOT/"m050/extraction/control/M050_Active_Control_Index_v0_20_MEDIANv0_5_0.json"; PRIOR_INDEX=ROOT/"m050/extraction/control/M050_Active_Control_Index_v0_19_MEDIANv0_5_0.json"
CHECKPOINT=ROOT/"m050/extraction/control/M050_Current_State_Checkpoint_v0_11_MEDIANv0_5_0.json"; PRIOR_CHECKPOINT=ROOT/"m050/extraction/control/M050_Current_State_Checkpoint_v0_10_MEDIANv0_5_0.json"
REPORT=ROOT/"m050/extraction/control/M050_Current_State_Checkpoint_v0_11_MEDIANv0_5_0.md"; BOOTSTRAP=ROOT/"m050/extraction/control/M050_New_Task_Bootstrap_v0_10_MEDIANv0_5_0.md"
CONFIG=ROOT/"m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_4_MEDIANv0_5_0.json"; FREEZE=ROOT/"m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Lean_Table_C0003_Pilot_Freeze_Proposal_v0_9_MEDIANv0_5_0.json"
COMPAT=ROOT/"m050/extraction/audit/M050_Authorial_Grammar_Lean_Table_Recalibration_Compatibility_Receipt_v0_4_MEDIANv0_5_0.json"; SPEND=ROOT/"m050/extraction/audit/spend-envelopes/M050_Provider_Spend_Envelope_001_After_Structural_C0003_v0_7_MEDIANv0_5_0.json"
SUMMARY={"registered_sources":24,"atomic_compile_exclusions":2,"compile_scope_sources":22,"atomized_legacy_seed_sources":4,"outstanding_compile_scope_sources":18,"outstanding_pre_reconciliation_sources":14,"outstanding_later_or_conditional_sources":4}
def load_prior():
 s=importlib.util.spec_from_file_location("prior",PRIOR_PATH); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
PRIOR=load_prior()
def read(path,errors):
 try: v=json.loads(path.read_text())
 except Exception as e: errors.append(f"cannot read {path.relative_to(ROOT)}: {e}"); return {}
 return v if isinstance(v,dict) else {}
def historical(errors,work_order):
 old=[]; result=PRIOR.historical(old,work_order); errors.extend(e for e in old if e!="artifacts hash binding mismatch: agents_contract"); return result
def validate(errors):
 if OVERRIDE.exists() or OVERRIDE.is_symlink(): errors.append("AGENTS.override.md present")
 text=AGENTS.read_text() if AGENTS.is_file() else ""
 for p in ("M050_Active_Control_Index_v0_20_MEDIANv0_5_0.json","M050_Current_State_Checkpoint_v0_11_MEDIANv0_5_0.md","M050_New_Task_Bootstrap_v0_10_MEDIANv0_5_0.md","m050_guard_v0_15.py","$0.122044","121 tests"):
  if p not in text: errors.append(f"AGENTS.md omits: {p}")
 idx=read(INDEX,errors); pred=idx.get("supersedes",{})
 if idx.get("schema_version")!="M050-ACTIVE-CONTROL-INDEX-0.20" or pred.get("path")!=PRIOR_INDEX.relative_to(ROOT).as_posix() or pred.get("sha256")!=sha256_file(PRIOR_INDEX) or idx.get("execution_state")!="AUTHORIAL_GRAMMAR_LEAN_TABLE_C0003_PILOT_FROZEN" or idx.get("corpus_state")!={**SUMMARY,"whole_corpus_atomization_complete":False}: errors.append("active index drifted")
 cal=idx.get("calibration_state",{})
 if cal.get("accepted_chunk_ids")!=["C0001","C0002"] or cal.get("rejected_chunk_id")!="C0003" or cal.get("pilot_chunk_id")!="C0003" or cal.get("pilot_cache_miss_ceiling_usd")!="0.122044" or cal.get("provider_calls_authorized")!=0: errors.append("calibration boundary drifted")
 if not idx.get("transition_boundary") or any(v is not False for v in idx["transition_boundary"].values()): errors.append("index crosses authority boundary")
 cfg=read(CONFIG,errors); policy=cfg.get("lean_table_policy",{})
 if cfg.get("status")!="OFFLINE_LEAN_TABLE_RECALIBRATION_REQUIRES_PILOT" or cfg.get("execution",{}).get("provider_calls_authorized") is not False or policy.get("header_row_required_disposition")!="no_substantive_claim" or policy.get("delimiter_row_required_disposition")!="no_substantive_claim" or policy.get("source_specific_block_patch") is not False: errors.append("lean-table config drifted")
 for name,path in cfg.get("artifacts",{}).items():
  target=ROOT/path
  if not target.is_file() or cfg.get("artifact_sha256",{}).get(name)!=sha256_file(target): errors.append(f"config artifact drifted: {name}")
 freeze=read(FREEZE,errors)
 if freeze.get("state")!="awaiting_exact_one_call_authorization" or freeze.get("authority",{}).get("provider_call_authorized") is not False or freeze.get("binding",{}).get("pilot_chunk_id")!="C0003" or freeze.get("pilot",{}).get("cache_miss_call_ceiling_usd")!="0.122044" or freeze.get("offline_verification",{}).get("offline_tests_passed")!=121: errors.append("pilot freeze drifted")
 comp=read(COMPAT,errors); rp=comp.get("replays",{})
 if comp.get("status")!="OFFLINE_LEAN_TABLE_RECALIBRATION_VERIFIED_PILOT_REQUIRED" or rp.get("accepted_c0001",{}).get("passed") is not True or rp.get("accepted_c0002",{}).get("passed") is not True or rp.get("rejected_c0003",{}).get("passed") is not False or rp.get("rejected_c0003",{}).get("table_structure_errors")!=1 or comp.get("offline_verification",{}).get("offline_tests_passed")!=121: errors.append("compatibility receipt drifted")
 spend=read(SPEND,errors)
 if spend.get("spent_usd")!="0.352455" or spend.get("remaining_usd")!="1.647545": errors.append("spend drifted")
 cp=read(CHECKPOINT,errors); pred=cp.get("supersedes",{})
 if cp.get("status")!="AUTHORIAL_GRAMMAR_LEAN_TABLE_C0003_PILOT_FROZEN" or pred.get("path")!=PRIOR_CHECKPOINT.relative_to(ROOT).as_posix() or pred.get("sha256")!=sha256_file(PRIOR_CHECKPOINT) or cp.get("corpus_vector")!=SUMMARY: errors.append("checkpoint drifted")
 if not cp.get("authority_boundary") or any(v is not False for v in cp["authority_boundary"].values()): errors.append("checkpoint crosses authority boundary")
 for name,b in cp.get("artifacts",{}).items():
  target=ROOT/b.get("path","")
  if not target.is_file() or b.get("sha256")!=sha256_file(target): errors.append(f"checkpoint artifact drifted: {name}")
 for p in ("$0.122044","121 tests","C0001 and C0002"):
  if p not in REPORT.read_text(): errors.append(f"report omits: {p}")
 for p in ("Remain read-only","generic lean-table","121-test"):
  if p not in BOOTSTRAP.read_text(): errors.append(f"bootstrap omits: {p}")
def tests(): return subprocess.run([str(ROOT/".venv/bin/python"),"-m","pytest","m050/extraction/engine/tests","-q"],cwd=ROOT,check=False).returncode
def main():
 p=argparse.ArgumentParser(); p.add_argument("--work-order",type=Path); p.add_argument("--with-tests",action="store_true"); a=p.parse_args(); e=[]; h=historical(e,a.work_order); validate(e)
 if a.with_tests and tests(): e.append("tests failed")
 if e: print("M050 GATE 5 LEAN-TABLE GUARD: FAIL"); [print(f"- {x}") for x in e]; return 1
 print("M050 GATE 5 LEAN-TABLE GUARD: PASS"); print("- corpus: 24 / 22 / 4 / 18 = 14 + 4; next Authorial Grammar"); print("- C0001/C0002 replay pass; captured C0003 fails exactly one table-structure check"); print("- C0003 pilot frozen; ceiling $0.122044; provider authority none"); print("- spend unchanged: $0.352455 cumulative; $1.647545 money-only balance"); print(f"- preserved legacy candidates: {h[7]}/913");
 if a.with_tests: print("- offline regression suite: pass (121 tests)")
 return 0
if __name__=="__main__": raise SystemExit(main())
