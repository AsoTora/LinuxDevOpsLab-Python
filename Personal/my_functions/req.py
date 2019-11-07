with requests.Session() as session:
    session.auth = (user, passwd)

    r = session.get(api_url + '/users/' + user)
    repos = session.get(repos_url % user)
for repo in json.loads(repos.text):
    print(repo['name'])
