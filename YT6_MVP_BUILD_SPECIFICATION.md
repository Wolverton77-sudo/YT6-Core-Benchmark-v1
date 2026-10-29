YT6 AI Interaction Stability Assessment
Minimum Viable Product Build Specification
Document Control
Company: YT6 Clarity Systems Ltd
Product: YT6 AI Interaction Stability Assessment
Document: MVP Build Specification
Version: Draft 0.1
Status: DRAFT — NOT APPROVED FOR PRODUCTION
Product stage: Working towards MVP
Primary benchmark: YT6-Core-Benchmark-v2
Primary claim under evaluation: YT6-CLAIM-001

1. Product Definition
The YT6 MVP is a controlled AI-interaction assessment application.

It allows a user to:

select a fixed multi-turn test task;
run the task under a baseline AI condition;
run the identical task under the YT6 condition;
preserve the complete inputs and outputs;
compare the two conditions;
record independent reviewer scores;
identify observable drift and constraint failures;
export a traceable evidence report.
The MVP does not claim that YT6 improves AI performance.

It creates the controlled mechanism needed to test whether an improvement occurs.

2. Product Hypothesis
Value Hypothesis
AI developers, evaluators and enterprise teams need a controlled way to identify where multi-turn AI systems lose:

user intention;
active constraints;
defined terminology;
required structure;
continuity across turns.
Solution Hypothesis
A paired baseline-versus-YT6 assessment will help users identify and measure differences in clarity, constraint retention and interaction drift.

Commercial Hypothesis
A person responsible for an AI workflow will find the assessment sufficiently useful to:

complete an assessment;
review the evidence;
export the results;
repeat the assessment;
request an assessment of their own workflow;
consider paying for the service.
3. Initial Product Name
YT6 AI Interaction Stability Assessment

Short Description
A controlled assessment tool that compares the same multi-turn AI task with and without the YT6 intervention.

Initial Commercial Category
B2B AI evaluation and interaction-quality assessment.

4. Initial User
The primary MVP user is:

A person responsible for evaluating, developing or governing a multi-turn AI workflow.

Possible early users include:

AI evaluators;
AI product managers;
software engineers;
responsible-AI reviewers;
startup founders building AI agents;
consultants assessing enterprise AI systems.
The MVP is not initially designed for general consumer use.

5. Primary User Job
The MVP must help the user answer:

Does the YT6 condition produce a measurable and reviewable difference from the baseline condition on the same AI task?

Secondary questions include:

Which constraints were retained or lost?
Was missing information invented?
Did the objective change?
Did symbol meaning remain stable?
Did the response preserve its required structure?
Did drift increase, decrease or remain unchanged?
Can another reviewer inspect the underlying evidence?
6. Core User Journey
SIGN IN
   ↓
CREATE ASSESSMENT
   ↓
SELECT FIXED TASK
   ↓
SELECT TESTED AI SYSTEM
   ↓
CONFIRM RUN SETTINGS
   ↓
RUN BASELINE CONDITION
   ↓
RUN YT6 CONDITION
   ↓
CAPTURE RAW EVIDENCE
   ↓
MASK CONDITION LABELS
   ↓
REVIEW AND SCORE OUTPUTS
   ↓
COMPARE RESULTS
   ↓
EXPORT EVIDENCE REPORT
The assessment is incomplete if either condition lacks raw evidence.

7. MVP Functional Scope
The MVP must provide eight core functions.

F-01 — User Access
The application must permit an authorised user to access the assessment workspace.

Minimum requirements:

user identity;
sign-in;
sign-out;
basic session protection.
A complex enterprise identity system is not required for the first internal build.

F-02 — Fixed Task Selection
The user must be able to select one task from the frozen YT6-Core-Benchmark-v2 dataset.

Each task record must include:

task ID;
category;
title;
exact prompt;
fixed turn sequence where applicable;
expected output format;
task version;
dataset version;
dataset hash.
The application must not allow the fixed task text to be silently edited during a formal benchmark run.

