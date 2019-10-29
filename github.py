#! /usr/bin/env python3
# Andrei Svedau

import getpass
import argparse
import requests
from requests import exceptions
import json
from datetime import datetime
import calendar

api_url = 'https://api.github.com'
repos_url = 'https://api.github.com/repos/%s/repos'
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
    parser.add_argument('-n', '--number',
                        help="Number of days pr was opened", action="store_true")
    # Positional
    parser.add_argument('username', help="set github username", default=None)
    parser.add_argument('repo', nargs='?', default='Hello-World')
    args = parser.parse_args()
    return args


def retrieve_info(user, repo):
    with requests.Session() as session:
        session.auth = (user, getpass.getpass())
        try:
            pulls = session.get(pulls_url % (user, repo))
        except exceptions.HTTPError as e:
            print(e)

    return json.loads(pulls.text)


if __name__ == '__main__':
    args = get_args()
    pulls = retrieve_info(args.username, args.repo)

    for pull in pulls:
        print('Pull Request "{}":'.format(pull['title']))

        if args.user:
            print("\twas opened by {}".format(pull['user']['login']))

        if args.day:
            datetime = datetime.strptime(pull['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            weekday = calendar.day_name[datetime.date().weekday()]
            print("\twas opened on {} {} at {}".format(weekday, datetime.date(), datetime.time()))

        if args.number:
            if pull['closed_at'] is None:
                print("\tPR is still opened")
            else:
                opened = pulls['created_at']
                closed = pulls['closed_at']
                print("\tPR was opened {} days".format(str(closed - opened)))

        print("\n *** \n")
