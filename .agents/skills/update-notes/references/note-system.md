# Note system

Use Australian English, plain technical language, short paragraphs, and only the formatting that improves retrieval or comparison.

## File and linking rules

- Keep the existing domain folders; do not build a nested folder taxonomy.
- Use human-readable filenames and one reusable idea per concept note.
- Keep broad topic paths as Maps of Content (MOCs).
- Build a MOC's learning path only from committed concepts actually inspected or already established in the vault. Do not fill it with a generic curriculum.
- Prefer `[[wikilinks]]`. Express meaning through frontmatter relationship fields and labelled sections, not unlabeled link lists.
- Select one canonical note for a concept. Replace obsolete duplicates with only `Moved to [[Canonical note]].`
- Check every substantive source heading and distinct idea before finalising. Account for it with an atomic note, an existing canonical note, retained source context, or an explicit open gap; never drop content merely because it occurs near the end of a rough note.
- Use Mermaid only when three or more relationships are materially clearer as a diagram.
- Link evidence and exercises; do not copy their implementation into a note.

## Common frontmatter

Use these fields on managed notes:

```yaml
---
type: concept
domain: cpp
tags:
  - note/concept
aliases: []
confidence: null
mastery: 0
knowledge_status: studied-theoretically
evidence: []
last_reviewed: null
prerequisites: []
related: []
contrasts: []
examples: []
implemented_in: []
used_by: []
ai_edit: true
---
```

Rules:

- Set `confidence` only from the user's `0–4` self-rating.
- Use the skills-matrix meanings for `mastery`. Require linked independent evidence above `2`.
- Use exactly one `knowledge_status`: `studied-theoretically`, `assisted`, `independently-implemented`, `independently-debugged`, or `integrated`.
- Set `last_reviewed` to `YYYY-MM-DD` only after an attempted recall question.
- Use quoted wikilinks inside YAML lists, for example `prerequisites: ["[[Compilation]]"]`.
- Treat `assessment: true` or `ai_edit: false` as immutable.

## Concept notes

Use `../assets/templates/Concept Note.md`. Keep these sections in order:

1. Why it matters
2. In simple terms
3. How it works
4. Concrete example
5. Common failure modes
6. Active recall
7. Interview check
8. Intuitive example
9. Connections and exercises
10. Sources

Keep recall questions answerable from the note but do not place answers directly beneath each question. Prefer two to four questions that require explanation, comparison, prediction, or reconstruction.

## Lecture or course notes

Use `../assets/templates/Lecture Course Note.md`. Treat the source note as a capture record and MOC, not a second copy of every concept. Preserve source context, objectives, linked atomic concepts, key connections, and unresolved questions.

## Project or design notes

Use `../assets/templates/Project Design Note.md`. Separate requirements from design choices. Include architecture, interfaces, trade-offs, failure handling, verification evidence, and concept links. Never invent test results.

## Interview-question notes

Use `../assets/templates/Interview Question.md`. State the question, a concise answer, the reasoning, common traps, likely follow-ups, and evidence links. Keep the answer short enough to say aloud.

## Maps of Content

Use `../assets/templates/Map of Content.md`. A MOC contains navigation and sequence, not repeated explanations. Include purpose, prerequisites, concept map, suggested learning path, projects or exercises, and open gaps.

## AI additions

Mark every factual, curricular, or technical addition not supported by inspected repository content with one of these callouts. Ordinary restructuring, grammar correction, and recall-question phrasing do not require a callout.

```markdown
> [!info] AI-added — verified
> Concise addition. [Primary source](https://example.com)
```

```markdown
> [!warning] AI-added — needs verification
> Concise unresolved addition.
```

Prefer official documentation, standards, or peer-reviewed primary research. Do not add background merely because it is related.

## Dashboard and learning log

Maintain ordinary Markdown without Dataview. The dashboard should expose managed concepts by domain, never-reviewed or low-confidence concepts, orphan concepts, evidence inconsistencies, unresolved AI additions, audit issues, and recent activity.

For each update log entry, record:

- inspected commit range;
- concepts created or changed;
- splits, merges, and redirects;
- code or other context inspected;
- AI additions and sources;
- protected or conflicting paths skipped;
- audit and test commands actually run.

For each review entry, record attempted notes, user confidence values, concise feedback topics, and metadata updated.
