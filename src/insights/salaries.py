from typing import Union, List, Dict
from src.insights.jobs import (read)
# from jobs import read


def get_max_salary(path: str) -> int:
    job_list_no_filter = read(path)
    job_list_filtred = []
    for job in job_list_no_filter:
        if job['max_salary'] != '' and job['max_salary'] != 'invalid':
            job_list_filtred.append(job['max_salary'])

    max_salary = 0
    for job in job_list_filtred:
        if int(job) > int(max_salary):
            max_salary = int(job)
    return max_salary


# print(get_max_salary('data/jobs.csv'))


def get_min_salary(path: str) -> int:
    job_list_no_filter = read(path)
    job_list_filtred = []
    for job in job_list_no_filter:
        if job['min_salary'] != '' and job['min_salary'] != 'invalid':
            job_list_filtred.append(job['min_salary'])

    min_salary = 1000000000000
    for job in job_list_filtred:
        if int(job) < int(min_salary):
            min_salary = int(job)
    return min_salary

# print(get_min_salary('data/jobs.csv'))


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if ('min_salary' not in job) or ('max_salary' not in job):
        raise ValueError
    elif type(job['min_salary']) not in [int, str] or\
            type(job['max_salary']) not in [int, str] or\
            type(salary) not in [int, str] or\
            job['min_salary'] == '' or\
            job['max_salary'] == '':
        raise ValueError

    min_salary = int(job['min_salary'])
    max_salary = int(job['max_salary'])
    salary = int(salary)

    if min_salary > max_salary or min_salary < 0 or max_salary < 0:
        raise ValueError
    elif min_salary <= salary and max_salary >= salary:
        return True
    return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    job_list_filtred = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list_filtred.append(job)
        except ValueError:
            pass
    return job_list_filtred


# jobs = read('data/jobs.csv')
# salary = 100_000

# print(filter_by_salary_range(jobs, salary))
