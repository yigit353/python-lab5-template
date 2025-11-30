import pytest

# Store scores
scores = {
    "easy": {"count": 0, "total": 4, "points": 2},
    "medium": {"count": 0, "total": 4, "points": 3},
    "hard": {"count": 0, "total": 4, "points": 5}
}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to attach markers to the report object so they can be accessed in the summary.
    """
    outcome = yield
    report = outcome.get_result()
    # Attach markers to the report
    report.markers = [m.name for m in item.iter_markers()]


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    Custom hook to print the scorecard at the end of the test session.
    """
    passed_tests = terminalreporter.stats.get('passed', [])

    for test in passed_tests:
        # Check markers attached in pytest_runtest_makereport
        markers = getattr(test, 'markers', [])

        if "easy" in markers:
            scores["easy"]["count"] += 1
        elif "medium" in markers:
            scores["medium"]["count"] += 1
        elif "hard" in markers:
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