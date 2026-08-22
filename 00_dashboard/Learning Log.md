# Learning Log

This log records successful `$update-notes` update and active-recall runs. An entry may report a test as passing only when the command was actually run and its result was observed.

## Entries

### 2026-08-22 — Bash scripting notes update

- Inspected commit range: `fb82cd88bdb94ac3cb5220499fdb51bb631ac2e0..4eab99b448d3d4086c0682c6b5a0eda49a987c5a`.
  The scanner found no committed candidates; the user explicitly requested
  work on the currently uncommitted Bash note and exercises, so those files
  were used as the source material.
- Concepts created or changed: converted [[02_linux_tooling/Bash Scripting|Bash Scripting]]
  into a MOC; created [[02_linux_tooling/Bash Shell Commands and Exit Status|Bash Shell Commands and Exit Status]],
  [[02_linux_tooling/Bash Variables and Quoting|Bash Variables and Quoting]],
  [[02_linux_tooling/Bash Script Input and Arguments|Bash Script Input and Arguments]],
  [[02_linux_tooling/Bash Conditional Tests|Bash Conditional Tests]],
  [[02_linux_tooling/Bash Case Statements|Bash Case Statements]],
  [[02_linux_tooling/Bash Loops|Bash Loops]], [[02_linux_tooling/Bash Functions|Bash Functions]],
  [[02_linux_tooling/Bash Arrays|Bash Arrays]], and
  [[02_linux_tooling/Bash Redirection and Pipelines|Bash Redirection and Pipelines]].
- Splits, merges, and redirects: split the broad running note into eight atomic
  concept notes and retained the original path as the MOC. No merges or redirects.
- Source coverage: retained the course source/context and learning status;
  covered command discovery, builtins, manuals, command substitution, syntax
  checks, exit status, variables, quoting, positional arguments, `read`, test
  operators, `case`, loops, functions, arrays, redirection, here documents,
  here strings, and pipelines. All 13 exercise/data files were linked to a
  relevant concept or the MOC. The arrays gap is explicit because no exercise
  demonstrates it.
- Context inspected: all files under
  `02_linux_tooling/bash_scripting/exercises/`, including the two text inputs
  and the saved builtin list. No build or test harness exists in this folder.
- AI additions and sources: concise explanations, terminology, examples for
  arrays and other concepts, failure modes, intuitive examples, and recall or
  interview prompts. Bash details were checked against the
  [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html).
  No unresolved AI additions remain.
- Protected or conflicting paths skipped: exercise files were read only and
  not rewritten. The scanner-ignored uncommitted Bash inputs and unrelated
  `.obsidian/workspace.json` change were not treated as candidates.
- Verification: `bash -n` was run on every exercise with a Bash shebang and
  returned 0. Smoke checks ran `shelltest.sh`, `script.sh`, `greet`,
  `posargu.sh`, `loop`, `greeter`, all `ifelifelse.sh` and `login.sh` branches,
  `hello`, `interactiveshell.sh` with piped input, and the three word-count
  examples; each command group returned 0. `git diff --check` passed.
  `python3 .agents/skills/update-notes/scripts/audit_notes.py --root . --dashboard
  "00_dashboard/Knowledge Dashboard.md"` passed with 17 managed notes, 15
  concepts, 0 errors, 0 warnings, 0 orphans, and 0 unresolved AI additions.
  No exercise test suite was run and no exercise is claimed to pass.

### 2026-08-17 — C++ introduction update

- Inspected commit range: `8677b60bbb55e80ec103b747fa9f5bd15bbe7e76..fb82cd88bdb94ac3cb5220499fdb51bb631ac2e0`.
- Concepts created or changed: converted [[01_cpp/01_01_Introduction|C++ Introduction]] into a MOC; created [[Modern C++ and the C++ Standard]], [[C++ Build Process]], [[C++ Development Environments]], [[C++ Program Structure]], [[C++ Preprocessor Directives]], and [[C++ Namespaces]].
- Splits, merges, and redirects: split the broad introductory running note into six atomic concepts; retained its original path as the MOC. No merges or redirects.
- Source coverage: mapped the standards timeline, modern/classical distinction, build pipeline, testing and debugging, IDE and command-line workflows, curriculum and challenge outlines, program components, directives, and namespaces. Curriculum topics without substantive explanation remain explicit open gaps.
- Context inspected: `.gitignore`; the committed C++ build-process image; four beginner `main.cpp` files; four CodeLite project files; and two CodeLite workspace files.
- AI additions and sources: no external factual or curricular material added; explanations, examples, failure modes, and recall prompts were constrained to the committed note and context files.
- Protected or conflicting paths skipped: all committed files under `01_cpp/workspaces/` were treated as protected context and were not edited. No blocking conflicts. Scanner-ignored skill, template, dashboard, state, and Obsidian paths were not treated as candidates.
- Verification: source-coverage checklist completed; `python3 .agents/skills/update-notes/scripts/audit_notes.py --root . --dashboard "00_dashboard/Knowledge Dashboard.md"` passed with 7 managed notes, 6 concepts, 0 errors, 0 warnings, 0 orphans, and 0 unresolved AI additions. `git diff --check` passed. No exercise tests were run, and no code is claimed to pass.
