## Intro to Git and Github for Beginners

<img src="figures/git_xkcd.png"
     style="width:40%" />

This tutorial guides you through the first steps to find your way on GitHub.
Follow the steps below to get comfortable making changes to the code base, opening up a pull request (PR), and merging code into the primary branch. Any important git and GitHub terms are in bold with links to the official git reference materials.
<ol>
  <li> <a href="#step1">Install git and create a GitHub account</a> </li>
  <li> <a href="#step2">Create a local git repository </a></li>
  <li> <a href="#step3">Add a new file to the repo </a></li>
  <li> <a href="#step4">Add a file to the staging environment </a></li>
  <li> <a href="#step5">Create a commit </a></li>
  <li> <a href="#step6">Create a new branch </a></li>
  <li> <a href="#step7">Create a new repository on GitHub </a></li>
  <li> <a href="#step8">Push a branch to GitHub </a></li>
  <li> <a href="#step9">Create a Pull Request (PR)</a></li>
  <li> <a href="#step10">Merge a PR</a></li>
  <li> <a href="#step11">Get changes on GitHub back to your computer</a></li>
  <li><a href="#step12">Bask in your git glory</a></li>
</ol>

<h3 id="step1">1. Install git and create a GitHub account</h3>
To start, (a) install git, and (b) create a free Github account. <br> <br>

<strong>(a) Installing git </strong><br>
For this tutorial, we recommend to use the command line:
<ul>
  <li> For Windows users, ...  </li>
  <li> For Mac users, use <em>Finder</em> to search for <em>Terminal</em> in the <em>Applications</em>. </li>
  <li> For Linux users,  ... </li>
</ul>
The instructions to install git are documented <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git" target="_blank">here</a>. <br> <br>

<strong>(b) Free GitHub account </strong><br>
Once you have installed git on your computer, create a GitHub account <a href="https://github.com/" target="_blank">here</a>.
(GitHub has <a href="https://docs.github.com/en/free-pro-team@latest/github/teaching-and-learning-with-github-education/applying-for-an-educator-or-researcher-discount" target="_blank">special accounts</a> for academic researchers.)

<h3 id="step2">2. Create a local git repository</h3>
When you want to create a new project -- ideally when you are at the start of a research project -- on your local machine (that is, your personal computer), you first have to create a new repository (or often, '<b>repo</b>', for short).
The instructions how to create a new repo can be found <a href="https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository" target="_blank">here</a>. <br> <br>


To begin, open up a terminal and go to the place on your local machine where you want to place your project.
To change directories, you use the <code>cd</code> command.
For example, if you have a 'projects' folder on your desktop, you do something like:

```shell
joetheplumber:Desktop joetheplumber$ cd ~/Desktop
joetheplumber:Desktop joetheplumber$ mkdir myproject
joetheplumber:Desktop joetheplumber$ cd myproject/
```

To connect (initialize) a git repository in the root of the folder, run the <a href="https://git-scm.com/docs/git-init" target="_blank"><code>git init</code></a> command:  

```shell
joetheplumber:myproject joetheplumber$ git init
Initialized empty Git repository in /Users/joetheplumber/Desktop/myproject/.git/
```

<h3 id="step3">3. Add a new file to the repo</h3>
When your project on your local machine is connected to the online git repository, you can start adding files to your project.
This can be done using any text editor you like, or by running a <a href="https://linux.die.net/man/1/touch" target="_blank"><code>touch</code></a> command:

```shell
joetheplumber:myproject mnelson$ touch mytext.txt
joetheplumber:myproject joetheplumber$ ls
mytext.txt
```

When you add or modify files in a folder containing a git repo, git will notice that changes have been made inside the repo.
But, git <strong>will not </strong> officially keep track of the file.
That is, <strong> git will not save it,</strong>, or more precisely put it in a <code>commit</code> -- more about commits next -- unless you explicitly tell git to keep track of your changes.

After creating the new file, you can use the <a href="https://git-scm.com/docs/git-status" target="_blank"><code>git status</code></a> command to see which files git know exist.

```shell
joetheplumber:myproject joetheplumber$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	mytext.txt

nothing added to commit but untracked files present (use "git add" to track)
```
What this basically says is, "<em>Hey, we noticed you created a new file called "mytext.txt", but unless you use the</em> <code>git add</code> <em>command we aren't going to do anything with it</em>."

If you want git to save the changes you made to your repo, you need the <code><a href="https://git-scm.com/docs/git-add" target="_blank"> git add</a> [filename]</code> command (see <a href="#step3">Step 3</a> below).
This process is called the <em><a href="https://git-scm.com/book/en/v2" target="_blank">staging environment</a></em>.
This is also called 'staging', the new preferred term for this, but you can also see it referred to as the 'index'.
Once you've used the <code>git add</code> command to add all the files you want to the staging environment, you can then tell git to package them into a commit using the <code>git commit</code> command.
A <a href="https://git-scm.com/docs/git-commit" target="_blank">commit</a> is a record of what files you have changed since the last time you made a commit.
Essentially, you make changes to your repo (for example, adding a file or modifying one) and then tell git to put those files into a commit.
Commits make up the essence of your project and allow you to go back to the state of a project at any point.

