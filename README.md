# Rust for Offshore Access Backends

A self-paced Rust course for engineers who know another language (Python, TypeScript, Java) but
are new to Rust, aimed at writing backend services for a company that builds **walk-to-work**
offshore access systems — motion-compensated gangways and access platforms that let personnel and
cargo move safely between vessels and offshore structures (wind turbines, platforms, substations)
in moving seas, anywhere in the world.

Every concept is grounded in a small, synthetic backend domain (transfer requests, access windows,
telemetry, operational status, audit events, service health), and every coding exercise starts from
a failing test plus an incomplete scaffold — never a filled-in solution. Early lessons hand you the
function signature (or a `todo!()` body stub) and leave the logic to you; later lessons deliberately
fade that scaffolding, sometimes down to a one-sentence description, so you also practice designing
the signature or trait/interface itself.

> **Note:** The domain examples here are teaching material only. They are simplified, synthetic
> backend code and do not represent certified motion-control, safety, or vessel-access logic.

See [`MISSION.md`](./MISSION.md) for the rationale and the domain glossary every lesson uses, and
[`RESOURCES.md`](./RESOURCES.md) for the annotated source list this course draws from.

## How to use this

Each lesson is a single, self-contained HTML file — open it in a browser. They are numbered and
meant to be worked through in order. You do all the setup yourself (toolchain install, editor
config, creating the practice crate); the lessons give exact commands with a one-line "why," not
pre-applied edits.

Set up one throwaway practice crate once and reuse it across lessons. This course refers to it as
`rust-practice/` — put it wherever you keep scratch projects and read that name as a relative
placeholder for your own path.

## Reference

- [Rust concept map](./reference/0001-rust-backend-map.html) — every concept in this course, paired
  with where the equivalent shape shows up in a real backend service.
- [Tooling cheatsheet](./reference/0002-rust-tooling-cheatsheet.html) — cargo, rust-analyzer, an
  editor/LSP, and the version-control commands used in the workflow lessons.
- [Comprehensive Rust cross-map](./reference/0003-comprehensive-rust-map.html) — how [Google's
  Comprehensive Rust](https://google.github.io/comprehensive-rust/) lines up with each lesson here.
- [Vim keybind cheatsheet](./reference/0004-vim-keybind-cheatsheet.html) — text objects and motions
  that pay off when stub-filling Rust and reading dense source.
- [Rustlings cross-map](./reference/0005-rustlings-map.html) — how [Rustlings](https://rustlings.rust-lang.org/)
  exercise sets line up with each lesson, for extra reps.

## Lessons

| # | Lesson | Concept |
|---|---|---|
| 1 | [Toolchain Anatomy, Highlighting, & Your First Function](./lessons/0001-open-rust-with-feedback.html) | rustc/cargo/rustfmt/clippy, editor + treesitter, implicit return |
| 2 | [Live Diagnostics & A Signature You Choose](./lessons/0002-live-diagnostics-and-your-signature.html) | rust-analyzer + LSP, `if` as an expression |
| 3 | [Your First jj Change](./lessons/0003-your-first-jj-change.html) | jj basics: `st`/`log`/`describe`/`new` |
| 4 | [Enums That Carry Data](./lessons/0004-enums-that-carry-data.html) | enums, exhaustive `match` |
| 5 | [Structs That Group Data](./lessons/0005-structs-that-group-data.html) | structs, `impl` blocks, methods vs. associated functions |
| 6 | [Ownership & Borrowing](./lessons/0006-ownership-and-borrowing.html) | move semantics, `.clone()`, `&` |
| 7 | [Lifetimes — Naming How Long a Borrow Lasts](./lessons/0007-lifetimes-and-borrowed-data.html) | lifetime elision, explicit lifetime parameters |
| 8 | [Navigating History with jj](./lessons/0008-jj-navigate-history.html) | `jj edit`, automatic rebase |
| 9 | [Collections & Strings](./lessons/0009-collections-and-strings.html) | `Vec`, `String`/`&str`, `HashMap` |
| 10 | [Result, Option, and the `?` Operator](./lessons/0010-result-option-and-error-handling.html) | `Result`/`Option`, `?`, `anyhow` |
| 11 | [Traits You Design Yourself](./lessons/0011-traits-and-conversions.html) | traits, struct-shaped enum variants |
| 12 | [jj Squash & Split](./lessons/0012-jj-squash-and-split.html) | reshaping history |
| 13 | [Generics & Trait Bounds](./lessons/0013-generics-and-trait-bounds.html) | generic functions, trait bounds |
| 14 | [Iterators & Closures](./lessons/0014-iterators-and-closures.html) | iterator combinators, closures |
| 15 | [Conflicts & jj undo, For Real](./lessons/0015-jj-conflicts-and-undo.html) | conflicts as first-class state, `jj undo` |
| 16 | [Shared State & Arc](./lessons/0016-shared-state-and-arc.html) | `Arc`, shared ownership |
| 17 | [Modules & Visibility](./lessons/0017-modules-and-visibility.html) | `mod`, `pub`/`pub use`, refactoring one crate into files |
| 18 | [Cargo Workspaces](./lessons/0018-cargo-workspaces.html) | workspace `members`/`default-members`, `--workspace` vs. `-p` |

## A note on the code examples

The domain types in these lessons (`TransferRequest`, `AccessWindow`, `AccessOutcome`,
`ControllerState`, and so on) are synthetic teaching constructs, not excerpts from any real
production system. Read them as realistic-shaped Rust, then practice the concept in your own
`rust-practice/` crate.

## Maintaining this course

After editing any lesson or reference page, run the structural validator (numbering, dead links,
required callouts, `course.css` linkage) before packaging:

```
uv run python scripts/validate_course.py
```
