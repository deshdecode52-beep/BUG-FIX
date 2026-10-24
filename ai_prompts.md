# AI Debugging Prompts for Lecture 8

Use these prompts during your practical and capture screenshots of your actual AI interaction.

## Prompt 1 — Explain a failing test
I am testing this Python function with unittest. The test expected 90.0 for [80, 90, 100], but got 135.0. Do not rewrite my code yet. Explain why this test is failing and tell me which line I should inspect.

## Prompt 2 — Check a proposed fix
I found the likely bug and plan to change `len(marks) - 1` to `len(marks)`. Do not give me a complete rewritten program. Tell me whether this addresses the failing tests and mention any related edge case I should rerun.

## Prompt 3 — Review after GREEN
Review my fixed `student_utils.py` and test summary. Do not rewrite it. Check whether the code matches the stated test cases, point out any edge case not covered, and tell me whether I changed the implementation instead of weakening the tests.
