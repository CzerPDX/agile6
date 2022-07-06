# agile6
Agile class group 6 repo

Group 6 members (add your name when you have access):
Brooke Czerwinski
Nicholas Muller
Jake Strong
John Pham

Note from Brooke: I'm no expert in git, so if there are improvements to this method we can implement, let's fix it up!


# For every user story card:

1. **Go to the main repo and create a new branch from staging (not main)**<br>
    - https://github.com/CzerPDX/agile6/branches

2. **Switch to your branch on the Linux server**
    - git checkout [BRANCH NAME]

3. **Check that you're on the new branch**
    - git branch

4. **Make your changes**

5. **Push your changes to your branch**
    - git add .
    - git commit -m 'message describing commit'
    - git push





To compile project:
$ python3 ftp-client.py

<hr>

### Old stuff below this line (ignore for now)


To get started
1. Make folder on linux server
2. Clone repo to the folder
        git clone https://github.com/CzerPDX/agile6.git
3. pull
        git pull
4. Switch to your branch
        git checkout [your first name lowercase]
5. Pull from origin
        git pull origin main
6. Open the README.md and add your name to the list
7. Add files
        git add .
7. Commit changes
        git commit -m 'quick message for commit'
8. Push changes
        git push
9. Create a pull request through the browser on github
        - Go to the "pull requests" tab in github: https://github.com/CzerPDX/agile6/compare/main...brooke
        - Under "comparing changes" choose "main" for the first dropdown and your repo for the second dropdown
        - Click "create pull request"
        - Click "create pull request" again
        - It will check for merge-ability here.
              - Resolve conflicts if necessary (edit the document as needed then click "mark as resolved" at the top left)
              - Commit merge
        - Click "Squash and Merge"
        - Click "Confirm Squash and Merge"

