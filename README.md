# Lecture 8 — Fixing a Buggy Python Script Using AI

## Overview
This project demonstrates the RED → FIX → GREEN debugging cycle using Python's `unittest`.

## Files
- `student_utils.py`: corrected implementation.
- `test_student_utils.py`: the nine specification-based tests.
- `red_stage/`: buggy implementation and the unchanged tests, for reproducing RED.
- `green_stage/`: fixed implementation and the same tests, for reproducing GREEN.
- `red_output.txt`: captured test output from running the tests against the buggy implementation.
- `green_output.txt`: captured test output from running the tests against the fixed implementation.
- `bug_notes.md`: bug, evidence, cause, and fix.
- `audit.md`: project audit.

## Run the GREEN tests
From this directory, run:
```bash
python test_student_utils.py
```
Expected result: all 9 tests pass.

## Reproduce the RED stage
1. Back up the root `student_utils.py`.
2. Copy `red_stage/student_utils.py` over `student_utils.py`.
3. Run `python test_student_utils.py` and save the failing output.
4. Restore the fixed root version from `green_stage/student_utils.py`.
5. Run `python test_student_utils.py` again.

The tests must not be weakened or edited to make them pass.

## RED → FIX → GREEN
- RED: the unchanged tests detect incorrect behavior in the buggy implementation.
- FIX: correct the denominator, pass-mark boundary, and grade-condition ordering.
- GREEN: rerun the same nine tests against the corrected implementation.

## GitHub
Create a repository (for example, `session8`), upload these files, and commit the RED and GREEN stages separately if your instructor requires visible commit history. Do not claim separate commits unless you actually create them in Git.

## Note
The lecture handout's specified tests cover nine cases. The fixed function also raises a clear `ValueError` for an empty marks list, an additional defensive behavior not covered by those nine tests.
