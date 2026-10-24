PASS_MARK = 40

def calculate_average(marks):
    """Return the arithmetic mean of the supplied marks."""
    if not marks:
        raise ValueError("marks must contain at least one value")

    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)


def is_passing(mark):
    """A mark equal to or above PASS_MARK is passing."""
    return mark >= PASS_MARK


def get_grade(average):
    """Return the grade for an average, checking the highest threshold first."""
    if average >= 90:
        return "Distinction"
    elif average >= 60:
        return "First"
    elif average >= 45:
        return "Second"
    return "Fail"
