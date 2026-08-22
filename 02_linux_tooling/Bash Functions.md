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
related: ["[[Bash Loops]]", "[[Bash Script Input and Arguments]]"]
contrasts: []
examples: []
implemented_in: []
used_by: ["[[Bash Scripting]]"]
ai_edit: true
---

# Bash Functions

## Why it matters

Functions give a repeated operation a name, making scripts shorter and easier
to change.

## In simple terms

Define a function once, then call it by name. Function arguments are available
as `$1`, `$2`, and so on inside the function.

## How it works

```bash
greet() {
    local name=$1
    printf 'Hello, %s\n' "$name"
}

greet 'Misbah'
```

`local` keeps `name` scoped to the function instead of changing a global
variable.

## Concrete example

The [greeter](bash_scripting/exercises/greeter) exercise defines `greet`, then
calls it once for every name in `"$@"`.

## Common failure modes

- Defining a function does not run it; it must be called.
- Calling it without the required argument leaves `$1` empty.
- Omitting `local` can unexpectedly overwrite a variable used elsewhere.

## Active recall

- When does the body of a function execute?
- Where does a function get its `$1` value?
- Why is `local` useful in a reusable function?

## Interview check

How would you combine a function with a `for` loop to process many names?

## Intuitive example

A function is a named tool on a workbench: define the tool once and use it
whenever the same job appears.

## Connections and exercises

- [[Bash Loops]] calls the function repeatedly in the `greeter` example.
- [[Bash Variables and Quoting]] explains `local name=$1` and quoted output.
- Practise with [greeter](bash_scripting/exercises/greeter).

> [!info] AI-added — verified
> The concise explanation of function arguments and `local` was added to make
> the guided exercise reusable. It was checked against the
> [GNU Bash Shell Functions](https://www.gnu.org/software/bash/manual/bash.html#Shell-Functions) section.

## Sources

- [GNU Bash Shell Functions](https://www.gnu.org/software/bash/manual/bash.html#Shell-Functions)
