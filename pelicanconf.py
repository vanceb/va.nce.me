#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Core site details
AUTHOR = u'Vance'
SITENAME = u'va.nce.me'
SITEURL = 'http://va.nce.me'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Define some project paths that have special meanings in Pelican
PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']

# Internationalization settings
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Gather as much metadata as possible from the file system
USE_FOLDER_AS_CATEGORY = True
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
DEFAULT_DATE = 'fs'
# Set some defaults§
DEFAULT_CATEGORY = 'ramblings'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_PAGINATION = 10

# Theme
THEME = "themes/pure-single"
COVER_IMG_URL = '/images/sidebar.jpg'
TAGLINE = "Man of few words..."
# Configure the site menu
# Fixed menu entries
MENUITEMS = [
    ('Archives', '/archives.html')
]
# Dynamic menu entries§
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/geospaced'),
          ('github', "https://github.com/vanceb")
          )
