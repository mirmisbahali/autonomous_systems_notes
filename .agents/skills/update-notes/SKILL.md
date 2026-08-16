---
name: update-notes
description: Organise rough learning notes and knowledge found in newly committed repository changes into concise, atomic Obsidian notes with Maps of Content, typed links, active-recall prompts, evidence-aware mastery metadata, core-Markdown dashboards, and a learning log. Use for requests to update, reorganise, deduplicate, connect, audit, or review this autonomous-systems learning vault, including explicit `$update-notes` update and review sessions.
---

# Update Notes

Preserve the user's learning integrity while turning committed running notes into a compact system for retrieval practice and later review. Follow the repository `AGENTS.md` before these instructions.

## Select the mode

- Treat `$update-notes` as **update mode**.
- Treat `$update-notes review` or a request to quiz/review notes as **review mode**.
- Accept an optional domain, MOC, or concept filter in review mode.

## Run update mode

1. Find the repository root and read `AGENTS.md`.
2. Read [note-system.md](references/note-system.md) and [learning-principles.md](references/learning-principles.md).
3. Run the change scanner before reading candidate files:

   ```bash
   python3 .agents/skills/update-notes/scripts/change_tracker.py scan \
     --state .update-notes/state.json \
     --output /tmp/update-notes-scan.json
   ```

4. Stop without editing notes if the scan reports no candidates. Report ignored uncommitted files separately.
5. If the scan reports a blocking conflict, do not overwrite it or advance the checkpoint. Continue with non-conflicting candidates only when the entire run can remain consistent; otherwise report the path and stop.
6. Inspect candidate **file contents**, not commit messages. Apply these boundaries:
   - Reorganise candidate Markdown learning notes.
   - Read code, build files, configuration, PDFs, and images only as context for concepts and examples.
   - Never edit source code, build files, assessment solutions, independent evidence artifacts, or files marked `assessment: true` or `ai_edit: false`.
   - Ignore deleted files and eligible renames reported by the scanner.
7. Preserve correct wording where practical. Fix structure, grammar, duplicated explanation, and inaccurate links without inflating the note.
8. Split a note containing distinct reusable ideas into atomic concept notes. Convert the original broad topic path into a concise MOC so existing links remain valid.
9. Merge duplicated explanations into one canonical atomic note. Convert obsolete duplicate note paths into link-only redirects; do not leave duplicate prose.
10. Add a short code example only when a changed code file demonstrates the concept. Do not present assessment code as AI implementation or claim tests pass unless they were run.
11. Add background knowledge only when it removes a comprehension gap. Treat every factual, curricular, or technical claim absent from the inspected candidate/context files as background knowledge; restructuring and grammar changes alone are not background. Do not invent future learning-path topics for a MOC. Mark background `AI-added`; cite an authoritative primary source when practical. Mark unresolved additions `needs verification`.
12. Add typed relationships and active-recall questions using the schemas in `note-system.md`. Never infer practical mastery from study notes.
13. Make a source-coverage checklist from every substantive heading or distinct idea in each candidate note. Before finalising, map each item to a new atomic note, an existing canonical note, retained source context, or an explicit open gap. Do not silently omit the final sections of a running note.
14. Append one run entry to `00_dashboard/Learning Log.md` containing the date, scanned commit range, concepts created or changed, splits or merges, AI additions and sources, skipped protected paths, and verification performed.
15. Rebuild and audit the core-Markdown dashboard:

   ```bash
   python3 .agents/skills/update-notes/scripts/audit_notes.py \
     --root . \
     --dashboard "00_dashboard/Knowledge Dashboard.md"
   ```

16. Resolve errors introduced by the run. Do not rewrite unchanged legacy notes merely to satisfy the audit.
17. Finalise only after all intended edits, the source-coverage check, and audits succeed:

   ```bash
   python3 .agents/skills/update-notes/scripts/change_tracker.py finalise \
     --state .update-notes/state.json \
     --scan /tmp/update-notes-scan.json \
     --path "00_dashboard/Knowledge Dashboard.md" \
     --path "00_dashboard/Learning Log.md"
   ```

   Add every newly generated or modified note with another `--path`. The command records candidate and output hashes and advances the checkpoint. Do not finalise a partial or failed run.

## Run review mode

Read [review-mode.md](references/review-mode.md), then conduct the session interactively. Ask one question at a time and wait for the user before revealing or evaluating the answer.

After the session:

- Record only the user's confidence rating.
- Update `last_reviewed` only for questions actually attempted.
- Never raise `mastery` from a verbal answer alone.
- Append a short review entry to the learning log and rebuild the dashboard.
- Do not calculate a next-review date or create review tasks.

## Protect knowledge integrity

- Use `mastery: 0` and `confidence: null` for new notes unless the user explicitly supplies stronger evidence.
- Use the most conservative supported `knowledge_status`.
- Require linked independent evidence before setting mastery above `2`.
- Distinguish theoretical study, assisted implementation, independent implementation, independent debugging, and integration.
- Do not modify the skills matrix merely because a concept note or review answer exists.

## Report the result

Lead with the concepts organised and any blockers. State the inspected commit range, whether the audit passed, what was marked for verification, and that uncommitted files were intentionally ignored. Never claim an exercise or code change passes without an executed test command and result.
