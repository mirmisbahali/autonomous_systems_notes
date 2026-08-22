---
type: moc
domain: linux-tooling
tags:
  - note/moc
  - topic/bash
aliases: []
prerequisites: []
related: []
ai_edit: true
---

# Bash Scripting

## Purpose

Compact recall map for the Bash scripting course studied on 2026-08-22. The
course examples are kept in `bash_scripting/exercises/` and linked below.

## Source and context

- Primary source: [Bash Scripting Tutorial for Beginners](https://youtu.be/tK9Oc6AEnR4?si=lvl88c6ogAtuBDCX).
- Format: guided, hands-on tutorial exercises.
- Learning status: studied theoretically and practised with course examples;
  independent implementation and debugging have not been assessed.

## Prerequisites

- Be comfortable running Linux commands and reading a file from the terminal.

## Concept map

- Shell tools and status → [[Bash Shell Commands and Exit Status]]
- Variables → [[Bash Variables and Quoting]]
- Script input → [[Bash Script Input and Arguments]]
- Conditions → [[Bash Conditional Tests]] → [[Bash Case Statements]]
- Repetition and reuse → [[Bash Loops]] → [[Bash Functions]]
- Collections → [[Bash Arrays]]
- Data flow → [[Bash Redirection and Pipelines]]

## Suggested learning path

1. [[Bash Shell Commands and Exit Status]]
2. [[Bash Variables and Quoting]]
3. [[Bash Script Input and Arguments]]
4. [[Bash Conditional Tests]] and [[Bash Case Statements]]
5. [[Bash Loops]] and [[Bash Functions]]
6. [[Bash Arrays]] and [[Bash Redirection and Pipelines]]

## Projects and exercises

The following are course practice files, not independent evidence of mastery:

- Script basics: [shelltest.sh](bash_scripting/exercises/shelltest.sh),
  [script.sh](bash_scripting/exercises/script.sh), [greet](bash_scripting/exercises/greet).
- Builtins and command discovery: [builtin.txt](bash_scripting/exercises/builtin.txt).
- Variables and interactive input: [interactiveshell.sh](bash_scripting/exercises/interactiveshell.sh).
- Positional arguments and fallback input: [posargu.sh](bash_scripting/exercises/posargu.sh),
  [hello](bash_scripting/exercises/hello).
- Conditional logic: [ifelifelse.sh](bash_scripting/exercises/ifelifelse.sh).
- Multiple fixed choices: [login.sh](bash_scripting/exercises/login.sh).
- Loops and functions: [loop](bash_scripting/exercises/loop),
  [greeter](bash_scripting/exercises/greeter).
- Redirection sample data: [hello.txt](bash_scripting/exercises/hello.txt),
  [file.txt](bash_scripting/exercises/file.txt).

## Open gaps

- No test harness or independent debugging record is present for these
  exercises. The files are useful examples, but they do not by themselves
  justify a practical mastery level above 0.
- Arrays are explained here because they were in the rough notes, but no
  exercise currently demonstrates them.

## Sources

- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
