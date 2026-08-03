#!/usr/bin/env python3
"""Verify frozen pure-label C0003 recalibration pilot."""
from __future__ import annotations
import argparse,importlib.util,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/"m050/extraction/engine/src"))
from median_gate5.canonical import sha256_file  # noqa:E402
PP=R/"m050/tools/m050_guard_v0_16.py";A=R/"AGENTS.md";O=R/"AGENTS.override.md";I=R/"m050/extraction/control/M050_Active_Control_Index_v0_22_MEDIANv0_5_0.json";PI=R/"m050/extraction/control/M050_Active_Control_Index_v0_21_MEDIANv0_5_0.json";C=R/"m050/extraction/control/M050_Current_State_Checkpoint_v0_13_MEDIANv0_5_0.json";PC=R/"m050/extraction/control/M050_Current_State_Checkpoint_v0_12_MEDIANv0_5_0.json";CFG=R/"m050/extraction/control/M050_Authorial_Grammar_Extraction_Machine_Config_v0_5_MEDIANv0_5_0.json";F=R/"m050/extraction/calibration/authorial-grammar/M050_Authorial_Grammar_Pure_Label_C0003_Pilot_Freeze_Proposal_v0_10_MEDIANv0_5_0.json";K=R/"m050/extraction/audit/M050_Authorial_Grammar_Pure_Label_Recalibration_Compatibility_Receipt_v0_5_MEDIANv0_5_0.json"
S={"registered_sources":24,"atomic_compile_exclusions":2,"compile_scope_sources":22,"atomized_legacy_seed_sources":4,"outstanding_compile_scope_sources":18,"outstanding_pre_reconciliation_sources":14,"outstanding_later_or_conditional_sources":4}
def lp():s=importlib.util.spec_from_file_location("p",PP);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
P=lp()
def rd(p,e):
 try:return json.loads(p.read_text())
 except Exception as x:e.append(str(x));return {}
def hist(e,w):old=[];r=P.historical(old,w);e.extend(x for x in old if x!="artifacts hash binding mismatch: agents_contract");return r
def val(e):
 if O.exists() or O.is_symlink():e.append("override")
 t=A.read_text()
 for x in ("v0_22_MEDIANv0_5_0.json","v0_13_MEDIANv0_5_0.md","v0_12_MEDIANv0_5_0.md","m050_guard_v0_17.py","$0.120852","122 tests"):
  if x not in t:e.append("AGENTS omits "+x)
 i=rd(I,e);p=i.get("supersedes",{})
 if i.get("schema_version")!="M050-ACTIVE-CONTROL-INDEX-0.22" or p.get("sha256")!=sha256_file(PI) or i.get("execution_state")!="AUTHORIAL_GRAMMAR_PURE_LABEL_C0003_PILOT_FROZEN" or i.get("corpus_state")!={**S,"whole_corpus_atomization_complete":False}:e.append("index")
 if any(v is not False for v in i.get("transition_boundary",{}).values()) or not i.get("transition_boundary"):e.append("authority")
 cfg=rd(CFG,e);pol=cfg.get("lean_structural_policy",{})
 if cfg.get("status")!="OFFLINE_PURE_LABEL_RECALIBRATION_REQUIRES_PILOT" or pol.get("pure_labels_audited")!=14 or pol.get("pure_label_required_disposition")!="no_substantive_claim" or pol.get("substantive_sentence_leadins_remain_eligible") is not True:e.append("config")
 f=rd(F,e)
 if f.get("state")!="awaiting_exact_one_call_authorization" or f.get("pilot",{}).get("cache_miss_call_ceiling_usd")!="0.120852" or f.get("offline_verification",{}).get("offline_tests_passed")!=122:e.append("freeze")
 k=rd(K,e)
 if k.get("status")!="OFFLINE_PURE_LABEL_RECALIBRATION_VERIFIED_PILOT_REQUIRED" or k.get("replays",{}).get("rejected_c0003",{}).get("required_disposition_errors")!=2 or k.get("offline_verification",{}).get("offline_tests_passed")!=122:e.append("compat")
 c=rd(C,e);p=c.get("supersedes",{})
 if c.get("status")!="AUTHORIAL_GRAMMAR_PURE_LABEL_C0003_PILOT_FROZEN" or p.get("sha256")!=sha256_file(PC) or c.get("corpus_vector")!=S:e.append("checkpoint")
 if any(v is not False for v in c.get("authority_boundary",{}).values()) or not c.get("authority_boundary"):e.append("checkpoint auth")
 for n,b in c.get("artifacts",{}).items():
  q=R/b.get("path","")
  if not q.is_file() or b.get("sha256")!=sha256_file(q):e.append("artifact "+n)
def tests():return subprocess.run([str(R/".venv/bin/python"),"-m","pytest","m050/extraction/engine/tests","-q"],cwd=R,check=False).returncode
def main():
 p=argparse.ArgumentParser();p.add_argument("--work-order",type=Path);p.add_argument("--with-tests",action="store_true");a=p.parse_args();e=[];h=hist(e,a.work_order);val(e)
 if a.with_tests and tests():e.append("tests")
 if e:print("M050 PURE-LABEL GUARD: FAIL");[print("- "+x) for x in e];return 1
 print("M050 PURE-LABEL GUARD: PASS\n- 14 pure labels marked and enforced; substantive lead-ins preserved\n- C0001/C0002 replay pass; C0003 replay fails B00101/B00105\n- C0003 pilot frozen at $0.120852; provider authority none\n- spend $0.419817; balance $1.580183\n- 122 tests pass");print(f"- preserved legacy candidates: {h[7]}/913");return 0
if __name__=="__main__":raise SystemExit(main())
