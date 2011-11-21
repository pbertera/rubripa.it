#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>


import web
import mimetypes

class public:
    def GET(self):
        try:
            file_name = web.ctx.path.split('/')[-1]
            web.header('Content-type', mime_type(file_name))
            return open('.' + web.ctx.path, 'rb').read()
        except IOError:
            raise web.notfound()
            
def mime_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream' 
