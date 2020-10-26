## Automating Reproducible Science

In a very simple and straightforward research setup, you may have a dataset that is already in exactly the desired format, you have a very straightforward analysis consisting of a simple script, and the only output you care about is some statistic said script produces. Then, to reproduce your research, all you'd need to do is to run that script.

Unfortunately, many research projects involve more steps. Maybe you have to first install some uncommon software libraries, combine data from multiple sources, and run some preprocessing scripts that produce an intermediate dataset, that then is analyzed by several anaysis scripts. Maybe the output of these scripts has then to be processed in some way or anoyher, and maybe your scripts are even written in different languages. Maybe you cannot publicly share your raw data, but others could reproduce your analysis on an aggregate intermediate file. As you can imagine, this becomes complex really quickly...

<img src="figures/doit_xkcd.png"
     style="width:40%" />
     
You could, of course, simply write a short instruction file in which you outline to any reader (including your future self) what needs to be done in which order, and how to do that. But rather than instructing the researcher, why don't we instruct the computer to take the correct steps? In other words, *let's automate the reproduction process*

There are several ways of doing this, such as [shell scripts](https://en.wikipedia.org/wiki/Shell_script) on Linux and MacOS or [batch files](https://en.wikipedia.org/wiki/Batch_file) on Windows. Advanced users of Linux may also have heard of [GNU Makefiles](https://en.wikipedia.org/wiki/Batch_file), which allow to specify, for instance, how to run a series of commands depending on things like the configuration of the system. This is an important point: We want our research to be replicable no matter what specific computer system someone uses. 

### Just `doit`

The compendium uses a system called [doit](https://pydoit.org/), which is based on Python.
Fortunately, python is now preinstalled on almost all computers, so that's one less worry.

Using `doit`, you define the instructions for reproducing your results as a set of **tasks** and their **dependencies**. 
For example, suppose that to reproduce your analysis we would have to install R and certain packages (with their correct versions); then download and clean a data set; and finally run a substantive analysis for a paper or report. 
With `doit`, each of those steps is a single **task**, and the system is smart enough that it does not e.g. re-download a data set if it is already present. 

As a *compendium user*, this is essentially all you need to know: You can just download the compendium and run `doit`, 
and it will automatically take all steps needed to reproduce the research. 
However, [using_dodo]() will take you through these steps with an example project. 

As *compendium creator*, we provide a python module [compendium-dodo](https://github.com/vanatteveldt/compendium-dodo) 
to make it as easy as possible for you to get started with your reproducible research compendium.
In short, `compendium-dodo` will initialize your compendium with the correct folders,
and automatically create the `dodo.py` file that chains together the steps in your research.
Please see [using dodod](https://github.com/ccs-amsterdam/compendium-dodo/blob/main/README.md) for more information.
