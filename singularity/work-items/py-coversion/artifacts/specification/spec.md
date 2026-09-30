<!-- singularity-flow:metadata
{
  "schemaVersion": 1,
  "workId": "py-coversion",
  "workType": "reference-driven-build",
  "phase": "specification",
  "generation": 1,
  "status": "in_progress",
  "generatedBy": {
    "name": "Ashok Raj",
    "email": "88361104+ashokraj2011@users.noreply.github.com",
    "login": "ashokraj2011",
    "githubLookup": "resolved"
  },
  "generatedAgent": "product-owner",
  "authorship": {
    "schemaVersion": 1,
    "producer": "governed-agent",
    "channel": "copilot-host",
    "actor": {
      "name": "Ashok Raj",
      "email": "88361104+ashokraj2011@users.noreply.github.com",
      "login": "ashokraj2011",
      "githubLookup": "resolved"
    },
    "governedAgentContext": {
      "agentId": "product-owner"
    },
    "kernelModel": {
      "invoked": false,
      "status": "exact",
      "invocationIds": []
    },
    "externalAiUse": {
      "value": "unknown",
      "status": "unavailable"
    },
    "changeOrigins": [
      "copilot"
    ],
    "source": {
      "kind": "in-place",
      "filename": "spec.md",
      "mediaType": "text/markdown",
      "sha256": "89ad329831b771ea605b2afaa3f4d20b47641c58834b9110959a7acc8d665c12",
      "bytes": 7135
    },
    "generation": 1,
    "publishedAt": "2026-09-30T03:42:11.366Z"
  },
  "sourceCommit": "6fc89b34524b86fbe86af21eb3639da26b906259",
  "generationCommit": null,
  "publicationCommit": null,
  "configSha256": "2ce4a29c11a99b96efaf8d9313e9df0685673df58c11fc5284006fc37fc20fe9",
  "sourceSha256": "fd664aa886ce5a4baa39a3f1cc21cfa4c95c900185ac2ff757eb467c5f3b02b3",
  "template": {
    "path": "singularity/work-items/py-coversion/config/wfa/blobs/sha256/27424a624b1dab57323fd7482ac62708bd42d11ba42e41c102f94e15182fe485",
    "sha256": "27424a624b1dab57323fd7482ac62708bd42d11ba42e41c102f94e15182fe485",
    "source": "workflow-snapshot",
    "sourcePath": "singularity/templates/spec-driven/spec.md"
  },
  "inputs": null,
  "designSources": {
    "sets": [],
    "approved": null
  },
  "remoteAgent": null,
  "clarification": {
    "generation": 1,
    "path": "singularity/work-items/py-coversion/context/clarifications-specification-gen1.json",
    "sha256": "379dca35d4d120d9298fcf7984147403f39434f39f2c165e355960daa040873e",
    "promptSha256": "77222a93cb1159e6cba911a12ae6a094557619be194c1d8c321bb438e6b894c8",
    "responses": 4,
    "markers": [],
    "recordedAt": "2026-09-30T03:37:56.326Z",
    "recordedBy": {
      "name": "Ashok Raj",
      "email": "88361104+ashokraj2011@users.noreply.github.com",
      "login": "ashokraj2011",
      "githubLookup": "resolved"
    }
  },
  "telemetry": [
    {
      "generation": 1,
      "path": "singularity/work-items/py-coversion/telemetry/specification-gen1.json",
      "sha256": "65cba64894310bddc4f298501fe6b0eabb2c7a536e3b98445519554614509316",
      "status": "pending",
      "models": [],
      "providerCost": null
    }
  ],
  "remoteOutputs": [],
  "usage": [
    {
      "status": "unavailable",
      "source": "copilot-otel-unavailable",
      "provider": null,
      "model": null,
      "requestedModel": null,
      "resolvedModel": null,
      "resolvedModelAssurance": "unavailable",
      "inputTokens": null,
      "outputTokens": null,
      "cachedInputTokens": null,
      "cacheWriteInputTokens": null,
      "totalTokens": null,
      "providerCost": null,
      "costStatus": "unavailable",
      "spans": null,
      "startedAt": "2026-09-30T03:42:11.366Z",
      "completedAt": "2026-09-30T03:42:11.366Z",
      "agent": "product-owner",
      "generation": 1
    }
  ],
  "sequenceOverrides": [],
  "approvals": [],
  "selfApproval": false,
  "conformanceTree": null
}
-->

<!-- singularity-flow:reference-repositories -->
## Read-only reference repositories

> This detached repository is read-only source data. Delivery changes belong in the current Story repository.

- **sf-field** — `.singularity-flow/reference-repositories/py-coversion/sf-field`
  - requested branch: `main`
  - pinned commit: `1b0c942f9b7d317199201533027bfd451d45a072`
<!-- /singularity-flow:reference-repositories -->

# Specification - py-coversion

## Agent brief

Convert the complete primary source project in the pinned `sf-field` reference repository from TypeScript/Node.js to Python 3.11+ packaged with a standard `pyproject.toml`. Preserve its externally observable capabilities, including the core runtime, CLI, adapters, presets, persistence, artifact handling, and testing support. Functional equivalence is required, while Python-appropriate interfaces may differ. Build tooling and generated files are excluded. Acceptance requires the converted project's full test suite and focused parity tests to pass.

