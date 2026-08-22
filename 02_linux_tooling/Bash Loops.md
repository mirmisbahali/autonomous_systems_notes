---
type: concept
domain: linux-tooling
tags:
  - note/concept
  - topic/bash
aliases: []
confidence: null
mastery: 0
knowledge_status: studied-theoretically
evidence: []
last_reviewed: null
prerequisites: ["[[Bash Script Input and Arguments]]"]
related: ["[[Bash Functions]]", "[[Bash Arrays]]"]
contrasts: []
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Loops

## Why it matters

Loops apply the same operation to many arguments, files, or other values.

## In simple terms

A `for` loop takes one item at a time from a list and runs its body.

## How it works

```bash
for item in "$@"; do
    printf 'item=%s\n' "$item"
done
```

`do` starts the repeated body and `done` ends it. `"$@"` preserves each
argument as a separate item, even when it contains spaces.

## Concrete example

- [loop](bash_scripting/exercises/loop) prints each command-line argument.
- [greeter](bash_scripting/exercises/greeter) loops over names and calls a
  function for each one.

## Common failure modes

- Using `$@` without quotes can split one argument into several loop items.
- Forgetting `done` causes a syntax error.
- A file glob such as `*.txt` can remain literal when no file matches it.

## Active recall

- What does `for item in "$@"` iterate over?
- Why are `do` and `done` needed?
- How does the loop in `greeter` use a function?

## Interview check

How would you write a loop that safely forwards every argument to a function?

## Intuitive example

A loop is a conveyor belt: each item arrives at the same work station, then the
next item takes its place.

## Connections and exercises

- [[Bash Functions]] provides reusable work for a loop body.
- [[Bash Arrays]] provides another kind of list to iterate over.
- Practise with [loop](bash_scripting/exercises/loop) and
  [greeter](bash_scripting/exercises/greeter).

> [!info] AI-added — verified
> The explanation of quoted positional parameters and loop structure was added
> to connect the two exercises. It was checked against the
> [GNU Bash Shell Expansions](https://www.gnu.org/software/bash/manual/bash.html#Shell-Expansions) section.

## Sources

- [GNU Bash Shell Expansions](https://www.gnu.org/software/bash/manual/bash.html#Shell-Expansions)
- [GNU Bash Looping Constructs](https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs)
