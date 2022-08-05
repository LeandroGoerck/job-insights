from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "Responsibilities") == 1645
    assert count_ocurrences("src/jobs.csv", "xablau") == 0
