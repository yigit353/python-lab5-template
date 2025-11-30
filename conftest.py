import pytest
import sys

# Store scores
scores = {
    "easy": {"count": 0, "total": 4, "points": 2},
    "medium": {"count": 0, "total": 4, "points": 3},
    "hard": {"count": 0, "total": 4, "points": 5}
}


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    Custom hook to print the scorecard at the end of the test session.
    """
    passed_tests = terminalreporter.stats.get('passed', [])

    for test in passed_tests:
        if "easy" in test.nodeid:
            scores["easy"]["count"] += 1
        elif "medium" in test.nodeid:
            scores["medium"]["count"] += 1
        elif "hard" in test.nodeid:
            scores["hard"]["count"] += 1

    total_score = (scores["easy"]["count"] * scores["easy"]["points"]) + \
                  (scores["medium"]["count"] * scores["medium"]["points"]) + \
                  (scores["hard"]["count"] * scores["hard"]["points"])

    max_score = (4 * 2) + (4 * 3) + (4 * 5)  # 40

    terminalreporter.section("Lab 5 Score Summary")
    terminalreporter.write_line(
        f"Easy Tasks ({scores['easy']['points']} pts each):   {scores['easy']['count']}/{scores['easy']['total']}")
    terminalreporter.write_line(
        f"Medium Tasks ({scores['medium']['points']} pts each): {scores['medium']['count']}/{scores['medium']['total']}")
    terminalreporter.write_line(
        f"Hard Tasks ({scores['hard']['points']} pts each):   {scores['hard']['count']}/{scores['hard']['total']}")
    terminalreporter.write_line("-" * 30)
    terminalreporter.write_line(f"TOTAL SCORE: {total_score} / {max_score}")
    terminalreporter.write_line("-" * 30)