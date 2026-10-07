# Daily routine

How a school day runs, how work is checked, and how the kids grow into running their own day. Written for both the parent and the kids: nothing here is secret.

## Subjects

| Slot | Subject | Notes |
|---|---|---|
| Core 1 | Maths | Every day. Separate track per kid (Khan Academy for the US student, Oak for the UK student). |
| Core 2 | English or science | Alternate by day: week A English Mon/Wed/Fri, science Tue/Thu; week B the reverse. Shared topic for both kids. |
| Aux 1 | Practical history topic | Social studies, history and human geography from `practical_history.md`. Shared. |
| Aux 2 | A second practical history topic | Runs in parallel with Aux 1. Shared. |
| PE | 30 min | Every day. |

The natural-science part of geography (plates, weather, climate, ecosystems) is taught in the science slot.

A topic runs two weeks. Every topic has a folder in `topics/` with reading material, 12 questions the kids must be able to answer by the end, and a parent-only `key.md`.

## The day

| Time | Kids | Parent |
|---|---|---|
| 08:45-08:55 | Fill in the day sheet: plan and time estimate per block | **Kickoff (10 min):** look at both day sheets together with each kid |
| 09:00-10:00 | Core 1: maths | Work |
| 10:15-11:15 | Core 2: English or science | Work |
| 11:15-12:00 | Finish and review the morning; get ready for the teach-back | Work |
| 12:00-12:20 | Lunch | **Checkpoint on full support (20 min)** |
| 13:00-13:45 | Aux 1 | Work |
| 14:00-14:15 | | **Checkpoint on medium or light support (15 min)** |
| 14:15-15:00 | Aux 2 | Work |
| 15:00-15:45 | Self-marking, day sheet: actual times, done or not | Work |
| 16:00-16:15 | | **Close (15 min)** |
| 16:15-16:45 | PE, together as a family | **PE with the kids (30 min)** |
| Friday 16:00-16:45 | Week review (see below) | **Weekly close (45 min)**; family PE moves to 16:45 |

Parent time: about 45 minutes a day in three fixed blocks, plus family PE straight after the close. Nothing else needs you unless the morning isn't done at the checkpoint.

Breaks between blocks are 15 minutes. Lunch is 12:00-13:00.

The 08:45 start is the same every day, in the same place, on purpose: a fixed cue is what turns a routine into a habit that runs without willpower.

## What "done" means

