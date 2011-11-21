#!/usr/bin/python26
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

import web
import app.controllers

urls = (
	# html stuff
    '/', 'app.controllers.webpages.Index',
    '/rubripa\.html', 'app.controllers.webpages.Rubripa',
    '/search-menu\.html', 'app.controllers.searchmenu.HtmlMenu',
	'/api.html', 'app.controllers.webpages.Api',	
	'/faq.html', 'app.controllers.webpages.Faq',	
	'/rubripa4snom.html', 'app.controllers.webpages.Rubripa4snom',
	'/info.html', 'app.controllers.webpages.Info',

	# Search forms	
    '/simple-search-form\.html', 'app.controllers.simplesearchform.HtmlSimpleSearchForm',
  	'/advanced-search-form\.html',	 'app.controllers.advancedsearchform.HtmlAdvancedSearchForm',
  	'/dn-search-form\.html',	 'app.controllers.dnsearchform.HtmlDnSearchForm',

	# Search results
    '/simple-search\.html',        'app.controllers.search.HtmlSimpleSearch',
    '/advanced-search\.html',      'app.controllers.search.HtmlAdvancedSearch',
    '/dn-search\.html',   		'app.controllers.search.HtmlDnSearch',
	
	# html renders 
    '/uff-search\.html',         'app.controllers.search.HtmlUffSearch',
    '/aoo-search\.html',         'app.controllers.search.HtmlAooSearch',
    '/pa-search\.html',      	 'app.controllers.search.HtmlPaSearch',

    # static files
    '/public/.+',           'app.controllers.public.public',

    # Backend URLS
    '/dn-search',   		'app.controllers.search.DnSearch',
    '/advanced-search',   	'app.controllers.search.AdvancedSearch',
    '/simple-search',   'app.controllers.search.SimpleSearch',
    '/uff-search',      'app.controllers.search.UffSearch',
    '/aoo-search',      'app.controllers.search.AooSearch',
    '/pa-search',       'app.controllers.search.PaSearch'
)

myApp = web.application(urls, globals())

if __name__ == "__main__":
    myApp.run()
