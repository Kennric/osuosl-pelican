#!/usr/bin/env python
# -*- coding: utf-8 -*- #


# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *  # noqa

SITEURL = os.getenv('PELICAN_SITE_URL', 'https://osuosl.org')
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
