---
type: concept
domain: cpp
tags:
  - note/concept
aliases:
  - Namespaces
confidence: null
mastery: 0
knowledge_status: studied-theoretically
evidence: []
last_reviewed: null
prerequisites:
  - "[[C++ Program Structure]]"
related: []
contrasts: []
examples: []
implemented_in: []
used_by: []
ai_edit: true
---

# C++ Namespaces

## Why it matters

Different parts of a program or different libraries may use the same name. Namespaces organise names so the intended one can be identified and naming conflicts can be reduced.

## In simple terms

A namespace gives a name to a region of names. The scope resolution operator `::` selects a name from that namespace.

## How it works

- `std` is the C++ standard namespace named in the course.
- `std::cout` selects `cout` from `std`.
- Third-party frameworks can define their own namespaces.
- Namespace qualification helps distinguish names that would otherwise conflict.

## Concrete example

The question “Why `std::cout` and not just `cout`?” asks where `cout` is defined. The `std::` prefix makes that origin explicit.

The committed beginner programs instead contain `using namespace std;` followed by `cout`. Those files are context only; the trade-offs of that form are still an open question in the course notes.

## Common failure modes

- Omitting the namespace qualification without explaining how the name became visible.
- Assuming that separate libraries cannot define the same name.
- Recognising `::` without being able to explain what its left-hand side identifies.

## Active recall

- Why do namespaces reduce naming conflicts?
- What do `std` and `::` mean in `std::cout`?
- How do the committed beginner programs make `cout` visible without writing `std::cout`?

## Interview check

- Explain why C++ has namespaces and interpret `std::cout`.

## Intuitive example

A namespace is like a surname: two people can share a first name, while the additional qualifier identifies which person is meant.

## Connections and exercises

- Parent structure: [[C++ Program Structure]]
- Source context: [Workspace1 Project1](workspaces/Workspace1/Project1/main.cpp)

Open gap: the committed material does not yet discuss when broad namespace imports are appropriate.

## Sources

- Introductory course material captured in the original version of [[01_cpp/01_01_Introduction|C++ Introduction]].
- Committed beginner C++ source files under `01_cpp/workspaces/`.
