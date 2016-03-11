Title: Setting up Pelican to create va.nce.me
Modified: 2016-06-06 15:00
Tags: python, pelican, publishing
Summary: A basic guide to setting up the development environment for [va.nce.me](http://va.nce.me/)

### Creating the Dev environment

[Pelican](http://docs.getpelican.com/) is a tool that allows the generation of static websites from [markdown](https://daringfireball.net/projects/markdown/) files.  It is written in [Python](https://www.python.org/) and there are many extensions.  It provides some basic themes as part of the install, but there are many other [contributed themes](http://www.pelicanthemes.com/) that you can use as-is or as a starting point to develop your own.  In future articles I will cover the development of the site theme, but this article covers the installation of the dev environment.

#### The Python environment

I am working on OS X and the links and details provided will relate to that, but it is obviously at home on linux.  If you are a linux user I am sure you can pick your way through my examples or find similar articles for linux.

* [Install python on OS X](http://docs.python-guide.org/en/latest/starting/install/osx/) using [homebrew](http://brew.sh/)
* Install [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref) for python to maintain a cleaner python environment on your machine and allow conflicting libraries across different projects.  I also use `virtualenvwrapper` which is also documented on [this page](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref).

#### Pelican

Setup a virtual environment for pelican

``` shell
$ mkvirtualenv pelican
$ workon pelican
(pelican) $
```

Follow the [pelican quickstart guide](http://docs.getpelican.com/en/3.6.3/install.html) to install pelican in the virtual environment we have just created, and initialise the website as a pelican project.

``` shell
(pelican) $ pip install pelican
(pelican) $ pip install markdown
(pelican) $ cd <your-desired-directory>
(pelican) $ pelican-quickstart
```
