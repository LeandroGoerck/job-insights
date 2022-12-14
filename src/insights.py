from src.jobs import read


def get_unique_job_types(path):
    # """Checks all different job types and returns a list of them

    # Must call `read`
    # read

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique job types
    # """
    jobs_list = read(path)

    unique_job_list = []
    for job in jobs_list:
        if job["job_type"] not in unique_job_list:
            unique_job_list.append(job["job_type"])

    return unique_job_list


def filter_by_job_type(jobs, job_type):
    # """Filters a list of jobs by job_type

    # Parameters
    # ----------
    # jobs : list
    #     List of jobs to be filtered
    # job_type : str
    #     Job type for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided job_type
    # """

    filtered_job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job_list.append(job)

    return filtered_job_list


def get_unique_industries(path):
    # """Checks all different industries and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique industries
    # """
    jobs_list = read(path)

    unique_industries_list = []
    for job in jobs_list:
        if job["industry"] not in unique_industries_list:
            if job["industry"] != "":
                unique_industries_list.append(job["industry"])

    return unique_industries_list


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry_list.append(job)

    return filtered_industry_list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    max_salary = 0
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            current_max_salary = int(job["max_salary"])
            if current_max_salary > max_salary:
                max_salary = current_max_salary

    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    min_salary = None
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            current_min_salary = int(job["min_salary"])
            if min_salary is None:
                min_salary = current_min_salary
            if current_min_salary < min_salary:
                min_salary = current_min_salary

    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if ("min_salary" or "max_salary") not in job:
        raise ValueError('Os valores n??o existem!')
    if type(job["min_salary"] or job["max_salary"] or salary) != int:
        raise ValueError("Os valores n??o s??o numeros inteiros")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("O sal??rio m??nimo ?? maior que o m??ximo")
    return int(job["min_salary"]) <= salary <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_in_salary_range = []
    for job in jobs:
        try:
            if type(salary) == int and matches_salary_range(job, salary):
                jobs_in_salary_range.append(job)
        except ValueError:
            pass

    return jobs_in_salary_range
