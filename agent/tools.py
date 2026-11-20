def calculate_expression(expression: str) -> str:
    """Evaluate a basic arithmetic expression (such as '245 * 18' or '(1200 + 450) / 3').

    Args:
        expression: A math expression using numbers and +, -, *, /, %, **, or parentheses.
    """
    allowed_chars = set("0123456789+-*/%.() ")
    if not expression or not set(expression).issubset(allowed_chars):
        return "Error: Unsupported characters in math expression."
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as exc:
        return f"Error evaluating expression: {exc}"


def get_project_note(topic: str) -> str:
    """Retrieve a saved project note for a given topic.

    Args:
        topic: Short keyword such as 'roadmap', 'stack', or 'ideas'.
    """
    notes = {
        "roadmap": "Phase 1: Tool calling & API. Phase 2: Persistent memory & webhooks.",
        "stack": "Python, FastAPI, GitHub Codespaces, Render free tier.",
        "ideas": "Add daily reminders, note lookup, and API status checks.",
    }
    key = topic.strip().lower()
    return notes.get(key, f"No note found for '{topic}'. Available topics: {', '.join(notes)}.")
