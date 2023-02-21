from typing import List, Dict
from src.insights.jobs import (read)


def get_unique_industries(path: str) -> List[str]:
    job_list = read(path)
    industries = []
    for job in job_list:
        if job['industry'] not in industries and job['industry'] != '':
            industries.append(job['industry'])
    return industries

# print(get_unique_industries('data/jobs.csv'))

def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
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
    raise NotImplementedError
