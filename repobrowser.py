import os
from github import Github
from github import Auth

print('starting to browse...')
github_tok = os.environ['TOK'];
print(f'length of TOK is {len(github_tok)}')
auth = Auth.Token(github_tok)

g = Github(auth=auth)

repo = g.get_repo("AKLOL7/PythonCode")
pull_requests = repo.get_pulls(state='all')
for pr in pull_requests:
    comments = pr.get_comments()
    created = pr.created_at
    updated = pr.updated_at
    merge_time = pr.merged_at
    print(f'Pull Request #: {pr.number}')
    print(f'Number of comments: {comments.totalCount}')
    print(f'This pull request was created at: {pr.created_at}')
    print(f' This pull request was updated at: {pr.updated_at}')
    print(f' Merge time : {merge_time}')
    time_between = pr.updated_at - pr.created_at
    print(f'This is the time between when the pull request was created and updated: {time_between}')
    sorted_comments = sorted(comments, key=lambda c: c.created_at)
    first_comment_created_at = sorted_comments[0].created_at
    print("First comment created at:", first_comment_created_at)
