#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

import web
import config

from config import htmlview

class HtmlSimpleSearchForm:
    def GET(self):
        return htmlview.simpleSearchForm()

class HtmlAdvancedSearchForm:
    def GET(self):
        return htmlview.advancedSearchForm()

class HtmlDnSearchForm:
    def GET(self):
        return htmlview.dnSearchForm()
