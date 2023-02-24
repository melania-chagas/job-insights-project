from typing import List, Dict
from src.insights.jobs import (read)
# import jobs
# read = jobs.read


def get_unique_industries(path: str) -> List[str]:
    job_list = read(path)
    industries = []
    for job in job_list:
        if job['industry'] not in industries and job['industry'] != '':
            industries.append(job['industry'])
    return industries

# print(get_unique_industries('data/jobs.csv'))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    if industry == '':
        return []
    jobs_filtred = []
    for job in jobs:
        if job['industry'] == industry:
            jobs_filtred.append(job)
    return jobs_filtred


# jobs = read('data/jobs.csv')
# print(filter_by_industry(jobs, 'Finance'))
