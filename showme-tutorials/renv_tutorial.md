Using renv to make R code reproducible
================

# The renv package

The renv package is a powerful tool for managing packages in R by
creating reproducible environments. In this document we provide an
abbreviated introduction and tutorial for the specific use case of
creating documentation for R code in a research compendium.

In short, the renv package allows you to create a `lock` file for an R
project. This file documents the *project library*: the specific
versions of packages that you used in a project. By including this file
in the compendium, others can install the exact same packages and
versions. In other words, the lock file contains a `snapshot` of the
project library.

By including this lock file in the compendium, the environment can be
`restored` on a different system. This not only makes it easier to
install the required R packages, but also ensures that updates to
packages do not break the code or affect the outcome (for more details,
see the `why we need renv` section below). Also, the environment is
isolated, meaning that the packages are stored in a separate library.
This way, even if the compendium requires many outdated packages, users
can install the environment without having to worry about affecting
other projects on the same computer.

The following illustration shows an example of using `renv` for creating
reproducible code ![renv for reproducible
code](figures/renv_simplified.png)

In this example, an analysis was performed with a very old version of
the `lme4` (0.2-1). On the computer on which the code is replicated a
much newer version is installed (1.1-23). If only the code is shared,
the analysis might give different results, and perhaps not even work.

By taking a snapshot with the `renv` package, the project library that
was used for the original analysis is documented in the `lock file`.
Efficiently, only the packages that are actually used in the project are
included.

To replicate the analysis on a different computer, this library is
`restored` in a separate environment. The old version of `lme4` is
automatically downloaded from the CRAN repository archive. The code can
now be executed in this environment using the old lme4 package. Since
the environment is isolated, this does not affect the newer version that
was already on the computer.

``` r
install.packages('renv')
```

# Creating a lock file with renv

Creating a lock file is surprisingly easy, especially if your code is
contained in an [RStudio
project](https://support.rstudio.com/hc/en-us/articles/200526207-Using-Projects)
(which we strongly encourage). From within the project or working
directory, simply run the `snapshot()` function.

``` r
renv::snapshot()
```

You will now see a list of all packages that are used in the project or
working directory. When asked to proceed, enter `y` in the Console. This
will create the `renv.lock` file. If you open the lock file, you’ll see
that it documents the R version that you used and the list of packages.
Next to the package names, the package version, source (e.g.,
repository, GitHub), and hash are also reported.

# Restoring a lock file

By including the lock file in the compendium, others will know exactly
what packages they’ll need to run the code and where to find them. The
easiest way to install these packages, is to create an environment with
`renv` in which to `restore` this lock file.

If a project made a `renv` snapshot, it should be included in the main
folder. Make sure that you open an R project in this folder, or set this
folder as your working directory If you now run the `renv::restore()`
function, it will look for the lock file, and if it exists it will
automatically create the environment.

``` r
renv::restore()
```

This will automatically install the packages that you need. Also, it
**initializes** the environment. This means that when you execute R
code, it will use the isolated environment. If you install new packages,
they will also be installed in this environment. If you want to return
to the state documented in the lockfile, simply run `renv::restore()`
again.

If you return to the project (after closing it), you will have to
initialize the environment again. For this you simply use:

``` r
renv::activate()
```

# Other things to do with renv

In this brief tutorial we only discussed the bare essentials for using
`renv` to share and reproduce R code. However, you can also use `renv`
in your regular workflow. It is good practice to always use an isolated
environment for any larger project. By making snapshots at important
times, such as submitting a manuscript to a journal, you can always go
back to this state.

In this case, you will want to learn more about [how renv
works](https://rstudio.github.io/renv/articles/renv.html) and what
additional functions there are.

# Why we need renv

One of the benefits of R code is that it is by design relatively easy to
share. Any external packages that are used need to be explicitly
mentioned in the code. To execute the code, one simply needs to install
these packages, which is trivial as long as only packages from public
repositories such as CRAN are used. So you might wonder, do we really
need `renv` to document what packages are used? What could go wrong if I
only share my code?

The problem is that knowing only **what** packages are used is not very
reliable. R packages tend to change over time, so code that worked
before might no longer work, or might produce different output. To
ensure that an analysis is reproducible over a longer period of time, it
is key that the specific package **versions** are also documented.

Furthermore, it’s not sufficient to only specify the versions of the
packages that are explicitly mentioned in the code, because these
packages often *depend* on other packages. In other words, these
packages themselves import code from other packages. This means that you
would also need to document the versions of these *dependencies*, and
these might in turn have more dependencies. So in practice, even if you
use one external package in R, you might have to document the names and
versions of many packages.

When `renv::snapshot()` is executed, it will look for all R files in
your project, and find all packages that are used. It will then look up
all the dependencies of these packages, and report the versions of these
packages in your library. In other words, it makes a snapshot of your
library, but includes only the packages needed to execute the code in
your project.

Without `renv` it would be tedious, and quite complicated, to provide
this documentation. Moreover, it would be terrible to replicate older
code, because you would have to manually install and/or downgrade many
packages. If you do not work with different libraries, this could also
mean that you have to upgrade and downgrade packages whenever you move
between different projects.