<h3 id="step4">4. Add a file to the staging environment</h3>
Add a file to the staging environment using the <code>git add</code> command.

If you rerun the <code>git status</code> command, you will see that git has added the file to the staging environment (notice the "Changes to be committed" line).  

```shell
joetheplumber:myproject joetheplumber$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   mytext.txt
```

To reiterate, the file has <strong>not</strong> yet been added to a commit, but it's about to be.

<h3 id="step5">5. Create a commit</h3>
It's time to create your first commit!

Run the command <code>git commit -m "Your message about the commit"</code>

```shell
joetheplumber:myproject joetheplumber$ git commit -m "This is my first commit!"
[master (root-commit) b345d9a] This is my first commit!
 1 file changed, 1 insertion(+)
 create mode 100644 mytext.txt
```

The message at the end of the commit should be something related to what the commit contains - maybe it's a new feature, maybe it's a bug fix, maybe it's just fixing a typo.
Don't put a message like "<em>asdfadsf</em>" or "<em>foobar</em>".
That makes the other people who see your commit sad.
Very, very, sad.

<h3 id="step6">6. Create a new branch</h3>

What if you want to try out some code, and you do not want to make changes to the main project, until you know the new code is running?
This is where <a href="https://git-scm.com/docs/git-branch" target="_blank"><code>git branch</code></a> come in.

Branches allow you to move back and forth between 'states' of a project. For instance, if you want to add a new page to your website you can create a new branch just for that page without affecting the main part of the project.
Once you're done with the page, you can <a href="https://git-scm.com/docs/git-merge" target="_blank">merge</a> your changes from your branch into the primary branch.
When you create a new branch, Git keeps track of which commit your branch 'branched' off of, so it knows the history behind all the files.

Let's say you are on the primary branch and want to create a new branch to develop your web page.
Here's what you'll do: <a href="https://git-scm.com/docs/git-checkout" target="_blank"><code>Run git checkout -b [my branch name]</code></a>. This command will automatically create a new branch and then 'check you out' on it, meaning git will move you to that branch, off of the primary (master) branch.

After running the above command, you can use the <a href="https://git-scm.com/docs/git-branch" target="_blank"><code>git branch</code></a> command to confirm that your branch was created:

```shell
joetheplumber:myproject joetheplumber$ git branch
  master
* my-new-branch
```

The branch name with the asterisk next to it indicates which branch you're pointed to at that given time.

Now, if you switch back to the primary branch and make some more commits, your new branch won't see any of those changes until you <a href="https://git-scm.com/docs/git-merge" target="_blank">merge</a> those changes onto your new branch.

<h3 id="step7">7. Create a new repository on GitHub</h3>

If you only want to keep track of your code locally, you don't need to use GitHub. But if you want to work with a team, you can use GitHub to collaboratively modify the project's code.

To create a new repo on GitHub, log in and go to the GitHub home page. You should see a green '+ New repository' button:

[add screenshot via ccs github]

After clicking the button, GitHub will ask you to name your repo and provide a brief description:

[add screenshot via ccs github]

When you're done filling out the information, press the 'Create repository' button to make your new repo.

GitHub will ask if you want to create a new repo from scratch or if you want to add a repo you have created locally.
In this case, since we've already created a new repo locally, we want to push that onto GitHub so follow the <strong>'....or push an existing repository from the command line'</strong> section:

```shell
joetheplumber:myproject joetheplumber$ git remote add origin https://github.com/ccs-amsterdam/mynewrepository.git
joetheplumber:joetheplumber joetheplumber$ git push -u origin master
Counting objects: 3, done.
Writing objects: 100% (3/3), 263 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/ccs-amsterdam/mynewrepository.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

(You'll want to change the URL in the first command line to what GitHub lists in this section since your GitHub username and repo name are different.)

<h3 id="step8">8. Push a branch to GitHub</h3>
Now we will <a href="https://git-scm.com/docs/git-push" target="_blank">push</a> the commit in your branch to your new GitHub repo.
This allows other people to see the changes you've made. If they're approved by the repository's owner, the changes can then be merged into the primary branch.

To push changes onto a new branch on GitHub, you'll want to run <code>git push origin yourbranchname</code>. GitHub will automatically create the branch for you on the remote repository:

```shell
joetheplumber:myproject joetheplumber$ git push origin my-new-branch
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 313 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/ccs-amsterdam/mynewrepository.git
 * [new branch]      my-new-branch -> my-new-branch
