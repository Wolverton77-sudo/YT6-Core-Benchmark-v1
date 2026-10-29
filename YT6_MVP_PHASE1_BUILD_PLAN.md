YT6 AI Interaction Stability Assessment
Phase 1 — Internal Prototype Build Plan
Document Control
Company: YT6 Clarity Systems Ltd
Product: YT6 AI Interaction Stability Assessment
Phase: Phase 1 — Internal Prototype
Version: Draft 0.1
Status: READY FOR IMPLEMENTATION PLANNING
Parent specification: YT6_MVP_BUILD_SPECIFICATION.md

1. Phase 1 Objective
Build the smallest internal prototype capable of completing one controlled Baseline-versus-YT6 assessment from task selection through evidence export.

Phase 1 exists to prove the assessment workflow can operate end to end.

It is not the commercial production version.

2. Phase 1 Definition of Success
Phase 1 succeeds when one complete assessment can be performed containing:

one fixed YT6 v2 task;
one Baseline run;
one matched YT6 run;
preserved raw inputs;
preserved raw outputs;
generated run IDs;
masked outputs for review;
reviewer scoring;
automatic score calculation;
a Baseline-versus-YT6 comparison;
an exported evidence report;
sufficient provenance to reproduce what happened.
The prototype must retain failures instead of hiding them.

3. Phase 1 Scope
IN SCOPE
fixed task selection;
assessment creation;
run record creation;
Baseline condition recording;
YT6 condition recording;
manual AI execution if necessary;
raw input/output capture;
condition masking;
human reviewer scoring;
automatic score calculation;
drift/failure recording;
evidence hashes;
comparison view;
report export;
basic audit record.
OUT OF SCOPE
Microsoft Copilot integration;
Marketplace publication;
customer billing;
enterprise multi-tenancy;
large-scale analytics;
autonomous scoring;
multiple model integrations;
complete YT6 architecture visualisation;
production compliance certification;
customer-specific training;
automatic claims about YT6 performance.
4. Build Principle
Build only what is required to complete this chain:

TASK
  ↓
ASSESSMENT
  ↓
BASELINE RUN
  ↓
YT6 RUN
  ↓
RAW EVIDENCE
  ↓
BLIND REVIEW
  ↓
SCORE
  ↓
COMPARISON
  ↓
REPORT
If a proposed feature does not directly support this chain, defer it.

5. Phase 1 Build Tasks
P1-01 — Create Prototype Project
Create the application project and establish:

source-code location;
configuration structure;
data-storage location;
evidence-storage location;
local development environment;
application version identifier.
Completion test:

The prototype starts successfully and displays a basic application page.

P1-02 — Load One Fixed Benchmark Task
Start with one task from:

YT6_V2_FIXED_DATASET.md

The prototype must store:

task ID;
category;
title;
exact prompt;
turn sequence;
task version;
dataset version.
Do not manually rewrite the task during execution.

Completion test:

The application displays the selected task exactly as stored.

P1-03 — Create Assessment Record
Implement creation of an assessment containing:

assessment ID;
task ID;
provider;
product/model;
model version if known;
protocol version;
dataset version;
Baseline condition version;
YT6 condition version;
creation timestamp;
assessment status.
Completion test:

Creating an assessment produces a persistent unique assessment record.

P1-04 — Generate Run Records
For each assessment create:

Run A — Baseline
Run B — YT6
Each run receives:

unique run ID;
condition;
task ID;
repetition;
status;
timestamps;
condition version;
evidence fields.
Completion test:

One assessment produces two distinguishable but linked run records.

P1-05 — Implement Baseline Capture
Phase 1 may initially use manual AI execution.

The operator:

opens the selected AI system;
starts a fresh session;
submits the exact fixed task;
captures the complete response;
enters/imports the raw response into the prototype;
records available model/environment information.
The system must preserve the submitted task and captured output.

Completion test:

A Baseline run contains immutable raw input and output records.

P1-06 — Implement YT6 Capture
Use the same tested AI system and same fixed task.

The operator:

starts a fresh session;
loads the defined YT6 prototype condition;
submits the identical fixed task;
captures the complete response;
enters/imports the raw response;
records the YT6 condition version.
Completion test:

The prototype contains a YT6 run matched to the corresponding Baseline run.

P1-07 — Evidence Hashing
Generate a reproducible hash for each preserved evidence record.

At minimum hash:

exact input;
exact raw output;
condition/version identifier;
run identifier.
Store the generated hash with the run.

Completion test:

Unmodified evidence reproduces the stored hash.

A changed evidence record produces a different hash.

P1-08 — Build Blind Review View
Create neutral labels:

Output X
Output Y
The reviewer view must not reveal:

Baseline;
YT6;
Condition A;
Condition B;
YT6 package information.
The assignment of X/Y should be stored separately.

Completion test:

A reviewer can inspect both outputs without seeing their experimental condition.

P1-09 — Implement Reviewer Form
For each masked output collect:

Intention preservation: 0–4
Constraint compliance: 0–4
Action clarity: 0–4
Multi-turn consistency: 0–4
Also collect:

drift-event count;
unsupported assumptions;
critical failure;
reviewer notes;
reviewer identifier;
submission timestamp.
Completion test:

A reviewer can submit a complete score for Output X and Output Y.

P1-10 — Implement Score Calculation
Calculate:

Dimension total =
intention preservation
+ constraint compliance
+ action clarity
+ multi-turn consistency
Then:

Clarity score =
(Dimension total ÷ 16) × 100
After review is submitted and the condition mapping is revealed:

Paired difference =
YT6 score − Baseline score
Completion test:

Known test inputs produce the expected mathematical result.

P1-11 — Record Failures and Drift
The prototype must permit recording:

