from unittest.mock import mock_open, patch
from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    fake_data = "titulo,salario,tipo\nDeveloper,2000,effective"
    expected_job_list = [
        {"title": "Developer", "salary": "2000", "type": "effective"}
    ]

    with patch("builtins.open", mock_open(read_data=fake_data)):
        assert (
            read_brazilian_file("tests/mocks/brazilian_jobs.csv")
            == expected_job_list
        )
