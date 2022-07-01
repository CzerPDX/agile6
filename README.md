# agile6
Agile class group 6 repo

Group 6 members (add your name when you have access):
Brooke Czerwinski
Nicholas Muller
Jake Strong


Note from Brooke: I'm no expert in git, so if there are improvements to this method we can implement, let's fix it up!

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


When you start programming always begin by typing:
        git pull origin main

This will make sure that you're always up to date. You may need to merge and resolve conflicts within your IDE when you do this, but doing they will always need to be resolved and this method will make those conflicts smaller and more manageable.

When you want to push
1. Add the files you want to push (below command will add everything but you can add specific ones instead if you want)
        git add . 
2. Make a commit with a message
        git commit -m 'your message for commit'
3. Push changes
        git push
4. Make a pull request as above in the getting started section