Initial task categories:

ambiguity;
emotional-pressure neutrality;
long-form continuity;
symbol pressure;
daily clarity.
F-03 — Assessment Configuration
Before a run begins, the user must record:

assessment ID;
selected task;
AI provider;
product or model;
model version where exposed;
account/access type;
execution route;
repetition number;
tool availability;
condition versions;
protocol version;
dataset version.
Unknown information must be recorded as unknown or null.

The application must not invent missing model or environment information.

F-04 — Baseline Execution
The application must execute or record the selected task under Condition A.

Condition A must receive:

the fixed benchmark task;
the standard capabilities of the tested AI system;
no YT6 condition package;
no Base44 package;
no CAR protocol;
no YT6 ambiguity, continuity or stability instructions.
The application must preserve:

exact input;
exact output;
turn order;
timestamp;
run identifier;
errors;
retries;
environment details;
evidence hash.
F-05 — YT6 Execution
The application must execute or record the same task under Condition B.

Condition B must receive:

the identical fixed benchmark task;
the same tested AI system;
the same normal tools and limits;
the frozen YT6 intervention package.
The application must preserve:

exact input;
exact output;
turn order;
loaded YT6 package version;
package hash;
timestamp;
run identifier;
errors;
retries;
environment details;
evidence hash.
No additional YT6 coaching may be introduced after the formal run begins.

F-06 — Side-by-Side Evidence View
The application must display the two run outputs side by side.

The evidence view must show:

task ID;
output label;
complete output;
turn boundaries;
run status;
technical errors;
evidence availability.
For blinded review, outputs should be labelled neutrally:

Output X
Output Y
The reviewer should not be shown which output is Baseline or YT6 until scoring is complete.

F-07 — Reviewer Scoring
The application must permit a reviewer to score each output independently.

Required dimensions:

intention preservation;
constraint compliance;
action clarity;
multi-turn consistency.
Each dimension is scored from 0 to 4.

The task-level score is:

(sum of four dimension scores ÷ 16) × 100
The reviewer must also be able to record:

drift events;
unsupported assumptions;
missed clarifications;
symbol-meaning failures;
format failures;
critical failure;
scoring notes;
uncertainty.
A reviewer score and a system-generated telemetry value must remain separate.

F-08 — Evidence Report
The application must generate an assessment report containing:

assessment ID;
task ID and category;
date and time;
tested system;
environment details;
protocol version;
dataset version;
Baseline condition version;
YT6 condition-package version;
run identifiers;
complete raw inputs;
complete raw outputs;
reviewer scores;
observed failures;
protocol deviations;
Baseline result;
YT6 result;
measured difference;
limitations;
evidence hashes.
The report must not state that YT6 is validated merely because the YT6 score is higher on one run.

8. Minimum Screens
The first version requires five screens.

Screen 1 — Sign In
Purpose:

Permit authorised access.

Elements:

YT6 AI Interaction Stability Assessment

Email
Password / identity provider

[Sign in]
Screen 2 — New Assessment
Purpose:

Configure a controlled assessment.

Elements:

New Assessment

Task:
[Select fixed task]

AI provider:
[Enter/select]

Product/model:
[Enter/select]

Model version:
[Enter if exposed]

Repetition:
[Number]

Protocol version:
[Read only]

Dataset version:
[Read only]

Baseline condition:
[Read only]

YT6 condition package:
[Read only]

[Validate Configuration]
[Run Assessment]
The application must block execution when required configuration fields are missing.

Screen 3 — Execution
Purpose:

Show run progress without altering the results.

Elements:

Assessment ID
Task ID

Baseline
Status: queued / running / complete / failed

YT6
Status: queued / running / complete / failed

Evidence capture
Status: pending / complete / incomplete

[View Technical Record]
The application must not automatically replace a failed run without recording the original failure.

