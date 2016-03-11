Title: Adding the photos plugin to my Pelican website
Tags: pelican, publishing
Summary: Adding the photos plugin to the Pelican site

## Pelican plugins

There is a collection of [Pelican plugins](https://github.com/getpelican/pelican-plugins) maintained on Github.  I followed the advice of their README and cloned the entire repository to my local machine.  To enable the [photos plugin](https://github.com/getpelican/pelican-plugins/tree/master/photos) I needed to install the Python Imaging Library (PIL) to allow the plugin to resize my photos as it was building the website.  Unfortunately when I tried to install using pip i got...

``` shell
pip install PIL
Collecting PIL
  Could not find a version that satisfies the requirement PIL (from versions: )
No matching distribution found for PIL
```

On further investigation it looks like [`pillow`](https://pillow.readthedocs.org/en/3.1.x/) is a maintained fork of `PIL`, so I installed that instead

``` shell
pip install pillow
```

## Configuring photos plugin

The [README](https://github.com/getpelican/pelican-plugins/tree/master/photos) for the plugin has good instructions on installing.  I followed these substituting my own paths and succeeded in getting the plugin to work.

One thing to note is that the plugin seems to ignore the `RELATIVE_URLS = True` setting in my config file, so I was unable to view the photos locally as the image links pointed at the uploaded location.
