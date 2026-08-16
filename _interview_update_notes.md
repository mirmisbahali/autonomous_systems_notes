# `/update_notes` and Obsidian Note-System Interview

> **Status:** Temporary planning file. Please answer inline beneath each question.
>
> This file will not be treated as part of the final note system unless you choose to keep it.

## 1. Learning goals

### 1. What are your main learning areas and priorities?

**Answer:** Refer [[Roadmap]] and [[skills_matrix]] to understand this

### 2. What should notes help you do most effectively?

Examples: recall concepts, pass interviews, build projects, write reports, track progress, or all of these.

**Answer:**all of these

### 3. Do you prefer concise revision notes, detailed explanations, or a layered system with both?

**Answer:** layered system with both

## 2. Existing vault

### 4. What are the current top-level folders and important files?

Should the existing structure be preserved or reorganised?

**Answer:**you can reorganise if you want.

### 5. Are there existing naming conventions, frontmatter fields, tags, templates, indexes, or dashboards?

**Answer:**no

### 6. Which notes should be considered authoritative if multiple notes cover the same topic?

**Answer:**delete the duplicate information. Reading text takes time and I don't want to waste a lot of time reading the same thing again and again.

### 7. Should old notes be rewritten, or should `/update_notes` only add and connect new material?

**Answer:**I'm dumping down rough running notes while watching videos so please rewrite these old notes in well structured manner. rewrite only those notes that have been changed since the last git commit as I don't want to change already established and commited notes.

## 3. Note types

### 8. Which note types do you want templates for?

- [x] Concept notes
- [x] Lecture/course notes
- [ ] Book/article/video notes
- [ ] Exercise notes
- [x] Project/design notes
- [ ] Debugging notes
- [x] Interview-question notes
- [ ] Progress/reflection notes
- [ ] Daily learning logs
- [ ] Glossary/definition notes
- [ ] Review/assessment notes
- [ ] Other: 

### 9. Are there other note types you want?

**Answer:**no

### 10. Should each note type have a fixed structure, or should templates be lightweight prompts?

**Answer:**fixed structure

### 11. What sections should notes include?

Examples: why it matters, how it works, examples, failure modes, interview questions, related concepts, exercises, and review prompts.

**Answer:**write the concept in easy language. If there is code change then give example of this code in the notes under the concept relating to the code change. Write an intuitive example at the end.

## 4. Zettelkasten and linking

### 12. Do you want classic atomic notes—one idea per note—or larger topic notes containing several ideas?

**Answer:**atomic notes

### 13. Should concept notes use unique IDs or human-readable filenames?

Examples: `202608171430 Concept name` or `Concept name`.

**Answer:**human reable filenames

### 14. Which linking style do you prefer?

- [ ] Dense bidirectional links between related concepts
- [ ] A curated hierarchy with fewer links
- [x] A combination of both

### 15. Should new concept notes be created automatically when a commit introduces a distinct concept?

Or should the skill only link to existing notes?

**Answer:**new concept notes be created automatically

### 16. How should broader topic maps be represented?

- [x] Maps of Content (MOCs)
- [x] Dataview tables
- [ ] Canvas files
- [x] Mermaid diagrams
- [ ] Nested folders
- [ ] A combination
- [ ] Other: 

### 17. Should links distinguish relationships between concepts?

Examples: prerequisite of, example of, implementation of, alternative to, commonly confused with, and used by.

**Answer:**yes

## 5. Obsidian features

### 18. Which Obsidian plugins are installed or acceptable to use?

Examples: Dataview, Templater, Tasks, QuickAdd, Metadata Menu, Breadcrumbs, Excalidraw, Canvas, Git, or other community plugins.

**Installed plugins:** Dataview, Templater

**Acceptable new plugins:**

### 19. Are you willing to install plugins, or must the system use core Obsidian features only?

**Answer:**use core obsidian features only

### 20. Do you prefer YAML frontmatter, inline fields, tags, folders, or a combination?

**Answer:**yaml frontmatter, folders, tags, inline fields