Screen 4 — Blind Review
Purpose:

Allow independent scoring without revealing the condition.

Elements:

Task requirements

Output X
[Complete raw output]

Output Y
[Complete raw output]

For each output:

Intention preservation: 0–4
Constraint compliance: 0–4
Action clarity: 0–4
Multi-turn consistency: 0–4

Drift events:
[Record]

Critical failure:
[Yes / No]

Reviewer notes:
[Text]

[Submit Scores]
Once a reviewer submits scores, the original scores must remain preserved.

Corrections must create a revision record rather than overwrite the original submission silently.

Screen 5 — Results and Export
Purpose:

Show the controlled comparison and evidence status.

Elements:

YT6 Assessment Result

Baseline score
YT6 score
Paired difference

Task-level requirements
Observed drift
Critical failures
Reviewer agreement
Protocol deviations
Evidence completeness

[View Raw Evidence]
[Export Report]
The application must display:

This assessment measures the tested task and environment only.
It does not establish universal YT6 performance.
9. Data Model
User
{
  "user_id": "",
  "name": "",
  "email": "",
  "role": "operator | reviewer | administrator",
  "created_at": ""
}
Assessment
{
  "assessment_id": "",
  "task_id": "",
  "status": "draft | ready | running | review | complete | invalid",
  "protocol_version": "",
  "dataset_version": "",
  "baseline_condition_version": "",
  "yt6_condition_version": "",
  "provider": "",
  "product": "",
  "model": "",
  "model_version": null,
  "environment": "",
  "created_by": "",
  "created_at": "",
  "completed_at": null
}
Run
{
  "run_id": "",
  "assessment_id": "",
  "task_id": "",
  "condition": "baseline | yt6",
  "repetition": 0,
  "status": "queued | running | complete | failed | contaminated",
  "input_sequence": [],
  "output_sequence": [],
  "timestamp_started": "",
  "timestamp_completed": null,
  "execution_time_seconds": null,
  "protocol_version": "",
  "dataset_version": "",
  "condition_version": "",
  "condition_hash": "",
  "technical_failure": false,
  "error_record": null,
  "retry_of": null,
  "raw_evidence_hash": "",
  "raw_evidence_path": ""
}
Review
{
  "review_id": "",
  "assessment_id": "",
  "run_id": "",
  "reviewer_id": "",
  "masked_output_label": "",
  "intention_preservation": null,
  "constraint_compliance": null,
  "action_clarity": null,
  "multi_turn_consistency": null,
  "clarity_score": null,
  "drift_event_count": null,
  "unsupported_assumption_count": null,
  "critical_failure": null,
  "notes": "",
  "submitted_at": ""
}
Deviation
{
  "deviation_id": "",
  "assessment_id": "",
  "run_id": "",
  "description": "",
  "reason": "",
  "impact": "",
  "authorised_by": "",
  "recorded_at": ""
}
10. Run Identifier Format
Every run must have a unique identifier:

YT6MVP-[TASK]-[CONDITION]-[REPETITION]-[DATE]-[SEQUENCE]
Example:

YT6MVP-AMB01-A-01-20261027-0001
Condition codes:

A = Baseline
B = YT6
Condition codes must be hidden from blinded reviewers.

11. Core Calculation
For each reviewed output:

Dimension total =
intention preservation
+ constraint compliance
+ action clarity
+ multi-turn consistency
Maximum dimension total:

16
Clarity score:

dimension total ÷ 16 × 100
Paired difference:

YT6 clarity score − Baseline clarity score
A positive difference favours YT6 for that assessed run.

A positive result on one task must not be reported as proof of general performance.

12. Evidence Integrity Requirements
The MVP must:

preserve raw inputs;
preserve raw outputs;
preserve failed runs;
preserve retry relationships;
preserve original reviewer scores;
record condition versions;
record dataset and protocol versions;
record timestamps;
generate evidence hashes;
show incomplete evidence visibly;
prevent silent replacement of evidence.
The MVP must not:

