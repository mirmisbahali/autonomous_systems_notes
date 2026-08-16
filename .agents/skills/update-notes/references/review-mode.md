# Active-recall review mode

## Choose material

1. Apply the user's requested domain or concept filter, if any.
2. Prefer concepts with `last_reviewed: null`, then low confidence, low mastery, weak links, or unresolved confusion.
3. Mix related concepts when comparison will improve discrimination. Do not pretend this selection is a scheduled spaced-repetition algorithm.

## Conduct the session

1. State the selected scope and ask one stored or newly phrased recall question.
2. Wait for the user's complete response. Do not reveal hints, headings, or the answer prematurely.
3. Separate feedback into:
   - what was correct;
   - the smallest important gap or misconception;
   - one concise correction or follow-up question.
4. Ask the user for a confidence rating from `0` to `4`:
   - `0`: no recall;
   - `1`: recognised after prompting;
   - `2`: partial explanation;
   - `3`: clear independent explanation;
   - `4`: clear explanation with trade-offs and failure cases.
5. Continue one question at a time until the requested scope or session ends.

## Record the session

- Write the user's rating to `confidence`; never replace it with an AI rating.
- Set `last_reviewed` only on notes actually attempted.
- Do not raise `mastery` because of a review answer. The repository evidence policy still applies.
- Record misconceptions as a short clarification in the relevant note only when the user agrees it was a genuine gap; mark new factual material under the AI-addition policy.
- Append a dated learning-log entry and rebuild the dashboard.
- Do not add `next_review`, due dates, review tasks, or automatic schedules.
