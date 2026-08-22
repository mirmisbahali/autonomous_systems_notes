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
related: ["[[Bash Shell Commands and Exit Status]]"]
contrasts: []
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Redirection and Pipelines

## Why it matters

Redirection connects commands to files or supplied text. Pipelines connect one
command's output to another command's input.

## In simple terms

| Operator | Meaning |
| --- | --- |
| `>` | write output, replacing the file |
| `>>` | append output to the file |
| `<` | read a file as standard input |
| `<<` | here document: several lines become standard input |
| `<<<` | here string: one string becomes standard input |
| `\|` | pipe output into the next command |

## How it works

```bash
wc -w hello.txt
wc -w < hello.txt

wc -w <<< 'hello there wordcount!'

cat << EOF
I will
write some
text here
EOF

printf '%s\n' one two three | wc -l
```

The first two commands count the same file in different ways: once as a
filename argument and once through standard input.

## Concrete example

- [hello.txt](bash_scripting/exercises/hello.txt) is a small input file for
  redirection experiments.
- [file.txt](bash_scripting/exercises/file.txt) is larger scratch input for
  commands such as `wc`, `head`, or `grep`.

## Common failure modes

- `>` overwrites existing content; use `>>` when you mean append.
- A here-document's ending marker must match exactly and be on its own line.
- Quote paths containing spaces when redirecting: `wc -w < "$file"`.

## Active recall

- What is the difference between `wc -w hello.txt` and `wc -w < hello.txt`?
- When would you use `<<<` instead of `<<`?
- Which operator would append command output without deleting old content?

## Interview check

Explain how a pipeline differs from redirecting output to a file.

## Intuitive example

Redirection is changing where a tap pours water; a pipeline attaches the tap of
one command directly to the input bucket of another.

## Connections and exercises

- [[Bash Shell Commands and Exit Status]] uses a pipeline with `compgen -b`.
- Practise with [hello.txt](bash_scripting/exercises/hello.txt) and
  [file.txt](bash_scripting/exercises/file.txt).

> [!info] AI-added — verified
> The operator names, table, and pipeline example were added to organise the
> rough notes. They were checked against the
> [GNU Bash Redirections](https://www.gnu.org/software/bash/manual/bash.html#Redirections)
> and [Pipelines](https://www.gnu.org/software/bash/manual/bash.html#Pipelines) sections.

## Sources

- [GNU Bash Redirections](https://www.gnu.org/software/bash/manual/bash.html#Redirections)
- [GNU Bash Pipelines](https://www.gnu.org/software/bash/manual/bash.html#Pipelines)
