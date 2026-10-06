# YT6 — Azure MCP Connector Plan

## 1. Purpose

This document defines how YT6 can be exposed as a **Model Context Protocol (MCP)** service so Azure Copilot and other MCP‑aware agents can call YT6 as a clarity benchmark.

Goal:  
Make YT6 available as a **remote clarity evaluation service** that accepts inputs, runs benchmark flows, and returns drift, stability, and reproducibility scores.

---

## 2. MCP Role for YT6

YT6 acts as:

- **Context provider:** supplies clarity evaluation context for AI agents.
- **Tool endpoint:** runs benchmark scenarios on demand.
- **Scoring service:** returns deterministic clarity metrics.

MCP clients (e.g., Copilot) call YT6 to:

- test multi‑turn reasoning
- detect drift
- confirm reproducibility
- evaluate clarity under pressure

---

## 3. High‑Level Connector Design

### 3.1 MCP Server

- Implement a lightweight MCP server (Node.js, Python, or .NET).
- Expose YT6 benchmark functions as MCP tools:
  - `yt6_run_benchmark`
  - `yt6_get_scores`
  - `yt6_get_logs`

### 3.2 YT6 Backend

- Backend reads:
  - `datasets/`
  - `scoring/`
  - `reproduction/`
  - `logs/`
- Runs benchmark flows based on MCP requests.
- Returns:
  - drift score
  - stability score
  - variance score
  - reproducibility flag

---

## 4. Example MCP Tool Definitions

### 4.1 Tool: yt6_run_benchmark

**Purpose:**  
Run the full YT6 benchmark against a target AI system.

**Inputs:**
- `system_id` (string)
- `run_id` (string)

**Outputs:**
- `status` (string)
- `run_id` (string)

### 4.2 Tool: yt6_get_scores

**Purpose:**  
Retrieve clarity scores for a completed benchmark run.

**Inputs:**
- `run_id` (string)

**Outputs:**
- `drift_score` (number)
- `stability_score` (number)
- `variance_score` (number)
- `reproducibility` (boolean)

### 4.3 Tool: yt6_get_logs

**Purpose:**  
Return raw logs for audit and analysis.

**Inputs:**
- `run_id` (string)

**Outputs:**
- `logs_url` or `logs_blob` (string)

---

## 5. Azure Integration Path

1. **Host MCP server** on Azure (App Service, Container Apps, or Functions).
2. **Connect MCP endpoint** to Azure Copilot Studio as a custom tool.
3. **Configure Copilot agents** to:
   - call `yt6_run_benchmark` after scenario runs
   - call `yt6_get_scores` to evaluate clarity
   - optionally call `yt6_get_logs` for deeper analysis

---

## 6. Next Steps

- Define concrete MCP schema for YT6 tools.
- Implement minimal MCP server that:
  - reads YT6 configs
  - runs benchmark flows
  - returns scores and logs
- Document usage in `docs/integration-examples.md`.

This plan makes YT6 **MCP‑ready**, enabling Azure Copilot and other MCP‑aware systems to use YT6 as a clarity benchmark service.
