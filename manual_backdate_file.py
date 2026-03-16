import os
import datetime
import time

# File to modify (so commits have changes)
FILE_NAME = "app.py"

# Number of commits you want
NUM_COMMITS = 5

# Start date (past)
start_date = datetime.datetime(2024, 1, 1, 9, 0, 0)

for i in range(NUM_COMMITS):
    # Create a new date for each commit
    commit_date = start_date + datetime.timedelta(days=i*2)

    # Make a small change to file
    with open(FILE_NAME, "a") as f:
        f.write(f"# Update {i} at {formatted_date}\n")

    # Stage file
    os.system("git add .")

    # Commit with backdated time
    command = f'''
    GIT_AUTHOR_DATE="{formatted_date}" GIT_COMMITTER_DATE="{formatted_date}" git commit -m "Update {i}"
    '''




