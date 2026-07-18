# AGENTS.md

## What this repo is

A self-paced course for **learning Rust**, aimed at an engineer who already knows another language
(Python, TypeScript, Java) and is new to Rust. The framing domain is **backend services for
walk-to-work offshore access systems** — motion-compensated gangways that bridge a moving vessel to
a fixed offshore structure. The course is *not* the control/safety system; it's the surrounding
backend software (asset/vessel tracking, access-window scheduling, telemetry ingest, operational
status, audit events).

The domain types are **synthetic teaching constructs**, not real production or safety-certified code.

Start with [`README.md`](./README.md) for the lesson index, [`MISSION.md`](./MISSION.md) for the
rationale and domain glossary, and [`RESOURCES.md`](./RESOURCES.md) for the annotated source list.

## Layout

- `lessons/` — numbered, self-contained HTML lessons (`0001-…` … `0018-…`), worked through in order.
- `reference/` — HTML reference pages (concept map, tooling cheatsheet, cross-maps to Comprehensive
  Rust and Rustlings, vim keybinds).
- `assets/course.css` — shared stylesheet linked by every lesson/reference page.
- `scripts/validate_course.py` — structural validator (numbering, dead links, required callouts,
  `course.css` linkage).
- `MISSION.md`, `RESOURCES.md`, `README.md` — course docs described above.

- `rust-practice/` — the learner's own practice crate, where every lesson's exercises are worked.
  The course calls this a throwaway crate and refers to it by that name; here it lives **inside the
  repo** by choice. Its `target/` is gitignored. This is the one place solution code belongs; the
  rest of the repo is course material.

Editor: **VS Code** with the `rust-analyzer` extension (the lessons are written for nvim/treesitter,
but any editor with rust-analyzer works — translate the editor-specific steps accordingly).

## Teaching method (important context when helping)

**TDD stub-filling — never hand over a filled-in solution first.** Every exercise starts from a
failing test plus an incomplete scaffold (a signature or `todo!()` body stub). Later lessons
deliberately fade the scaffold, sometimes down to a one-sentence description, so designing the
signature/trait is itself the practice. When assisting with a lesson, prefer hints, diagnostics
explanations, and pointing at the relevant concept over writing the answer.

Setup (toolchain, editor/LSP, creating the practice crate) is done by the learner by hand — guidance
is exact commands with a one-line "why," not pre-applied edits. Version control in the workflow
lessons uses **jj (Jujutsu)**, not plain git.

## Working on the course itself

After editing any lesson or reference page, run the structural validator before considering it done:

```
uv run python scripts/validate_course.py
```