drift event;
unsupported assumption;
missed clarification;
format failure;
symbol failure;
technical failure;
protocol deviation;
evidence incompleteness.
Do not require every field to contain a positive/negative answer if it was not observed.

Use null or equivalent for unknown information.

Completion test:

An unsuccessful YT6 run can be stored fully without being deleted or converted into a successful run.

P1-12 — Build Comparison View
After scoring, display:

Assessment ID
Task ID

Baseline score
YT6 score
Paired difference

Baseline drift events
YT6 drift events

Baseline critical failure
YT6 critical failure

Evidence status
Protocol deviations
Also provide access to the raw evidence.

Completion test:

The displayed numbers correspond exactly to the underlying review records.

P1-13 — Generate Evidence Report
Generate an exportable assessment containing:

assessment ID;
task;
system/model information;
condition versions;
protocol version;
dataset version;
run IDs;
raw inputs;
raw outputs;
evidence hashes;
reviewer scores;
drift/failure information;
paired result;
deviations;
limitations.
Include:

This assessment measures the tested task and environment only. It does not establish universal YT6 performance.

Completion test:

An exported report can be traced back to the underlying assessment, runs and reviews.

P1-14 — Maintain Audit Record
Record important state changes including:

assessment created;
run created;
evidence added;
run failed;
retry created;
review submitted;
result calculated;
report exported.
Do not silently overwrite important records.

Completion test:

The sequence of the assessment can be reconstructed from the audit record.

6. First Internal Test
The first test is not part of the formal v2 benchmark.

Label it:

PHASE-1 ENGINEERING TEST
NOT FORMAL BENCHMARK EVIDENCE
Use one fixed task.

Recommended objective:

Verify the software and evidence workflow, not whether YT6 wins.

The engineering test asks:

Was the same task used?
Were both outputs preserved?
Were run IDs generated?
Was masking successful?
Did scoring calculate correctly?
Did the report export?
Can another person trace the result?
Any performance result from this engineering test must remain separate from the formal benchmark.

7. Phase 1 Data Requirements
Minimum persistent entities:

Task
Assessment
Run
Review
Deviation
AuditEvent
Minimum file/evidence artefacts:

raw_input
raw_output
evidence_hash
assessment_report
8. Evidence Directory Structure
Recommended logical structure:

phase1/
├── assessments/
├── runs/
│   ├── baseline/
│   └── yt6/
├── reviews/
├── reports/
├── deviations/
└── audit/
The implementation may use a database/object store rather than physical directories, but equivalent logical separation must exist.

9. Phase 1 Roles
Operator
creates assessment;
performs or records runs;
preserves evidence;
does not modify outputs.
Reviewer
sees masked outputs;
scores each output;
records observable failures;
does not see condition identity during scoring.
Administrator
manages prototype configuration;
manages condition and dataset versions;
audits evidence integrity.
For an early internal prototype, one person may technically hold multiple roles, but role separation must still be recorded.

10. Phase 1 Quality Gates
Gate A — Task Integrity
PASS when:

exact task stored;
task version recorded;
task cannot change silently between conditions.
Gate B — Condition Integrity
PASS when:

Baseline and YT6 versions are recorded;
the intended condition difference is identifiable.
Gate C — Evidence Integrity
PASS when:

complete inputs preserved;
complete outputs preserved;
hashes generated;
failed runs retained.
Gate D — Review Integrity
PASS when:

reviewer cannot see the condition;
original review is preserved;
score calculation is correct.
Gate E — Report Integrity
PASS when:

report maps to the underlying evidence;
limitations are shown;
no unsupported performance claim is generated.
11. Phase 1 Definition of Done
Phase 1 is complete only when:

ONE FIXED TASK
      ↓
ONE BASELINE RUN
      ↓
ONE YT6 RUN
      ↓
RAW EVIDENCE PRESERVED
      ↓
OUTPUTS MASKED
      ↓
HUMAN REVIEW COMPLETED
      ↓
SCORES CALCULATED
      ↓
COMPARISON DISPLAYED
      ↓
REPORT EXPORTED
      ↓
SECOND PERSON CAN TRACE THE ASSESSMENT
The prototype does not need to demonstrate that YT6 wins.

It must demonstrate that YT6 can be tested properly.

12. Phase 1 Stop Conditions
Stop the build and correct the problem if:

evidence can be silently edited;
condition labels leak into blinded review;
Baseline and YT6 tasks differ;
failed runs disappear;
score calculation is incorrect;
version information is lost;
the report cannot be traced to raw evidence;
the system automatically treats YT6 as successful.
13. Phase 2 Entry Gate
Do not begin Phase 2 until:

Phase 1 Definition of Done satisfied;
engineering test completed;
discovered defects recorded;
critical defects corrected;
another person has followed the workflow;
evidence export checked;
no formal benchmark evidence has been mixed with engineering-test data.
14. Current Position
MVP BUILD SPECIFICATION: COMPLETE FOR DRAFT
PHASE 1 BUILD PLAN: COMPLETE FOR DRAFT
SOFTWARE IMPLEMENTATION: NOT STARTED
ENGINEERING TEST: NOT STARTED
FORMAL V2 BENCHMARK: NOT STARTED
MVP: NOT YET ACHIEVED
15. Immediate Build Order
Execute in this sequence:

01  Prototype project
02  One fixed task
03  Assessment record
04  Baseline/YT6 run records
05  Raw evidence capture
06  Evidence hashing
07  Blind output view
08  Reviewer form
09  Score calculation
10  Failure/deviation record
11  Comparison view
12  Evidence report
13  Audit record
14  Internal engineering test
Do not expand the product until this chain works end to end.

END OF YT6 MVP PHASE 1 BUILD PLAN
