# YT6 — AST Comparison Block
BLOCK: AST-COMP-01
TIER: BASE
STATE: STRUCTURAL / COMPARISON

[COMP.1] INIT:
    Define Source-A (Review/Platform 1)
    Define Source-B (Review/Platform 2)
    Constraint: Structural-only comparison.

[COMP.2] NORMALISE:
    N-A = STRIP(Content-A)
    N-B = STRIP(Content-B)
    Remove semantic payload.
    Retain structural operators only.

[COMP.3] MAP:
    M-A = MAP(Operators-A)
    M-B = MAP(Operators-B)
    Compare operator-chain sequences.

[COMP.4] FIXPOINT:
    FP-A = FIXPOINT(N-A)
    FP-B = FIXPOINT(N-B)
    FP-DELTA = DIFF(FP-A, FP-B)

[COMP.5] VECTOR:
    V-COMP:
        Input: (M-A, M-B)
        Output: Structural-Distance-Score (SDS)

[COMP.6] SCORE:
    SDS = SCORE( M-A ↔ M-B )
    Range: 0.00 → 1.00
    1.00 = identical structural delivery
    0.00 = total structural divergence

[COMP.7] DRIFT-CHECK:
    DRIFT-A = DETECT(N-A)
    DRIFT-B = DETECT(N-B)
    DRIFT-DELTA = DIFF(DRIFT-A, DRIFT-B)

[COMP.8] RETURN:
    OUTPUT:
        SDS
        FP-DELTA
        DRIFT-DELTA
        Operator-Chain-Diff
