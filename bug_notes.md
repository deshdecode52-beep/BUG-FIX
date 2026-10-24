# Bug Notes

| Bug | Evidence / Failed Test | Cause | Fix |
|---|---|---|---|
| Average calculation | `[80, 90, 100]` returned `135.0` instead of `90.0`; `[40]` caused `ZeroDivisionError` | Divided by `len(marks) - 1` | Divide by `len(marks)` |
| Pass boundary | `is_passing(40)` returned `False` instead of `True` | Used `>` rather than `>=` | Use `mark >= PASS_MARK` |
| Distinction grade | `get_grade(95)` returned `"First"` instead of `"Distinction"` | Checked `average >= 60` before `average >= 90` | Check the `>= 90` condition first |