Every block in the weekly plan (`weeks/<date>/week.md`, shown on the progress board's "This week" page) has a "done" line. A block is done when everything on that line exists, in the right place, at the time of the checkpoint.

Rules that apply to every block, and why:

- **Written work goes into Google Docs:** one doc per subject per topic, named `<Subject> - <Topic>`, shared with the parent. Each day starts with a heading: `Day N - <date>`. *Why: one place to look makes checking take two minutes instead of twenty.*
- **Type it yourself, in your own words.** No pasting, no AI, no translation tools; quotes are fine in quotation marks. *Why: the learning happens in the effort of putting it into your words. A pasted answer is a day of work with nothing left in your head.*
- **Laptops face the room; phones stay with the parent until the close.** *Why: apps are engineered by some of the best-paid people in the world to win your attention. That's not a fair fight for anyone, adult or teen. This rule takes the fight off the table.*

## Checkpoint (parent, 15-20 min)

1. **"Anything to flag?"** Stuck, skipped, took a shortcut, anything. Ask it every time, in the same neutral tone. Thank them for anything they flag, before anything else.
2. **Look (2 min per kid):** open each Google Doc due by now. Is every "done" item there? Open version history on the docs the kid's support level says: look for large blocks of text appearing at once.
3. **Teach-back:** for each subject the kid's support level says, ask the kid to explain:
   - "What did you learn in this one?" (let them talk for a minute),
   - one question from that topic's `key.md` (verbal questions section),
   - one sentence they wrote: "say this to me in different words".

   Explaining from memory is one of the strongest ways to learn (retrieval practice), so this is part of the learning, not just a check. It also shows clearly whether the work is theirs.
4. **Then:**
   - Morning done: say one specific thing you noticed in their work.
   - Morning not done: the rest of the day, they work next to you, and you look at each block as it ends. Say it plainly and without heat: "Let's do the afternoon side by side."
   - A shortcut: see "Shortcuts" below.

## Self-marking (kids, 15:00)

1. Open the answers file for today's self-test or questions (maths: `self_test_answers.md`; other subjects: answers are checked against the reading).
2. Mark your own work **in a different colour** (green). Do not change the original answer.
3. For every mistake write one line: what kind of mistake it was, and whether it is **new** or **again**.
4. Write the score at the top of the day.

Attempt first, open the answers second. *Why: finding your own mistakes is the fastest way to stop making them. "Again" mistakes are the most useful ones to catch.*

## Close (parent, 15 min)

1. "Anything to flag?"
2. "What was the most interesting thing today?" Listen; this is the part where you're a person who's curious about what they learned, not an inspector.
3. Day sheets: actual times and done/not done filled in?
4. Look at one self-marked item per kid: did they catch their own mistakes?
5. After family PE, record the day in `progress/log.csv` (one line per kid). Run `python3 tools/progress.py status` and tell each kid tomorrow's support level. Phones are returned.

## Rank and support

Two separate things:

- **Rank** is who you've become: how much of your own day you've shown you can run. It's earned, and **it never goes down.** It's on the progress site.
- **Support** is how much help you get on a given day. It follows your rank, but can tighten for a couple of days after a hard day, the way a coach steps in closer when a player is struggling. It says nothing about who you are.

### Self-run days

A **self-run day** is a day when:
- the day sheet was filled in by 09:00,
- the morning was done by the checkpoint,
- in the teach-back, you could explain your work in your own words (one "I'm not sure, but I think..." is fine),
- self-marking was done,
- PE was done (if family PE doesn't happen, that doesn't count against the kid),
- any shortcut was flagged by you and fixed.

### Ranks

| Rank | Earned by | What it gives you |
|---|---|---|
| **0** | Starting point | Choices inside each block: the order you answer questions, your PE activity, the examples you pick in tasks, the format of final pieces. |
| **1** | 5 self-run days out of your last 6 | Medium support. You choose, together with your sibling, the next practical history topic from the list. At the checkpoint you present your own work first, before the parent looks. |
| **2** | 10 self-run days out of your last 12 | Light support. You choose the order of your blocks. You help write next week's plan at the weekend. Once a week you teach your sibling something from a topic you're ahead on. |
| **3+** | Defined later, from real data | |

Kids can name their ranks. The parent and kid mark a rank-up however the kid chooses (small and theirs).

Why "most days" and not "every day in a row": research on habits shows a single missed day doesn't undo a habit; only frequent gaps do. One bad day shouldn't wipe out a good week, so it doesn't.

### Support levels

| Support | Normally at | First checkpoint | Teach-back | Version history |
|---|---|---|---|---|
| **Full** | Rank 0 | 12:00, and the close | Every subject done that day | Every doc |
| **Medium** | Rank 1 | 14:00, and the close | 2 subjects, picked at random | 2 docs, picked at random |
| **Light** | Rank 2 | 14:00, and the close | 1 subject, picked at random, 3 questions | 1 doc, picked at random |

There's always a checkpoint. Feedback stays daily at every rank.

Support tightens by one step (Light → Medium → Full) after:
- a morning that wasn't done by the checkpoint, or
- a shortcut found by the parent that was a whole block (see below).

It returns to the rank's normal level after **2 self-run days**. `tools/progress.py status` works this out.

## Shortcuts

Taking a shortcut is normal: everyone does it when something feels too hard, too boring, or pointless. A shortcut is information about the task, the day or the support, not a verdict on the kid. The response is always the same three steps:

1. **Repair:** redo the work, properly.
2. **Understand:** "What made the shortcut tempting?" Too hard? Too long? Didn't see the point? Tired? Listen.
3. **Adjust:** change what needs changing: the task size, an explanation, a break, the support.

| What happened | Repair | Support |
|---|---|---|
| **Small:** a sentence copied without quote marks, peeking at answers early, one answer they can't explain | Redo it now | No change |
| **A block:** a whole answer or block that isn't theirs (pasted, AI, copied from the sibling), or self-marking that skipped over mistakes | Redo the block next to the parent | One step tighter, back after 2 self-run days |
| **A pattern:** the same thing again within a week, or saying work is theirs when it isn't | Redo the work next to the parent | Full support, back after 2 self-run days. Plus a sit-down: something in the setup isn't working for this kid, and the plan should change, not just the kid. |

**Flagged by the kid,** at the "anything to flag?" question or before: repair only. No change in support, and a small shortcut that was flagged and fixed still leaves the day self-run. Flagging is the skill we're building: noticing your own corner-cutting and saying so is exactly what self-direction looks like.

Talk about the act, never the person: "this answer isn't yours, let's redo it", never "you're a cheat" or "I can't trust you".

## Tracking self-direction

Recorded daily in `progress/log.csv`. Public on the progress site: rank, self-run days, morning-done rate, teach-back, estimates, "again" mistakes. Shortcuts and flags stay between parent and kid.

| Measure | What it shows | Grounded competence skill |
|---|---|---|
| Rank, self-run days (total and last 10) | Running your own day, over time | Ownership of mental capacities |
| Mornings done by the checkpoint | Can they run a morning alone | Ownership, emotional regulation |
| Estimate vs. actual minutes | Do they know how long things take | Temporal awareness |
| Self-marking: mistakes caught, "again" mistakes | Do they see their own mistakes | Metacognition, humility |
| Flags raised by the kid vs. shortcuts found by the parent | Noticing and naming their own corner-cutting | Humility & unlearning, metacognition |

Rate the grounded competence skills in `students/<name>/profile.md` once a month from these numbers, not from impressions.

## How to talk about it (parent's guide)

Based on `research/2026-10-08_motivation_and_identity.md`.

1. **Give the reason.** Every request comes with its why. The "why" lines in this file are there to be said out loud.
2. **Acknowledge the feeling, keep the task.** "Yes, this reading is long and dry. Do the first part, then tell me if it was worth it." Don't argue with the complaint.
3. **Invite, don't command.** "What's your plan for science?" rather than "Do your science."
4. **Use identity words for what they actually did.** "That's what a self-directed person does: you noticed you were stuck and changed approach." Name the identity, attached to real evidence, never as flattery.
5. **Critique with high standards and belief.** When pointing out what's weak: "I'm telling you this because the standard here is high and I know you can reach it."
6. **Difficulty means it matters.** When something's hard: "Hard means you're at the edge of what you know. That's where the learning is."
7. **Name mastery.** "Two weeks ago you couldn't do this." Make progress visible: it's the strongest source of confidence there is.
8. **Respect is the lever.** Teenagers respond to being treated as capable and given real responsibility, not to rules and lectures. Ranks give real responsibility; use it.
9. **Never compare the two kids.** Compare each kid with their own last week.
10. **Your consistency is the model.** Run the three parent blocks on time.

### The week review (Friday)

Each kid writes four lines on their Friday day sheet:

1. Something I can do now that I couldn't before.
2. Something that was hard this week, and why it mattered.
3. What I'll try next week.
4. This week shows I'm someone who ___.

Read them with each kid separately. Line 4 is theirs: don't correct it, ask about it.

### Screen time

Right now screen time is earned back by doing schoolwork. Research on rewards (see the research report) predicts this works as a start but blocks the shift to doing the work for its own sake: an expected reward for completing a task lowers interest in it. Suggested path: as rank rises, decouple screen time from schoolwork until it's a fixed household allowance that has nothing to do with the school day. Parent's decision.

## Topic tests

Friday of a topic's week 2 is test day. Each block starts with that subject's test: the kid answers 4 of the 12 questions, picked by the parent and written on paper the evening before, handwritten, closed book, no devices, 30 minutes. The core 2 block holds both the English and the science test. Maths uses its own self-test or Khan unit test. Mark with the topic's `key.md` at the weekly close or the weekend, record in `progress/tests.csv`.

These are the main evidence of learning, and the main evidence that the daily work was real.

## Weekly cycle

- **Friday close:** week review; kids write their three lines. In a topic's week 2, mark the tests (or leave them for the weekend).
- **Weekend (parent with Claude, ~30 min):** update logs and profiles, publish the progress board (`python3 tools/progress.py publish`, which updates https://lorinc.github.io/progress-board/), prepare next week's plan and materials.

## Files

| Path | What |
|---|---|
| `weeks/<monday's date>/week.md` | That week's plan for both kids (pseudonyms only): schedule, materials, what to do per block, what "done" looks like. Published as the "This week" page. |
| `weeks/day_sheet.md` | Printable day sheet: plan, estimates, actuals. |
| `topics/<subject>/<topic>/` | Reading, questions, self-tests, and the parent-only `key.md`. |
| `progress/log.csv`, `progress/tests.csv` | Daily and test records, source of the progress site. |
