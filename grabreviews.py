from github import Github
from datetime import datetime, timedelta
import sys


def write_comment(pr_number, comment):
    try:
        print(f'#{pr_number} {comment.user.login}: {comment.body}')
    except:
        print(f'** skipped a print for #{pr_number}')


def get_pull_request_comments(repo, since_date):
    for pull_request in repo.get_pulls(state='all'):
        if pull_request.updated_at >= since_date:
            print(f'PR {pull_request.number}')
            for comment in pull_request.get_review_comments():
                write_comment(pull_request.number, comment)
            for comment in pull_request.get_issue_comments():
                write_comment(pull_request.number, comment)


def main():
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]
    github_token = sys.argv[3]

    g = Github(github_token)
    repo = g.get_repo(f'{repo_owner}/{repo_name}')

    # Calculate the date 6 months ago
    six_months_ago = datetime.now() - timedelta(days=180)

    # Get all comments from pull requests since the calculated date
    get_pull_request_comments(repo, six_months_ago)


if __name__ == "__main__":
    main()
