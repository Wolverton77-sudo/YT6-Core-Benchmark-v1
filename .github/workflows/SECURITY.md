# Security Policy — YT6 Clarity Benchmark

YT6 is a clarity and reproducibility benchmark. While it does not execute code,
it interacts with AI systems and therefore requires a clear security posture.

## Supported Versions
YT6 supports all versions of the benchmark that include:
- architecture/
- reproduction/
- scoring/
- datasets/
- logs/

## Reporting Security Issues
If you discover a security concern related to:
- data integrity
- benchmark manipulation
- reproducibility interference
- drift injection
- clarity degradation

Please report it to the primary contact listed in the README.

## Security Principles
YT6 follows these principles:
- reproducibility cannot be compromised
- clarity outputs must remain unmodified
- drift detection must remain intact
- datasets must remain unchanged
- scoring rules must remain deterministic

## Threat Model
YT6 considers the following threats:
- intentional drift injection
- dataset tampering
- scoring manipulation
- log alteration
- benchmark bypassing

YT6 mitigates these through:
- strict reproduction rules
- immutable datasets
- deterministic scoring
- transparent logs
