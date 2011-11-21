#!/usr/bin/python26
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

import web
import app.controllers
import config
import mimetypes

from config import htmlview
import markdown2

# controller for Markdown pages:
class PageClassTemplate:
	content_file = ""

	def GET(self):
		html = markdown2.markdown_path(self.content_file)
		return htmlview.page(html)

# controller for static files
class Public:
    def GET(self):
        try:
            file_name = web.ctx.path.split('/')[-1]
            web.header('Content-type', mime_type(file_name))
            return open('.' + web.ctx.path, 'rb').read()
        except IOError:
            raise web.notfound()

# mime type interpreter
def mime_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

myApp = web.application(mapping=(), fvars=globals())


for page in config.pages:
	if not page.has_key("content_file"):
		continue
	pattern = page["link"]
	globals()[page["name"]] = type(page["name"],(PageClassTemplate,object,), dict(content_file=page["content_file"]))
	myApp.add_mapping(pattern, page["name"])

# add static file handler:
try:
	if config.static_dir:
		myApp.add_mapping("/%s/.+" % config.static_dir, "Public")
except AttributeError:
	pass

# add custom pages:
for pattern, controller in config.custom_pages:
	myApp.add_mapping(pattern, controller)

if __name__ == "__main__":
    myApp.run()
