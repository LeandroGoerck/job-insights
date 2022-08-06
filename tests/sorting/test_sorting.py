from src.sorting import sort_by


def test_sort_by_criteria():

    fake_job_list = [
        {
            "job_title": "AnyJob",
            "company": "AnyCompany",
            "state": "AnyState",
            "city": "AnyCity",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "AnyJobDescription",
            "industry": "AnyIndustry",
            "rating": "4.0",
            "date_posted": "2019-07-08",
            "valid_until": "2023-06-08",
            "job_type": "AnyJobType",
            "id": "0"
        },
        {
            "job_title": "SecJob",
            "company": "SecCompany",
            "state": "SecState",
            "city": "SecCity",
            "min_salary": "10000",
            "max_salary": "15000",
            "job_desc": "SecJobDescription",
            "industry": "SecIndustry",
            "rating": "4.0",
            "date_posted": "2022-06-08",
            "valid_until": "2023-06-08",
            "job_type": "SecJobType",
            "id": "0"
        },
        {
            "job_title": "ThirdJob",
            "company": "ThirdCompany",
            "state": "ThirdState",
            "city": "ThirdCity",
            "min_salary": "9000",
            "max_salary": "20000",
            "job_desc": "ThirdJobDescription",
            "industry": "ThirdIndustry",
            "rating": "4.0",
            "date_posted": "2021-06-08",
            "valid_until": "2023-06-08",
            "job_type": "ThirdJobType",
            "id": "0"
        },
            ]
    sort_by(fake_job_list, "max_salary")
    assert fake_job_list[0]["max_salary"] == "20000"

    sort_by(fake_job_list, "min_salary")
    assert fake_job_list[0]["min_salary"] == "9000"

    sort_by(fake_job_list, "date_posted")
    assert fake_job_list[0]["date_posted"] == "2022-06-08"
