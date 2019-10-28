#! /usr/bin/env python3
# Andrei Svedau

import getpass
import argparse
import requests
import json
from datetime import datetime
import calendar

passwd = ''
user = 'octocat'
repo = 'Hello-World'
api_url = 'https://api.github.com'
repos_url = 'https://api.github.com/users/%s/repos'
pulls_url = 'https://api.github.com/repos/%s/%s/pulls'
pull_url = 'https://api.github.com/repos/%s/%s/pull/%s'


def get_args():
    parser = argparse.ArgumentParser(prog='github-pr')
    # Optional args
    parser.add_argument('-v', '--version',
                        help="get script version", action='version', version='1.0')
    parser.add_argument('-u', '--user',
                        help="get user opened pr", action="store_true")
    parser.add_argument('-d', '--day',
                        help="get day of the weel pr was opened on", action="store_true")
    parser.add_argument('-l', '--lines',
                        help="get number of lines added to pr", action="store_true")
    # Positional
    parser.add_argument('username', help="set github username")
    args = parser.parse_args()

    user = args.username
    passwd = getpass.getpass()
    return args


def retrieve_info():
    with requests.Session() as session:
        session.auth = ('AsoTora', passwd)

        try:
            pulls = session.get(pulls_url % (user, repo))
        except requests.exceptions.RequestException as e:
            print(e)

        for pull in json.loads(pulls.text):  # TODO: check
            try:
                r = session.get(pull_url % (user, repo, pull['number']))
                additions[pull['number']] = json.loads(r.text)['additions']
            except requests.exceptions.RequestException as e:
                additions[pull['number']] = 0
                continue

        print(additions)

    return json.loads(pulls.text)


if __name__ == '__main__':
    additions = {}
    args = get_args()
    pulls = retrieve_info()

    for pull in pulls:
        print('Pull Request "{}":'.format(pull['title']))

        if args.user:
            print("\twas opened by {}".format(pull['user']['login']))

        if args.day:
            datetime = datetime.strptime(pull['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            weekday = calendar.day_name[datetime.date().weekday()]
            print("\twas opened on {} {} at {}".format(weekday, datetime.date(), datetime.time()))

        if args.lines:
            print("\twas added {} lines".format(additions[pull['number']]))

        print("\n *** \n")
