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
prerequisites: []
related: ["[[Bash Script Input and Arguments]]", "[[Bash Arrays]]"]
contrasts: []
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Variables and Quoting

## Why it matters

Variables let a script reuse values. Quoting stops spaces and wildcard
characters in a value from being interpreted as separate shell syntax.

## In simple terms

Assign with no spaces around `=`. Expand a variable with `$name` or
`${name}`. Double quotes expand variables; single quotes keep text literal.

## How it works

```bash
name='Dave'
count=12
greeting="Hello, $name"

printf '%s has %s tasks\n' "$name" "$count"
printf '%s\n' "$greeting"
```

Quote variable expansions by default: `"$name"`. The quotes are removed by
Bash after they have protected the value.

## Concrete example

The [script.sh](bash_scripting/exercises/script.sh) file assigns `name` and
`number`, then expands `name`. The [greet](bash_scripting/exercises/greet)
file is a smaller version that also expands a variable.

## Common failure modes

- `name = Dave` is not an assignment; the spaces make Bash treat it as a command.
- `echo $name` can split a value containing spaces; prefer `printf '%s\n' "$name"`.
- Single quotes do not expand variables: `'Hello, $name'` prints `$name` literally.

## Active recall

- What is wrong with `name = Dave`?
- When would you use single quotes instead of double quotes?
- Why is `"$name"` safer than `$name` in a command?

## Interview check

Explain the difference between assigning a variable and expanding a variable
in Bash.

## Intuitive example

A variable is a labelled box. Assignment puts a value in the box; expansion
opens the box and uses its current value.

## Connections and exercises

- [[Bash Script Input and Arguments]] stores values received from users.
- Practise with [script.sh](bash_scripting/exercises/script.sh) and
  [greet](bash_scripting/exercises/greet).

> [!info] AI-added — verified
> The quoting guidance and example were added to make the rough variable notes
> safer to reuse. They were checked against the
> [GNU Bash Shell Parameters](https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameters)
> and [Quoting](https://www.gnu.org/software/bash/manual/bash.html#Quoting) sections.

## Sources

- [GNU Bash Shell Parameters](https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameters)
- [GNU Bash Quoting](https://www.gnu.org/software/bash/manual/bash.html#Quoting)