### 21. Do you want tasks and review dates integrated into notes?

**Answer:**no

### 22. Should the system create automated indexes, dashboards, or progress summaries?

**Answer:**yes

## 6. Git-based update workflow

### 23. What commits should `/update_notes` inspect?

- [x] Commits since the last `/update_notes` run
- [ ] Commits since a specified date
- [ ] The full Git history
- [ ] Uncommitted changes as well
- [ ] Other: 

### 24. Should it inspect only changed Markdown files, or also other files?

Examples: code, PDFs, images, notebooks, and configuration files.

**Answer:**other files as well.

### 25. Where should the skill record the last processed commit?

**Answer:**record in [[AGENTS]] or where you recommend.

### 26. If a commit changes an existing note, what should the skill do?

- [ ] Summarise the change
- [x] Reorganise the note
- [x] Add missing links
- [ ] Add questions and review prompts
- [x] Preserve the original wording as much as possible
- [ ] All of these
- [ ] Other: 

### 27. Should updates be based on commit messages, diffs, file contents, or all three?

**Answer:**file contents

### 28. How should it handle deleted or renamed notes?

**Answer:**don't update the renamed notes if /update_notes skills had processed it before. Don't do anything with the deleted note

### 29. Should it create a changelog or learning-log entry for every update?

**Answer:**yes please

## 7. AI behaviour and boundaries

### 30. Should `/update_notes` only document knowledge present in the Git changes?

Or may it add useful background knowledge from general expertise?

**Answer:**can add useful background knowledge from general expertise but make sure don't add a lot of content as I don't want to make a mess. Reading takes time and I don't have time to read all the junk that's not useful so make sure if adding new content it's very short and concise but will explain the concept in simple and easy languge with less words

### 31. If it adds background knowledge, how should that be marked?

Examples: `AI-added`, `needs verification`, or a separate section.

**Answer:**AI-added and needs verification.

### 32. Should it ask for confirmation before substantial changes?

Examples: merging notes, renaming files, or creating many new notes.

**Answer:**not required

### 33. Should it avoid modifying assessment exercises and independently completed work?

**Answer:**yes

### 34. Should it distinguish levels of knowledge and evidence?

Examples: studied theoretically, implemented with assistance, implemented independently, debugged independently, and integrated into a larger system.

**Answer:**yes

## 8. Review and recall system

### 35. Do you want spaced-repetition prompts?

If yes, what schedule would you prefer?

**Answer:**not required

### 36. Should every concept note contain active-recall questions?

**Answer:**yes

### 37. Should the system generate interview questions automatically?

**Answer:**not required

### 38. Should it track confidence, mastery, evidence, and last-reviewed dates?

**Answer:**yes

### 39. Do you want periodic reports for weak connections or unreviewed concepts?

**Answer:**yes

## 9. Style and practical preferences

### 40. What language and spelling conventions should notes use?

Australian English will be assumed unless specified otherwise.

**Answer:** simple, technical, easy to understand australian english

### 41. Should notes be formal, conversational, exam-oriented, or engineering-oriented?

**Answer:** mix of conversational and engineering-oriented.

### 42. Which formatting features do you prefer?

- [x] Headings
- [x] Callouts
- [x] Tables
- [x] Checklists
- [x] Mermaid diagrams
- [x] LaTeX
- [ ] Other: 

### 43. Are there note-taking systems or authors whose style you want to emulate?

**Answer:** I like Zettelkasten for linking ideas

### 44. Do you want templates stored in a dedicated folder such as `_templates/`?

**Answer:** yes

### 45. Where should the skill itself be installed?

- [ ] Personal Codex skill
- [x] Repository-local skill
- [ ] Both
- [ ] Other: 

## 10. Desired first version

### 46. What would make the first version successful?

**Answer:** 

### 47. Provide one example of a recent Git commit and describe what notes you would have wanted it to produce.

**Commit/example:**

### 48. Should I first propose the complete note architecture for approval, then create templates, then implement `/update_notes`?

**Answer:** yes

## Additional requirements or concerns

**Answer:**

