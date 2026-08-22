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
related: ["[[Bash Loops]]"]
contrasts: []
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Arrays

## Why it matters

An array stores several related values under one variable name.

## In simple terms

Bash arrays are zero-indexed: the first element is index `0`. Use `[@]` to
expand all elements.

## How it works

```bash
MY_FIRST_LIST=(one two three four five)

printf '%s\n' "${MY_FIRST_LIST[0]}"   # one
printf '%s\n' "${MY_FIRST_LIST[2]}"   # three
printf '%s\n' "${MY_FIRST_LIST[@]}"  # all elements
```

An unindexed expansion such as `$MY_FIRST_LIST` refers to the first element.
For safe iteration, use `"${MY_FIRST_LIST[@]}"` inside a loop.

## Concrete example

The rough note created `MY_FIRST_LIST` with five values and listed its indexes.
There is currently no exercise file that demonstrates arrays, so this small
example is intentionally self-contained.

## Common failure modes

- Forgetting that indexes start at `0` selects the wrong element.
- Unquoted `${MY_FIRST_LIST[@]}` can split elements containing spaces.
- `[@]` and `[*]` behave differently when quoted; use quoted `[@]` for separate
  elements.

## Active recall

- What index selects the first array element?
- What is the difference between `${array[0]}` and `"${array[@]}"`?
- How would you iterate over each array element safely?

## Interview check

Why should an array expansion usually be written as `"${array[@]}"` inside a
loop?

## Intuitive example

An array is a row of labelled lockers: the variable names the row and the
index identifies one locker.

## Connections and exercises

- [[Bash Loops]] can process each array element.
- No matching exercise is present yet; the example above fills the gap in the
  rough note.

> [!info] AI-added — verified
> The array expansion and quoting details were added because the rough note had
> no reference exercise. They were checked against the
> [GNU Bash Arrays](https://www.gnu.org/software/bash/manual/bash.html#Arrays) section.

## Sources

- [GNU Bash Arrays](https://www.gnu.org/software/bash/manual/bash.html#Arrays)