clean up poor outputs;
hide failed YT6 runs;
regenerate until YT6 wins;
alter the task between conditions;
expose expected answers to the tested system;
expose condition labels to blinded reviewers;
allow YT6 to score itself as the sole evaluator.
13. Security and Privacy Minimum
For the first MVP:

use authorised accounts only;
encrypt traffic in transit;
restrict access to stored assessments;
avoid collecting unnecessary personal data;
avoid using confidential customer data in early tests;
record who created, executed and reviewed an assessment;
provide a method to delete test assessments;
keep credentials outside source code;
separate application secrets from repositories.
The first customer pilot must use synthetic or explicitly authorised data.

14. MVP Technical Architecture
The precise technology stack remains an implementation decision.

The minimum architecture requires:

Web application
      ↓
Assessment service
      ↓
Run orchestrator
   ↙             ↘
Baseline        YT6
runner          runner
   ↘             ↙
Evidence and telemetry store
      ↓
Blind-review service
      ↓
Report generator
Required Logical Components
User interface
Authentication
Fixed-task repository
Condition-package repository
Run orchestrator
Model connector
Raw-evidence store
Scoring service
Report generator
Audit log
The first implementation may support only one model connector.

15. Manual Versus Automated Functions
To reduce build complexity, the first MVP may use manual operations where they do not damage evidence integrity.

May Initially Be Manual
selecting the tested model;
transferring prompts where direct API integration is unavailable;
entering model/version information;
human reviewer scoring;
approving the final export;
recording an external run URL or evidence file.
Must Be System-Controlled
task version selection;
condition-version recording;
run ID creation;
evidence preservation;
score calculation;
reviewer-condition masking;
export generation;
audit history.
Manual transfer must be disclosed in the assessment report.

16. MVP Acceptance Criteria
The MVP is accepted only when an authorised user can complete this sequence without founder-only intervention:

sign in;
create an assessment;
select a fixed task;
configure the tested AI system;
complete a Baseline run;
complete a YT6 run;
capture both raw outputs;
mask the condition labels;
submit reviewer scores;
calculate the comparison;
view the raw evidence;
export the assessment report.
Additional acceptance requirements:

failed runs remain visible;
task text is identical across conditions;
condition versions are recorded;
exported scores match displayed scores;
evidence hashes are generated;
missing provenance is visibly flagged;
no output is silently edited.
17. Non-Goals for MVP v1
The first MVP will not include:

general-purpose AI chat;
every YT6 architectural component;
the complete public display of Base44;
automatic claims of zero drift;
automatic claims of reproducibility;
automatic replacement of human reviewers;
Microsoft Copilot integration;
Microsoft Marketplace publication;
enterprise multi-tenancy;
advanced billing;
customer-specific model training;
autonomous remediation of customer agents;
full compliance certification;
unlimited model connectors;
acquisition or licensing workflows.
These may be considered only after evidence and user demand justify them.

18. Initial Commercial Offer
Offer Name
YT6 AI Interaction Stability Assessment

Customer Supplies
a bounded AI workflow;
a set of non-confidential test scenarios;
applicable constraints;
the desired assessment question.
YT6 Supplies
controlled Baseline and YT6 evaluation;
matched task execution;
raw evidence capture;
clarity and drift scoring;
observed-failure analysis;
evidence report;
limitations statement.
Initial Revenue Path
The first commercial version may be sold as a bounded assessment service rather than a self-service software subscription.

The purpose is to test whether customers value the assessment before building a larger platform.

19. MVP Success Measures
Product Feasibility
assessments complete end to end;
evidence is not lost;
scores calculate correctly;
reports export successfully;
another operator can use the system.
User Value
reviewer can understand the comparison;
reviewer can identify the evidence supporting a score;
customer reports the output is useful;
customer requests another assessment or supplies a real workflow.
Commercial Signal
At least one of the following:

