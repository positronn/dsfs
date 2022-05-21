# api_github.py
import requests
import json
from pprint import pprint
from collections import Counter
from dateutil.parser import parse

github_user = 'positronn'
endpoint = f'https://api.github.com/users/{github_user}/repos'

repos = json.loads(requests.get(endpoint).text)

pprint(repos)

dates = [parse(repo['created_at']) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

# get the languages of last five repositories:
last_repos = sorted(repos,
                    key=lambda r: r['pushed_at'],
                    reverse=True)[:5]

last_langs = [repo['language'] for repo in last_repos]

pprint(f'last_langs: {last_langs}')
