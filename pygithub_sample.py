#!/usr/bin/env python3

from github import Github

def load_token():
    with open('github_token', 'r') as fr:
        data = fr.readline().strip()
    return data

TOKEN = load_token()

def tutorial():
    g = Github(TOKEN)
    for repo in g.get_user().get_repos():
        print(repo.name)

def main():
    g = Github(TOKEN)
    print(g.get_user().name)

    d = {}
    for i, issue in enumerate(g.search_issues('author:ki4070ma is:pr')):
        print(i, issue.title)
        name = issue.repository.full_name
        if name in d.keys():
            d[name].append(issue)
        else:
            d[name] = [issue]
        if i == 10:  # TODO Remove
            break

    for key in d.keys():
        print(f'\n***{key}')
        for issue in d[key]:
            s_time = issue.created_at.strftime("%Y-%m-%d")
            e_time = issue.closed_at.strftime("%Y-%m-%d") if issue.closed_at else ''
            days = (issue.closed_at - issue.created_at).days if e_time else '-'
            print(s_time, e_time, f'{days} days', issue.title)

if __name__ == '__main__':
    # tutorial()
    main()