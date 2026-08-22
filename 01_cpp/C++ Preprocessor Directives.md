---
type: concept
domain: cpp
tags:
  - note/concept
aliases:
  - Preprocessor Directives
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

# C++ Preprocessor Directives

## Why it matters

Preprocessor directives appear in C++ source files but are commands to the preprocessor. Recognising them prevents confusion with ordinary C++ statements.

## In simple terms

A preprocessor directive starts with `#` and tells the preprocessor to perform an action before the later build stages.

## How it works

The introductory material groups these directive forms:

- File inclusion: `#include`
- Conditional forms: `#if`, `#elif`, `#else`, `#endif`, `#ifdef`, `#ifndef`
- Definition forms: `#define`, `#undef`
- Other directives: `#line`, `#error`, `#pragma`

## Concrete example

```cpp
#include <iostream>
#include "myfile.h"
```

The first form names a standard header. The second shows the course's local-header form with plain quotation marks.

## Common failure modes

- Forgetting the leading `#`.
- Using typographic quotation marks instead of plain `"` characters in source code.
- Listing a conditional opening directive without its corresponding closing form.

## Active recall

- What identifies a line as a preprocessor directive?
- Group the listed directives by inclusion, conditional use, definitions, and other commands.
- Reconstruct the two `#include` forms shown in the example.

## Interview check

- What is a preprocessor directive, and how can you recognise one?

## Intuitive example

Preprocessor directives are preparation instructions attached to the source before the remaining translation work proceeds.

## Connections and exercises

- Parent structure: [[C++ Program Structure]]
- Source context: [Workspace1 Project1](workspaces/Workspace1/Project1/main.cpp)

## Sources

- Introductory course material captured in the original version of [[01_cpp/01_01_Introduction|C++ Introduction]].
- Committed beginner C++ source files under `01_cpp/workspaces/`.
