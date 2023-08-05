import os
from github import Github
from github import Auth

print('starting to browse...')
github_tok = os.environ['TOK'];
print(f'length of TOK is {len(github_tok)}')
auth = Auth.Token(github_tok)

g = Github(auth=auth)

for repo in g.get_user('AKLOL7').get_repos():
    print(repo.name)
