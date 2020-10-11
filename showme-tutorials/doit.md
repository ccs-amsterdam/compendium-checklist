## What is `doit`?

<img src="figures/doit_xkcd.png"
     style="width:40%" />


In a very simple and straightforward research setup, you may have a dataset that is already in exactly the desired format, you have a very straightforward analysis consisting of a simple script, and the only output you care about is some statistic said script produces. Then, to reproduce your research, all you'd need to do is to run that script.

Unfortunately, many research projects involve more steps. Maybe you have to first install some uncommon software libraries, then decrypt your data, then run some preprocessing scripts that produce an intermediate dataset, that then is analyzed by several anaysis scripts. Maybe the output of these scripts has then to be processed in some way or anoyher, and maybe your scripts are even written in different languages. You could, of course, simply write a short instruction file in which you outline to any reader (including your future self) what needs to be done in which order, and how to do that.

This can be automated.

There are several ways of doing this, such as [shell scripts](https://en.wikipedia.org/wiki/Shell_script) on Linux and MacOS or [batch files](https://en.wikipedia.org/wiki/Batch_file) on Windows. Advanced users of Linux may also have heard of [GNU Makefiles](https://en.wikipedia.org/wiki/Batch_file), which allow to specify, for instance, how to run a series of commands depending on things like the configuration of the system. This is an important point: We want our research to be replicable no matter what specific computer system someone uses. 

`doit` takes this idea a step further: It does not depend on tools like GNU Make and works on all operating systems. It only requires Python to be installed -- and currently, all recent versions of all major operating systems ship with Python preinstalled, even though as an end user, you may not be aware of that.


### General idea

The general idea of `doit` is to define *tasks* (such as installing dependices, running an analysis, etc.) in a file called `dodo.py`. This file -- which, for those who know GNU Make, can be seen as a Makefile -- defines how to run these tasks. The user therefore does not need to remember the exact steps that need to be done, but can simply run `doit` which will exectute the tasks defined in `dodo.py`. Alternatively, the user can also run `doit help` and `doit list` to get information on how to get more control and excecute, for instance, only specific tasks.



### `doit` and the Standardized Research Compendium

In the standardized research compendium, you do not need to write a `dodo.py` file yourself. We already did this for you. 

As a *user* (i.e., if you want to reproduce someone else's compendium), just run `doit`. That's all, everything will be handled for you.
If you use our recommended folder structure, you can

As a *developer* (i.e., if you want to create a compendium), ...
# ***************
# TODO ADD SPECIFICS ONCE DODO.PY IS FINSIHED. E.G., ABOUT ENCRYPTION AND DECRYPTION
# **************




### More `doit`

If you want to learn more about `doit`, have a look at the official [tutorial](https://pydoit.org/contents.html)
