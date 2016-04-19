#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colegio Salesiano San Isidro de la Orotava'
SITENAME = u'Cross Maria Auxiliadora'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Atlantic/Canary'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Salesianos La Orotava', 'http://www.salesianos-laorotava.com/'),
    ('Ayuntamiento de La Orotava', 'http://www.villadelaorotava.org/'),
    ('Cabildo de Tenerife', 'http://www.cabtfe.es/'),
    ('Gobierno de Canarias', 'http://www.deportecanario.com/'),
)

# Social widget
SOCIAL = (
    ('<i class=\'fa fa-twitter\'></i> Siguenos en twitter', 'https://twitter.com/CrossMauxi'),
    ('<i class=\'fa fa-facebook\'></i> Estamos en facebook', 'http://es-es.facebook.com/pages/CROSS-MARIA-AUXILIADORA/101320243244134'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = "cosmo"

PAGE_ORDER_BY = 'order'
