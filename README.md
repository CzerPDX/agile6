# agile6
Agile class group 6 repo

Group 6 members (add your name when you have access):
Brooke Czerwinski
Nicholas Muller
Jake Strong
John Pham

Note from Brooke: I'm no expert in git, so if there are improvements to this method we can implement, let's fix it up!


# For every user story card:

1. **Go to the main repo and create a new branch**<br>
    - https://github.com/CzerPDX/agile6/branches

2. **Switch to your branch on the Linux server**
    - git pull
    - git checkout [BRANCH NAME]

3. **Check that you're on the new branch**
    - git branch

4. **Make your changes**

5. **Push your changes to your branch**
    - git add .
    - git commit -m 'message describing commit'
    - git push

<hr>

## When you finish working on a user story
merge your branch with staging and delete it

1. **Submit a PR between staging and your branch**
    - go to the main repo https://github.com/CzerPDX/agile6
    - There should be a "Compare & pull request" button. 
      - Click it if it's there
      - If it's not there
        - Click "pull requests" at the top under the repo name
        - Click the green "New pull request" button on the right
    - For the left dropdown, choose staging
    - For the right dropdown, choose your branch you created
    - Then click "create pull request"
    - Then click "create pull request" again lol
    - It will check to see if it can be merged.
      - If it can, click "squash and merge"
      - If it can't
        - Resolve the conflicts
        - Then click "squash and merge"
    - Delete the branch
      - Where it says "Pull request successfully merged" and "branch can be safely deleted" click "delete branch"
      

<hr>

## To compile project:
$ python3 ftp-client.py
<br><br>

<hr>

## Testing with pytest
- Create a matching test file for each .py file you add to the project
    - **Test File Names**: "[original file name]_test.py"
- Create a test function for every test case
    - **Test Function Names**: "test_[original function name]_test_description"
- **File includes**
    - include pytest
        - test library
    - include os
        - For getting environment variables
- **To run pytest**
    - $ pytest