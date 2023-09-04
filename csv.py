import github
import csv

# Replace 'YOUR_GITHUB_USERNAME' and 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual GitHub credentials
g = github.Github("YOUR_PERSONAL_ACCESS_TOKEN")

repo = g.get_repo("AKLOL7/PythonCode")
pull_requests = repo.get_pulls(state='all')

# Create and open a CSV file in write mode
with open('pull_requests.csv', 'w', newline='') as csvfile:
    fieldnames = ['Pull Request Number', 'Pull Request Name', 'Number of Comments', 'Created At', 'Updated At', 'Merge Time', 'Time Between', 'First Comment Created At']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row to the CSV file
    writer.writeheader()

    for pr in pull_requests:
        comments = pr.get_comments()
        created = pr.created_at
        updated = pr.updated_at
        merge_time = pr.merged_at
        pr_name = pr.title
        time_between = pr.updated_at - pr.created_at
        sorted_comments = sorted(comments, key=lambda c: c.created_at)
        first_comment_created_at = sorted_comments[0].created_at

        # Write a row of data to the CSV file
        writer.writerow({
            'Pull Request Number': pr.number,
            'Pull Request Name': pr_name,
            'Number of Comments': comments.totalCount,
            'Created At': created,
            'Updated At': updated,
            'Merge Time': merge_time,
            'Time Between': time_between,
            'First Comment Created At': first_comment_created_at
        })
print("CSV file 'pull_requests.csv' has been created.")