## Actors

* **Conversion implementer:** changes delivery source and tests and preserves behavior.
* **Project maintainer:** reviews the converted package, tests, and declared dependencies.
* **Evaluator:** runs the documented test commands and parity checks; authority is limited to observable results.

## User scenarios

### S1 - Convert the complete reference project to Python

**Priority:** P1
**Actor:** Conversion implementer
**Context:** The pinned reference repository is a TypeScript monorepo with `packages/` containing core, CLI, HTTP, filesystem artifacts, local and memory presets, SQLite storage, and testing areas.

- **Given** the pinned reference source and documented behavior
  **When** all primary source roots are converted
  **Then** the delivery repository contains a Python 3.11+ package with equivalent observable capabilities and a standard `pyproject.toml`.

- **Given** Python interfaces may differ from the TypeScript interfaces
  **When** a capability is exercised through its supported Python interface
  **Then** its observable result, errors, and material side effects match the reference behavior.

### S2 - Verify functional parity through tests

**Priority:** P2
**Actor:** Evaluator
**Context:** The converted project and parity tests are present in the delivery repository.

- **Given** the project is installed from `pyproject.toml`
  **When** the full converted-project suite and focused parity tests run
  **Then** every test passes and the command exits successfully.

## Failure and empty states

* **Empty:** No converted source or tests means the Story is incomplete; a partial package is not accepted.
* **Failure:** Installation, import, build, or test failure means the conversion is not accepted, with evidence identifying the affected capability.
* **Partial:** Passing packages do not waive failures in other in-scope primary source roots.

## Permissions

The implementer and maintainer may modify and review the Story checkout. The evaluator may read, install, and execute the converted package and tests but may not redefine scope or waive a failing requirement. No end-user or production authorization model changes here.

## Boundary conditions

* The minimum supported runtime is Python 3.11.
* Every primary source root under `packages/` is in scope, including the seven listed package areas; build tooling and generated files are excluded.
* A standard `pyproject.toml` is required at the converted project's package boundary.
* Public names and call signatures may change for Python, but capabilities, outcomes, failure behavior, and material side effects may not be silently dropped.
* One failing required test means the Story is not accepted.

## Requirements

- Provide Python implementations for all primary source roots under the pinned reference repository's `packages/` directory. *(S1)* [py-coversion:REQ-001]
- Target Python 3.11 or newer and declare installable package metadata in a standard `pyproject.toml`. *(S1)* [py-coversion:REQ-002]
- Preserve the reference project's core runtime, CLI, HTTP, artifact, preset, persistence, and testing capabilities in the primary source roots. *(S1)* [py-coversion:REQ-003]
- Preserve representative successful results, failure behavior, and material side effects while allowing Python-appropriate interfaces. *(S1, S2)* [py-coversion:REQ-004]
- Exclude build tooling and generated files from required conversion targets. *(S1)* [py-coversion:REQ-005]
- Include focused parity tests covering representative behaviors from each major converted capability area. *(S2)* [py-coversion:REQ-006]
- Make the full converted-project suite and focused parity tests runnable from the packaged Python project, with failures producing a non-zero exit status. *(S2)* [py-coversion:REQ-007]
- Achieve a 100% pass rate for the required verification set, measured by its test report and exit status. *(S2)* [py-coversion:REQ-008]
- Declare runtime dependencies through `pyproject.toml` so a clean environment can reproduce installation. *(S1, S2)* [py-coversion:REQ-009]

Acceptance criteria:

- A clean checkout exposes an installable Python project with `pyproject.toml` and corresponding Python source for every in-scope primary source root. *(S1)* [py-coversion:AC-001]
- Working equivalents exist for the reference runtime, CLI, adapters, presets, persistence, artifact handling, and testing capabilities. *(S1)* [py-coversion:AC-002]
- Focused parity tests demonstrate matching representative outputs, errors, and material side effects. *(S2)* [py-coversion:AC-003]
- The full converted-project suite and parity tests pass with exit status zero. *(S2)* [py-coversion:AC-004]

## Non-functional requirements

* The required verification set has a 100% pass rate, measured by its test report and exit status. *(S2)* [py-coversion:REQ-010]
* A clean environment can install the package using only dependencies declared in `pyproject.toml`. *(S1, S2)* [py-coversion:REQ-011]

## Constitution articles

No project constitution articles were supplied in the approved Story inputs, so this specification binds to no additional article IDs.

## Assumptions

* The pinned `sf-field` repository at commit `1b0c942f9b7d317199201533027bfd451d45a072` is the sole reference source.
* Source behavior and tests are the authority for detailed parity; README and package layout identify capability areas.
* Python 3.11+ and a standard package installer are available to the evaluator.
* The recorded clarification answers are authoritative: complete primary-source conversion, functional equivalence with interface freedom, and full-suite plus parity-test acceptance.

## Out of scope

* Converting TypeScript/Node.js build tooling, lockfiles, generated `dist` output, or other generated files into Python.
* Preserving TypeScript or Node.js public interfaces when a Python interface is needed for equivalent behavior.
* Adding capabilities, changing business behavior, or redesigning the reference project.
* Deploying the converted project, changing external infrastructure, or establishing a production operations model.
