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
related: ["[[Bash Case Statements]]", "[[Bash Script Input and Arguments]]"]
contrasts: ["[[Bash Case Statements]]"]
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Conditional Tests

## Why it matters

Conditions let a script choose an action based on input or command results.

## In simple terms

`[ ... ]` and Bash's double-square-bracket form test a condition. A true test
has exit status `0`; a false test has a non-zero status. `if`, `elif`, `else`,
and `fi` select the branch to run.

## How it works

```bash
name=$1

if [ "$name" = 'ready' ]; then
    echo 'start'
elif [ -z "$name" ]; then
    echo 'a name is required'
else
    echo "waiting for $name"
fi
```

Spaces around `[` and `]` are required because `[` is a command name. In Bash,
Bash's double-square-bracket form is a safer conditional form with Bash-specific
features such as pattern matching.

## Concrete example

The [ifelifelse.sh](bash_scripting/exercises/ifelifelse.sh) exercise compares
the first argument after converting it to lowercase with `${1,,}`. The
[hello](bash_scripting/exercises/hello) exercise uses Bash's double-square-
bracket form with `-n $1` to check whether an argument is non-empty.

## Common failure modes

- Missing spaces or the closing `]` changes the command and causes a syntax error.
- Unquoted values can break a string comparison when the value is empty or has spaces.
- `=` inside `[ ... ]` is a string comparison; it is not numeric equality.

## Active recall

- Why is `[ hello = hello ]` a command rather than special punctuation?
- What does `-n` test? What does `-z` test?
- When would several `elif` branches become easier to express with `case`?

## Interview check

What is the practical difference between `[ ... ]` and Bash's double-square-
bracket form?

## Intuitive example

A conditional is a railway switch: the test decides which track the script
follows next.

## Connections and exercises

- [[Bash Case Statements]] is often clearer when matching several fixed values.
- [[Bash Script Input and Arguments]] supplies the values being tested.
- Practise with [ifelifelse.sh](bash_scripting/exercises/ifelifelse.sh) and
  [hello](bash_scripting/exercises/hello).

> [!info] AI-added — verified
> The distinction between test commands and Bash conditional syntax, plus the
> comparison details, were added and checked against the
> [GNU Bash Conditional Constructs](https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs) section.

## Sources

- [GNU Bash Conditional Constructs](https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs)
- [GNU Bash Conditional Expressions](https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions)
