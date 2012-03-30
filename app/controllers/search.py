#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

from app.models import indicePA
import web
import json
import config
from config import htmlview
from config import indice_pa_max_res

IPA = indicePA.IndicePA(max_results=config.indice_pa_max_res,\
	indice_pa_uri=config.indice_pa_uri,\
	indice_pa_base=config.indice_pa_base,\
	indice_pa_bind_dn=config.indice_pa_bind_dn,\
	indice_pa_bind_pw=config.indice_pa_bind_pw)
#IPA = indicePA.IndicePA(max_results=config.indice_pa_max_res)

class AbstractAdvancedSearch:
    def JsonPOST(self):
        return self.GET()

    def JsonGET(self):
		user_data = web.input(tipo=[])
        try:
			r = IPA.advanced_search(user_data)
            return json.dumps(r, cls=indicePA.IpaJsonEncoder, indent=4)
        except Exception, e:
            web.internalerror()
            return json.dumps([{"Message": "Error occured: %s" % e}])
    
class AdvancedSearch(AbstractAdvancedSearch):
    def GET(self):
        return self.JsonGET()

    def POST(self):
        return self.JsonPOST()

class HtmlAdvancedSearch(AbstractAdvancedSearch):
    def GET(self):
        results =json.loads(self.JsonGET())
        if web.ctx.status.split(' ')[0] != "200":
            return htmlview.error(results)
        return htmlview.searchResult(results)

class AbstractDnSearch:
    def JsonPOST(self):
        return self.GET()

    def JsonGET(self):
		user_data = web.input(dn="")
        try:
			r = IPA.dn_search(user_data["dn"])
            return json.dumps(r, cls=indicePA.IpaJsonEncoder, indent=4)
        except Exception, e:
            web.internalerror()
            return json.dumps([{"Message": "Error occured: %s" % e}])
    
class DnSearch(AbstractDnSearch):
    def GET(self):
        return self.JsonGET()

    def POST(self):
        return self.JsonPOST()

class HtmlDnSearch(AbstractDnSearch):
    def GET(self):
        results =json.loads(self.JsonGET())
        if web.ctx.status.split(' ')[0] != "200":
            return htmlview.error(results)
        return htmlview.searchResult(results)

class AbstractSimpleSearch:
    def JsonPOST(self):
        return self.GET()

    def JsonGET(self):
        user_data = web.input(q="")
        if user_data["q"] == "":
            web.badrequest()
            return json.dumps([{"Message": "'q' parameter empty"}])
        try:
            r = IPA.simple_search(user_data['q'])
            return json.dumps(r, cls=indicePA.IpaJsonEncoder, indent=4)
        except Exception, e:
            web.internalerror()
            return json.dumps([{"Message": "Error occured: %s" % e}])
    
class SimpleSearch(AbstractSimpleSearch):
    def GET(self):
        return self.JsonGET()

    def POST(self):
        return self.JsonPOST()

class HtmlSimpleSearch(AbstractSimpleSearch):
    def GET(self):
        results =json.loads(self.JsonGET())
        if web.ctx.status.split(' ')[0] != "200":
            return htmlview.error(results)
        return htmlview.searchResult(results)

class AbstractUffSearch:
    def JsonPOST(self):
        return self.GET()

    def JsonGET(self):
        user_data = web.input(coduff="")
        if user_data["coduff"] == "":
            web.badrequest()
            return json.dumps([{"Message": "'coduff' parameter empty"}])
        try:
            r = IPA.search_cod_uff(user_data['coduff'])
            return json.dumps(r, cls=indicePA.IpaJsonEncoder, indent=4)
        except Exception, e:
            web.internalerror()
            return json.dumps([{"Message": "Error occured: %s" % e}])

class UffSearch(AbstractUffSearch):
    def GET(self):
        return self.JsonGET()

    def POST(self):
        return self.JsonPOST()

class HtmlUffSearch(AbstractUffSearch):
    def GET(self):
        results =json.loads(self.JsonGET())
        if web.ctx.status.split(' ')[0] != "200":
            return htmlview.error(results)
        return htmlview.uffSearch(results)

class AbstractAooSearch:
    def JsonPOST(self):
        return self.GET()

    def JsonGET(self):
        user_data = web.input(codaoo="")
        if user_data["codaoo"] == "":
            web.badrequest()
            return json.dumps([{"Message": "'codaoo' parameter empty"}])
        try:
            r = IPA.search_cod_aoo(user_data['codaoo'])
            return json.dumps(r, cls=indicePA.IpaJsonEncoder, indent=4)
        except Exception, e:
            web.internalerror()
            return json.dumps([{"Message": "Error occured: %s" % e}])

class AooSearch(AbstractAooSearch):
    def GET(self):
        return self.JsonGET()

    def POST(self):
        return self.JsonPOST()

class HtmlAooSearch(AbstractAooSearch):
    def GET(self):
        results =json.loads(self.JsonGET())
        if web.ctx.status.split(' ')[0] != "200":
            return htmlview.error(results)
        return htmlview.aooSearch(results)

class AbstractPaSearch:
    def JsonPOST(self):
        return self.GET()

    def JsonGET(self):
        user_data = web.input(codpa="")
        if user_data["codpa"] == "":
            web.badrequest()
            return json.dumps([{"Message": "'codpa' parameter empty"}])
        try:
            r = IPA.search_cod_pa(user_data['codpa'])
            return json.dumps(r, cls=indicePA.IpaJsonEncoder, indent=4)
        except Exception, e:
            web.internalerror()
            return json.dumps([{"Message": "Error occured: %s" % e}])

class PaSearch(AbstractPaSearch):
    def GET(self):
        return self.JsonGET()

    def POST(self):
        return self.JsonPOST()

class HtmlPaSearch(AbstractPaSearch):
    def GET(self):
        results =json.loads(self.JsonGET())
        if web.ctx.status.split(' ')[0] != "200":
            return htmlview.error(results)
        return htmlview.paSearch(results)
