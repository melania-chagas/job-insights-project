from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r') as file:
        csv_file = csv.DictReader(file)
        jobs = []
        for line in csv_file:
            jobs.append(line)
        return jobs
# print(read('data/jobs.csv'))


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job['job_type'] not in job_types:
            job_types.append(job['job_type'])
    return job_types

# print(get_unique_job_types('data/jobs.csv'))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    if job_type == '':
        return []
    jobs_filtred = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_filtred.append(job)
    return jobs_filtred


# jobs = read('data/jobs.csv')
# print(filter_by_job_type(jobs, ''))
