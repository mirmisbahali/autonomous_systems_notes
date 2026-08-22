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
prerequisites: ["[[Bash Variables and Quoting]]"]
related: ["[[Bash Conditional Tests]]", "[[Bash Loops]]"]
contrasts: []
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Script Input and Arguments

## Why it matters

Input makes one script reusable with different names, files, or options.

## In simple terms

- `$0` is the script name; `$1`, `$2`, and so on are positional arguments.
- `$#` is the number of arguments; `"$@"` expands to each argument separately.
- `read` collects input typed by the user.

## How it works

```bash
if test -n "$1"; then
    name=$1
else
    read -r -p 'Enter your name: ' name
fi

printf 'Hello, %s\n' "$name"
```

Run it with an argument, or omit the argument to use the prompt:

```bash
bash hello Misbah
bash hello
```

## Concrete example

- [posargu.sh](bash_scripting/exercises/posargu.sh) prints `$1` and `$2`.
- [interactiveshell.sh](bash_scripting/exercises/interactiveshell.sh) reads a
  first and last name interactively.
- [hello](bash_scripting/exercises/hello) uses `$1` when present and otherwise
  prompts with `read`.

## Common failure modes

- A missing argument becomes an empty value, so validate required input.
- Use `"$@"`, not `$@`, when passing all arguments through a loop or function.
- Quote user input when printing it or using it as a command argument.

## Active recall

- What is the difference between `$1`, `$#`, and `"$@"`?
- How can a script support both a command-line name and an interactive prompt?
- Why should `read -r` and quoted expansions be preferred?

## Interview check

How would you preserve an argument such as `"front left"` when forwarding all
script arguments to another command?

## Intuitive example

Positional arguments are the items handed to a function in order; `read` is the
same interaction happening later at the terminal.

## Connections and exercises

- [[Bash Variables and Quoting]] explains the values stored from input.
- [[Bash Loops]] uses `"$@"` to process every argument.
- Practise with [posargu.sh](bash_scripting/exercises/posargu.sh),
  [interactiveshell.sh](bash_scripting/exercises/interactiveshell.sh), and
  [hello](bash_scripting/exercises/hello).

> [!info] AI-added — verified
> The parameter summary and safer input example were added to connect the
> exercises. They were checked against the
> [GNU Bash Special Parameters](https://www.gnu.org/software/bash/manual/bash.html#Special-Parameters)
> and [Bash Builtins](https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins) sections.

## Sources

- [GNU Bash Special Parameters](https://www.gnu.org/software/bash/manual/bash.html#Special-Parameters)
- [GNU Bash Read Builtin](https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins)
