## Intro to Git and Github for Beginners

<img src="figures/git_xkcd.png"
     style="float: center; width: 40%;" />

This tutorial guides you through the first steps to find your way on GitHub.
Follow the steps below to get comfortable making changes to the code base, opening up a pull request (PR), and merging code into the primary branch. Any important git and GitHub terms are in bold with links to the official git reference materials.
<ol>
  <li> Install git and create a GitHub account. </li>
  <li> Create a local git repository. </li>
  <li> Add a new file to the repo. </li>
  <li> Add a file to the staging environment. </li>
  <li> Create a commit. </li>
  <li> Create a new branch. </li>
  <li> Create a new repository on GitHub. </li>
</ol>

### 1. Install git and create a GitHub account
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

### 2. Create a local git repository
When you want to create a new project -- ideally when you are at the start of a research project -- on your local machine (that is, your personal computer), you first have to create a new repository (or often, '<mark>repo</mark>', for short).
The instructions how to create a new repo can be found <a href="https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository" target="_blank">here</a>. <br> <br>


To begin, open up a terminal and move to where you want to place the project on your local machine using the cd (change directory) command. For example, if you have a 'projects' folder on your desktop, you'd do something like:
```shell
jtheplumber:Desktop jtheplumber$ cd ~/Desktop
jtheplumber:Desktop jtheplumber$ mkdir myproject
jtheplumber:Desktop jtheplumber$ cd myproject/
```
