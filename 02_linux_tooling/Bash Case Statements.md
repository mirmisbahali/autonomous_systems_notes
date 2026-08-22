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
prerequisites: ["[[Bash Conditional Tests]]"]
related: ["[[Bash Script Input and Arguments]]"]
contrasts: ["[[Bash Conditional Tests]]"]
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Case Statements

## Why it matters

`case` keeps several fixed choices readable without a long chain of `if` and
`elif` statements.

## In simple terms

`case` compares one value with patterns. Each matching branch ends with `;;`.
`*)` is the default branch; `|` separates alternative patterns.

## How it works

```bash
choice=${1,,}

case "$choice" in
    y|yes) echo 'continuing';;
    n|no)  echo 'stopping';;
    *)     echo 'enter y or n';;
esac
```

`${1,,}` converts the first argument to lowercase before matching.

## Concrete example

The [login.sh](bash_scripting/exercises/login.sh) exercise matches several
username patterns, including `herbert | administrator`, then falls back to `*`.

## Common failure modes

- Omitting `;;` lets execution continue into the next branch syntax.
- Omitting `*)` leaves unexpected input without a useful response.
- Patterns are not always literal strings; read them carefully before matching.

## Active recall

- What do `;;`, `*)`, and `esac` mean?
- How does `herbert | administrator)` differ from two separate branches?
- When is `case` clearer than `if`/`elif`?

## Interview check

Describe how you would add a default response for an unknown command in a
`case` statement.

## Intuitive example

`case` is a switchboard: route one incoming label to one of several named
operators, with a fallback operator for unknown labels.

## Connections and exercises

- [[Bash Conditional Tests]] is better for ranges or compound conditions.
- Practise with [login.sh](bash_scripting/exercises/login.sh).

> [!info] AI-added — verified
> The compact syntax explanation and example were added to make the course
> exercise easier to recall. They were checked against the
> [GNU Bash Conditional Constructs](https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs) section.

## Sources

- [GNU Bash Conditional Constructs](https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs)
