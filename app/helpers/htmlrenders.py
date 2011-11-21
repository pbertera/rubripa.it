#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

def render_uff(ufficio):
    ret = "<table width=\"80%\" class=\"pa\">"
    ret = ret + "<tr><th colspan=\"2\"><h4>" + str(ufficio['description']) + "</h4></th></tr>"
    for k in ufficio:
        if ufficio[k] == None:
            continue
        elif k == "aooRef":
            ret = ret + "<tr><td><b>Aoo</b></td><td><a href=\"/aoo-search.html?codaoo="+str(ufficio[k])+"\">"+str(ufficio[k])+"</a><br /></td></tr>"
        else:
            ret = ret + "<tr><td><b>" + str(k) + "</b></td>" + "<td>" + str(ufficio[k])
    ret = ret + "</td></tr></table>"
    return ret

def render_pa(pa):
    ret = "<table width=\"80%\" class=\"pa\">"
    ret = ret + "<tr><th colspan=\"2\"><h4>"+ str(pa['description'])+"</h4></th></tr>"
    for k in pa:
        if pa[k] == None:
            continue
        elif k == "servizi":
			ret = ret + render_servizi_row(pa[k])
        else:
            ret = ret + "<tr><td><b>" + str(k) + "</b></td>" + "<td>" + str(pa[k]) + "</td></tr>"
    ret = ret + "</table>"
    return ret
   
def render_aoo(aoo):
    ret = "<table width=\"80%\" class=\"pa\">"
    ret = ret + "<tr><th colspan=\"2\"><h4>"+str(aoo['description'])+"</h4></th></tr>"
    for k in aoo:
        if aoo[k] == None:
            continue
        elif k == "codiceUff":
            for coduff in aoo[k]:
                ret = ret + "<tr><td><b>Uffici</b></td><td><a href=\"/uff-search.html?coduff="+str(coduff)+"\">"+str(coduff)+"</a><br /></td></tr>"
		elif k == "servizi":
			ret = ret + render_servizi_row(aoo[k])
		else:
            ret = ret + "<tr><td><b>" + str(k) + "</b></td>" + "<td>" + str(aoo[k]) + "</td></tr>"
    ret = ret + "</table>"
    return ret

def render_servizi_row(servizi):
	ret = "<tr><td><b>servizi</b><td><table width=\"90%\" class=\"servizi\">"
	for nome_servizio in servizi:
		ret = ret + "<tr><td><b>"+str(nome_servizio)+"</b></td>"
		ret = ret + "<td>"
		for att in servizi[nome_servizio]:
			ret = ret + "<b>"+ str(att) + "</b>: "+str(servizi[nome_servizio][att])+"<br/>"
		ret = ret + "</td>"
		ret = ret + "</tr>"
	ret = ret + "</table></td></tr>"
	return ret