```

You might be wondering what that "origin" word means in the command above.
What happens is that when you clone a remote repository to your local machine, git creates an <strong>alias</strong> for you.
In nearly all cases this alias is called "<a href="https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes" target="_blank">origin</a>."
It's essentially shorthand for the remote repository's URL.
So, to push your changes to the remote repository, you could've used either the command: <code>git push git@github.com:git/git.git yourbranchname or git push origin yourbranchname</code>

(If this is your first time using GitHub locally, it might prompt you to log in with your GitHub username and password.)

If you refresh the GitHub page, you will see note saying a branch with your name has just been pushed into the repository.
You can also click the 'branches' link to see your branch listed there.

[add screenshot via ccs github]

Now click the green button in the screenshot above. We are going to make a <strong>pull request</strong>!

<h3 id="step9">9. Create a Pull Request (PR)</h3>

A pull request (or PR) is a way to alert a repo's owners that you want to make some changes to their code. It allows them to review the code and make sure it looks good before putting your changes on the primary branch.

This is what the PR page looks like before you've submitted it:

[add screenshot via ccs github]

And this is what it looks like once you've submitted the PR request:

[add screenshot via ccs github]

You might see a big green button at the bottom that says 'Merge pull request'. Clicking this means you'll merge your changes into the primary branch.

Note that this button won't always be green.
In some cases it'll be grey, which means you're faced with a <strong>merge conflict</strong>.
This is when there is a change in one file that conflicts with a change in another file and git can't figure out which version to use.
You'll have to manually go in and tell git which version to use.

Sometimes you'll be a co-owner or the sole owner of a repo, in which case you may not need to create a PR to merge your changes. However, it's still a good idea to make one so you can keep a more complete history of your updates and to make sure you always create a new branch when making changes.

<h3 id="step10">10. Merge a PR</h3>
Go ahead and click the green 'Merge pull request' button. This will merge your changes into the primary branch.

[add screenshot via ccs github]

When you're done, I recommend deleting your branch (too many branches can become messy), so hit that grey 'Delete branch' button as well.

You can double check that your commits were merged by clicking on the 'Commits' link on the first page of your new repo.

[add screenshot via ccs github]

This will show you a list of all the commits in that branch. You can see the one I just merged right up top (Merge pull request \#2).

[add screenshot via ccs github]

You can also see the <a href="https://git-scm.com/docs/git-hash-object" target="_blank">hash code</a> of the commit on the right hand side. A hash code is a unique identifier for that specific commit. It's useful for referring to specific commits and when undoing changes (use the <a href="https://git-scm.com/docs/git-revert" target="_blank"><code>git revert</a> [hash code number]</code> command to backtrack).

<h3 id="step11">11. Get changes on GitHub back to your computer</h3>
Right now, the repo on GitHub looks a little different than what you have on your local machine.
For example, the commit you made in your branch and merged into the primary branch doesn't exist in the primary branch on your local machine.

In order to get the most recent changes that you or others have merged on GitHub, use the <code>git pull origin master</code> command (when working on the primary branch).

```shell
joetheplumber:myproject joetheplumber$ git pull origin master
remote: Counting objects: 1, done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), done.
From https://github.com/ccs-amsterdam/mynewrepository
 * branch            master     -> FETCH_HEAD
   b345d9a..5381b7c  master     -> origin/master
Merge made by the 'recursive' strategy.
 mytext.txt | 1 +
 1 file changed, 1 insertion(+)
```

This shows you all the files that have changed and how they've changed.

Now we can use the <a href="https://git-scm.com/docs/git-log" target="_blank"><code>git log</code></a> command again to see all new commits.

(You may need to switch branches back to the primary branch. You can do that using the <code>git checkout master</code> command.)

```shell
joetheplumber:myproject joetheplumber$ git log
commit 3e270876db0e5ffd3e9bfc5edede89b64b83812c
Merge: 4f1cb17 5381b7c
Author: Joe the Plumber <joetheplumber@joetheplumber.com>
Date:   Fri Sep 11 17:48:11 2015 -0400

    Merge branch 'master' of https://github.com/ccs-amsterdam/mynewrepository

commit 4f1cb1798b6e6890da797f98383e6337df577c2a
Author: Joe the Plumber <joetheplumber@joetheplumber.com>
Date:   Fri Sep 11 17:48:00 2015 -0400

    added a new file

commit 5381b7c53212ca92151c743b4ed7dde07d9be3ce
Merge: b345d9a 1e8dc08
Author: Joe the Plumber <joetheplumber@joetheplumber.com>
Date:   Fri Sep 11 17:43:22 2015 -0400

    Merge pull request \#2 from ccs-amsterdam/my-newbranch

    Added some more text to my file

commit 1e8dc0830b4db8c93efd80479ea886264768520c
Author: Joe the Plumber <joetheplumber@joetheplumber.com>
Date:   Fri Sep 11 17:06:05 2015 -0400

    Added some more text to my file

commit b345d9a25353037afdeaa9fcaf9f330effd157f1
Author: Joe the Plumber <joetheplumber@joetheplumber.com>
Date:   Thu Sep 10 17:42:15 2015 -0400

    This is my first commit!
```
<h3 id="step12">12. Bask in your git glory</h3>

You've successfully made a PR and merged your code to the primary branch. Congratulations! If you'd like to dive a little deeper, check out the files in <a href="https://github.com/cubeton/git101/tree/master/TurtorialInfo" target="_blank">this Git101 folder</a> for even more tips and tricks on using git and GitHub.

### Reference
This tutorial is adapted from <a href="https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners" target="_blank">the tutorial</a> developed by <a href="https://product.hubspot.com/blog/author/meghan-nelson" target="_blank"><Meghan Nelson</a>
