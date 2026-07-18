# Mission: Rust for Offshore Access Backends

## Why
You work on the backend team of a company that builds walk-to-work offshore access solutions —
motion-compensated gangways and access systems that keep a bridge steady between a moving vessel and
a fixed offshore structure so people and equipment can cross safely. The control and safety systems
themselves are their own discipline; your job is the surrounding **backend software**: services that
track assets and vessels, schedule and gate access windows, ingest telemetry, expose operational
status, and record an auditable event history, for operations running all over the world. This
course takes you from "new to Rust" to "can read, reason about, and write backend Rust for that kind
of service" — using another language you already know as the point of comparison.

## Success looks like
- Can open an unfamiliar Rust backend source file and correctly explain what it does without help.
- Can write a new Rust function from a failing test (TDD stub-filling) using enums, structs, traits,
  generics, `Result`/`?`, and shared state — without copying a filled-in example first.
- Can read and act on rust-analyzer diagnostics, clippy warnings, and compiler errors before
  reaching for a search engine.
- Can manage a sequence of edits with a modern VCS workflow: inspect status/log, describe changes,
  split/squash messy work, and recover from a mistake.

## Constraints
- Learning happens in short sessions that each end with a tangible win, not open-ended reading.
- You do the tooling/install/config work yourself. Setup is part of the practice — guidance gives
  exact snippets/commands with a one-line "why," not pre-applied edits.
- Teaching method: TDD stub-filling. Never a filled-in solution first — every exercise starts from a
  failing test and an incomplete scaffold, then review. Early scaffolds are a signature/body stub;
  later lessons fade the scaffold, sometimes to a one-sentence description, so designing the
  interface itself becomes practice too.

## Domain glossary (used consistently across every lesson)
These are synthetic teaching types, not real safety-system code. Every lesson draws its examples
from this vocabulary so the domain stays coherent as concepts build:

- **`AssetId`** — identifier for a deployed access system or gangway unit.
- **`VesselVisit`** — a vessel arriving at a site for a period, during which transfers may happen.
- **`TransferRequest`** — a request to move personnel or cargo across the gangway.
- **`AccessWindow`** — a time span during which transfers are permitted for a visit.
- **`CompensationState`** — reported state of the motion-compensation system (e.g. `Active`,
  `Standby`, `Faulted`) as seen by the backend, not the control loop itself.
- **`AccessOutcome`** — the result of evaluating a transfer request: `Ready`, `Blocked(reason)`, or
  `EscortRequired`.
- **`AccessEvent`** — an entry in the audit/event log (who/what/when/outcome).
- **`ControllerState`** — backend-side shared state aggregating status across handlers.
- **operating parameters** — a `HashMap` of tunable service settings, with per-site overrides.
- **crates** — a small workspace of `access-service`, `telemetry-core`, and `test-support`.

## Out of scope
- The real-time motion-compensation control loop, PLC/embedded code, and functional-safety
  certification — this course is about the surrounding backend services only, and all examples are
  simplified and synthetic.
- Deep dives into `unsafe` Rust, custom allocators, or advanced macro authoring.
- Debugging tooling (`nvim-dap`/`codelldb`) — deferred until the edit → compile → test loop is
  comfortable.