paid assessment;
signed pilot;
written customer commitment;
repeat assessment request;
approved test with an external organisation.
Evidence Signal
controlled pilot completed;
raw evidence complete;
scoring completed;
independent reproduction attempted.
20. MVP Failure Conditions
The MVP should be reconsidered if:

users cannot understand the report;
reviewers cannot score consistently;
the condition package cannot be reproduced;
evidence is incomplete;
the tested task differs between conditions;
YT6 results cannot be separated from operator coaching;
no target user finds the assessment valuable;
customers care about a different problem than the one being measured.
Failure must lead to learning, not concealment.

21. Delivery Phases
Phase 1 — Internal Prototype
Build:

fixed task selection;
run record;
raw-output storage;
manual Baseline/YT6 execution;
basic comparison;
manual reviewer scoring;
report export.
Exit condition:

One complete internal assessment can be reproduced.

Phase 2 — Usable MVP
Add:

authorised sign-in;
reliable storage;
reviewer masking;
audit history;
evidence hashes;
assessment export;
basic customer-ready interface.
Exit condition:

A non-founder can complete the assessment with written instructions.

Phase 3 — External Pilot
Add only what the first pilot requires:

customer/project separation;
data handling notice;
pilot agreement inputs;
customer-specific task import;
results delivery workflow.
Exit condition:

One external organisation completes or commissions an assessment.

Phase 4 — Commercial Validation
Add only after demonstrated demand:

payment route;
repeat-assessment workflow;
customer account improvements;
additional connectors;
Marketplace preparation.
22. Build Priority
Use this order:

P0 — Evidence integrity
P0 — Fixed task and condition control
P0 — Complete Baseline/YT6 workflow
P0 — Raw-output preservation
P0 — Blind scoring
P0 — Evidence report

P1 — Authentication
P1 — Audit history
P1 — Better user experience
P1 — Customer task import

P2 — Additional models
P2 — Automated scoring assistance
P2 — Billing
P2 — Marketplace packaging

P3 — Broader YT6 architecture visualisation
P3 — Enterprise administration
P3 — Advanced analytics
No P2 or P3 feature should delay the P0 workflow.

23. Readiness Checklist
The MVP build may begin when:

product scope accepted;
v2 test protocol available;
fixed dataset available;
Baseline condition available;
YT6 condition available;
YT6 condition package sufficiently defined for prototype use;
scoring rubric available;
telemetry schema available;
raw-evidence format available;
one target user identified;
implementation owner identified;
repository location selected.
The formal benchmark must remain marked NOT STARTED until its separate pre-run readiness gate is passed.

24. MVP Definition of Done
YT6 has reached MVP when:

A real authorised user can run or record the same fixed AI task under Baseline and YT6 conditions, preserve both evidence chains, submit blinded scores, view the measured comparison, and export a trustworthy assessment without requiring undocumented founder intervention.

The MVP is not complete merely because:

a demonstration script runs;
a user interface exists;
one curated example looks successful;
YT6 reports that it passed;
architecture documents are available.
25. Product Evidence Statement
Permitted wording:

YT6 AI Interaction Stability Assessment is an early-stage product for conducting controlled baseline-versus-YT6 evaluations of multi-turn AI interactions.

Not permitted without evidence:

YT6 has proven that it eliminates drift.

YT6 improves Microsoft Copilot.

YT6 guarantees deterministic AI outputs.

26. Current Status
PRODUCT DEFINITION: COMPLETE FOR DRAFT
BUILD STATUS: NOT STARTED
MVP STATUS: WORKING TOWARDS MVP
CUSTOMER VALIDATION: NOT STARTED
COMMERCIAL VALIDATION: NOT STARTED
MICROSOFT COPILOT CLAIM: NOT ESTABLISHED
END OF YT6 MVP BUILD SPECIFICATION

