
def parse_salary(text: str)->float | None:
    """Return a non-negative salary or None if invalid."""
    try:
        salary = float(text)
    except ValueError:
        return None
    if salary<0:
        return None
    return salary


