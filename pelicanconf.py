#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vance'
SITENAME = u'va.nce.me'
#SITEURL = 'http://va.nce.me'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/geospaced'),
          ('github', "https://github.com/vanceb")
          )

# menu
MENUITEMS = [
    ('About', '/pages/about.html'),
    ('Archives', '/archives.html')
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Vance's settings
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'ramblings'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_DATE = 'fs'
PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']

# Theme
#THEME = 'pure-single'
THEME = "themes/pure-single"
COVER_IMG_URL = '/images/sidebar.jpg'
TAGLINE = "Man of few words..."
