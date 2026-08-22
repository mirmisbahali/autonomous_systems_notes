---
type: concept
domain: cpp
tags:
  - note/concept
aliases: []
confidence: null
mastery: 0
knowledge_status: studied-theoretically
evidence: []
last_reviewed: null
prerequisites: []
related:
  - "[[01_cpp/01_01_Introduction|C++ Introduction]]"
contrasts: []
examples: []
implemented_in: []
used_by: []
ai_edit: true
---

# Modern C++ and the C++ Standard

## Why it matters

The selected C++ standard determines which language generation a project targets. It also gives developers a shared reference point when discussing language features and practices.

## In simple terms

The course calls C++ before C++11 *classical C++* and C++11 onward *modern C++*.

## How it works

The course timeline records:

- Early 1970s: Dennis Ritchie and the C programming language
- 1979: Bjarne Stroustrup began “C with Classes”
- 1983: the name changed to C++
- 1989: first commercial release
- 1998: C++98
- 2003: C++03
- 2011: C++11, with many new features
- 2014: C++14, with smaller changes
- 2017: C++17, with simplifications

The introductory material also associates modern C++ with best practices and the Core Guidelines.

## Concrete example

The committed Workspace1 CodeLite projects set `-std=c++17` in their Debug compiler options. This identifies C++17 as the intended language standard for those configurations.

## Common failure modes

- Calling every era of C++ “modern C++” without stating the boundary being used.
- Naming a standard version without checking which version the project configuration selects.
- Treating a version timeline as evidence that particular features have been learned or implemented.

## Active recall

- Where does this course place the boundary between classical and modern C++?
- How do C++11, C++14, and C++17 differ in the course summary?
- Where would you look to determine the standard selected by a project?

## Interview check

- What does “modern C++” mean in the context of this course?

## Intuitive example

Think of each standard as an edition of a shared engineering manual: naming the edition tells everyone which rules and tools are available.

## Connections and exercises

- Parent map: [[01_cpp/01_01_Introduction|C++ Introduction]]
- Configuration context: [Workspace1 Project1 configuration](workspaces/Workspace1/Project1/Project1.project)

The configuration link is context, not evidence of independent implementation.

## Sources

- Introductory course material captured in the original version of [[01_cpp/01_01_Introduction|C++ Introduction]].
- Committed CodeLite project configuration linked above.
