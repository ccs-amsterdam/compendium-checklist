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
What this basically says is, "<em>Hey, we noticed you created a new file called</em> <code>mytext.txt</code><em>, but unless you use the</em> <code>git add</code> <em>command we aren't going to do anything with it</em>."

#### An interlude: The staging environment, the commit, and you

One of the most confusing parts when you're first learning git is the concept of the staging environment and how it relates to a commit.

A commit is a record of what files you have changed since the last time you made a commit. Essentially, you make changes to your repo (for example, adding a file or modifying one) and then tell git to put those files into a commit.

Commits make up the essence of your project and allow you to go back to the state of a project at any point.

So, how do you tell git which files to put into a commit? This is where the staging environment or index come in. As seen in Step 2, when you make changes to your repo, git notices that a file has changed but won't do anything with it (like adding it in a commit).

To add a file to a commit, you first need to add it to the staging environment. To do this, you can use the git add <filename> command (see Step 3 below).

Once you've used the git add command to add all the files you want to the staging environment, you can then tell git to package them into a commit using the git commit command.

Note: The staging environment, also called 'staging', is the new preferred term for this, but you can also see it referred to as the 'index'.

<h3 id="step4">4. Add a file to the staging environment</h3>

<h3 id="step5">5. Create a commit</h3>

<h3 id="step6">6. Create a new branch</h3>


<h3 id="step7">7. Create a new repository on GitHub</h3>
