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
related: ["[[Bash Redirection and Pipelines]]", "[[Bash Script Input and Arguments]]"]
contrasts: []
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Shell Commands and Exit Status

## Why it matters

Knowing what Bash is running and whether it succeeded makes command-line
debugging much faster.

## In simple terms

- A **builtin** runs inside Bash, for example `echo`, `help`, and `read`.
- An external command is a separate program, often under `/bin` or `/usr/bin`.
- `type` shows how Bash resolves a command; `type -a` shows all matches.

## How it works

- `help COMMAND` documents a Bash builtin; `man COMMAND` opens a manual page.
- `compgen -b` lists Bash builtins.
- `$(...)` captures command output as text.
- `bash -n file.sh` checks syntax without running the script.
- `$?` contains the previous command's exit status: `0` normally means success.

## Concrete example

```bash
type -a kill
compgen -b | head
help read | less

system_info=$(uname -a)
printf '%s\n' "$system_info"

bash -n script.sh
printf 'syntax-check-status=%s\n' "$?"
```

The [builtin list](bash_scripting/exercises/builtin.txt) is a saved output of
`compgen -b`. The [shelltest.sh](bash_scripting/exercises/shelltest.sh) file is
the smallest script example; [script.sh](bash_scripting/exercises/script.sh)
shows a script with variables.

## Common failure modes

- Running another command before reading `$?` loses the status you wanted.
- `type -a kill` may show both the builtin and an external `/bin/kill`.
- `>` and `|` are shell syntax, not arguments passed directly to a command.

## Active recall

- How would you check whether `kill` is a builtin or external command?
- What does `bash -n` check, and what does it not check?
- Why must `$?` be read immediately after the command of interest?

## Interview check

What is the difference between a Bash builtin and an external command? Give one
reason the distinction matters when debugging.

## Intuitive example

`type -a` is like asking a receptionist which person will handle a request and
whether there are other people with the same name.

## Connections and exercises

- Uses [[Bash Redirection and Pipelines]] in `compgen -b | head`.
- Practise with [builtin.txt](bash_scripting/exercises/builtin.txt),
  [shelltest.sh](bash_scripting/exercises/shelltest.sh), and
  [script.sh](bash_scripting/exercises/script.sh).

> [!info] AI-added — verified
> The short explanations and recall examples were added to organise the rough
> notes. Syntax and command behaviour were checked against the
> [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html).

## Sources

- [Bash Bourne Shell Builtins](https://www.gnu.org/software/bash/manual/bash.html#Bourne-Shell-Builtins)
- [Bash Shell Parameters](https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameters)
