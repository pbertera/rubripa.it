#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

import ldap
import ldap.resiter
import ldap.filter
import sys
import json
import pprint

indice_pa_uri = "ldap://indicepa.gov.it"
indice_pa_base = "c=it"


class IpaJsonEncoder(json.JSONEncoder):
    """Encoder for IpaObj Objects
    """
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

class IpaObj:
    """Abstract IndicePA Object.
    This class implements common code for IPA Objects (Pa, Aoo and Uo).
    """
    def __init__(self, dn, ldap_obj):
        self.dn = dn
        self._ldap_obj = ldap_obj
		self._public_attrs = ["tipo"]
		self.tipo = "abstract"
		#self._public_attrs = ["tipo"]
        
		self._parse_ldap_obj()

    def __repr__(self):
        ret = ''
        for att in self._public_attrs:
            ret = ret + "%s: %s\n" % (att, getattr(self,att))        
        return ret

    def reprJSON(self):
        ret = {}
		for att in self._public_attrs:
            ret[att] = getattr(self,att)
        return ret


    def _parse_ldap_obj(self):
        """This method must be implemented by concrete objects
        """
        print "NOT Implemented"
    
    def _get_from_ldap(self, attrName, single=True):
        """This function retreive content from private attribute _ldap_obj.
        If single param is false return a list, otherwise return a string.
        """
        try:
            if single == True:
                return self._ldap_obj[attrName][0]
            else:
                return self._ldap_obj[attrName]
        except KeyError:
            return None

    def _parse_servizi(self):
        """
        Services provided by PA are defined in LDAP using multi-value entry, indexed by 
        a field in the content separed by '#' char, for example:
            
        nomeS: 1#Sportello consulenza Piano Assetto Idrogeologico
        nomeS: 2#Sportello consulenza Piano Bilancio Idrico
        nomeS: 3#Pareri ex Dlgs 152/99
        nomeS: 4#Distribuzione dati territoriali
        descrizioneS: 1#Il servizio fornisce informazioni sugli atti e la cartografia 
          riguardanti il Piano di Bacino stralcio Assetto Idrogeologico
        descrizioneS: 2#Il servizio fornisce informazioni sugli atti e la cartografia 
          riguardanti il Piano di Bacino stralcio Bilancio Idrico
        descrizioneS: 3#Il servizio fornisce pareri nell'ambito dell'iter amministrati
          vo riguardante la concessione di acque pubbliche ex D.Lgs. 152/2006
        descrizioneS: 4#Il servizio fornisce informazioni e dati dal catalogo dei dati
          territoriali prodotti e gestiti dall'Amministrazione
        fruibS: 1#true
        fruibS: 2#true
        fruibS: 3#false
        fruibS: 4#true
        mailS: 1#m.brugioni@adbarno.it
        mailS: 2#i.bonamini@adbarno.it
        mailS: 3#i.bonamini@adbarno.it
        mailS: 4#b.mazzanti@adbarno.it
        telephonenumberS: 1#05526743220
        telephonenumberS: 2#05526743222
        telephonenumberS: 3#05526743222
        telephonenumberS: 4#05526743246
        servizioTelematico: 1#http://www.adbarno.it/cont/testo.php?id=49
        servizioTelematico: 2#http://www.adbarno.it/arnoriver/
        servizioTelematico: 4#http://www.adbarno.it/gds/
    
        this function return a dictionary that represent all services:

        {   'Sportello consulenza Piano Assetto Idrogeologico': { 
                'telephonenumber': '05526743220', 
                'mail': 'm.brugioni@adbarno.it', 
                'servizioTelematico': 'http://www.adbarno.it/cont/testo.php?id=49', 
                'mail_pec': None, 
                'descrizione': 
                'Il servizio fornisce informazioni sugli atti e la cartografia riguardanti il Piano di Bacino stralcio Assetto Idrogeologico'}, 

            'Distribuzione dati territoriali': {
                'telephonenumber': '05526743246', 
                'mail': 'b.mazzanti@adbarno.it', 
                'servizioTelematico': 'http://www.adbarno.it/gds/', 
                'mail_pec': None, 
                'descrizione': "Il servizio fornisce informazioni e dati dal catalogo dei dati territoriali prodotti e gestiti dall'Amministrazione"}, 
            
            'Pareri ex Dlgs 152/99': {
                'telephonenumber': '05526743222', 
                'mail': 'i.bonamini@adbarno.it', 
                'servizioTelematico': None, 
                'mail_pec': None, 
                'descrizione': "Il servizio fornisce pareri nell'ambito dell'iter amministrativo riguardante la concessione di acque pubbliche ex D.Lgs. 152/2006"}, 
                
            'Sportello consulenza Piano Bilancio Idrico': {
                'telephonenumber': '05526743222', 
                'mail': 'i.bonamini@adbarno.it', 
                'servizioTelematico': 'http://www.adbarno.it/arnoriver/', 
                'mail_pec': None, 'descrizione': 
                'Il servizio fornisce informazioni sugli atti e la cartografia riguardanti il Piano di Bacino stralcio Bilancio Idrico'}
        }
        """
        servizi = {}
        if not self._ldap_obj.has_key("nomeS"):
            return servizi
        for nome_servizio_raw in self._ldap_obj['nomeS']:
            servizio = {}
            servizio_key = nome_servizio_raw.split('#')[0]
            nome_servizio = nome_servizio_raw.split('#')[1]
            
            desc_servizio = fruib_servizio = \
             mail_servizio = mail_pec_servizio = \
             telephonenumber_servizio = servizioTelematico_servizio = None 

            try:
                for desc_servizio_raw in self._ldap_obj['descrizioneS']:
                    if desc_servizio_raw.split('#')[0] == servizio_key:
                        desc_servizio = desc_servizio_raw.split('#')[1]
            except KeyError:
                desc_servizio = None
            
            try:
                for fruib_servizio_raw in self._ldap_obj['fruibS']:
                    if fruib_servizio_raw.split('#')[0] == servizio_key:
                        fruib_servizio = fruib_servizio_raw.split('#')[1]
            except KeyError:
                fruib_servizio = None
            
            try:
                for mail_servizio_raw in self._ldap_obj['mailS']:
                    if mail_servizio_raw.split('#')[0] == servizio_key:
                        mail_servizio = mail_servizio_raw.split('#')[1]
            except KeyError:
                mail_servizio = None
            
            try:
                for mail_pec_servizio_raw in self._ldap_obj['mailSPEC']:
                    if mail_pec_servizio_raw.split('#')[0] == servizio_key:
                        mail_pec_servizio = mail_pec_servizio_raw.split('#')[1]
            except KeyError:
                mail_pec_servizio = None

            try:
                for telephonenumber_servizio_raw in self._ldap_obj['telephonenumberS']:
                    if telephonenumber_servizio_raw.split('#')[0] == servizio_key:
                        telephonenumber_servizio = telephonenumber_servizio_raw.split('#')[1]
            except KeyError:
                telephonenumber_servizio = None

            try:
                for servizioTelematico_servizio_raw in self._ldap_obj['servizioTelematico']:
                    if servizioTelematico_servizio_raw.split('#')[0] == servizio_key:
                        servizioTelematico_servizio = servizioTelematico_servizio_raw.split('#')[1]
            except KeyError:
                servizioTelematico_servizio = None
            
            servizio = {'descrizione': desc_servizio, \
                        'mail': mail_servizio, \
                        'mail_pec': mail_pec_servizio, \
                        'telephonenumber': telephonenumber_servizio, \
                        'servizioTelematico': servizioTelematico_servizio}

            servizi[nome_servizio] = servizio
        
        return servizi

class Pa(IpaObj):
    def _parse_ldap_obj(self):
		self.tipo = "amministrazione"
        #TODO: ALL MAY!
        self.codiceAmm = self._get_from_ldap('codiceAmm') #Single
        self.provincia = self._get_from_ldap('provincia') #Single
        self.street = self._get_from_ldap('street') #Single
        self.regione = self._get_from_ldap('regione') #Single
        self.logoAmm = self._get_from_ldap('logoAmm') #Single
        self.postalCode = self._get_from_ldap('postalCode') #Single
        self.sitoIstituzionale = self._get_from_ldap('sitoIstituzionale') #Single
        self.nomeResp = self._get_from_ldap('nomeResp') #Single
        self.cognomeResp = self._get_from_ldap('cognomeResp') #Single
        self.titoloResp = self._get_from_ldap('titoloResp') #Single
        self.mail = self._get_from_ldap('mail') #Single
        self.mailPEC = self._get_from_ldap('mailPEC') #Single
        self.l = self._get_from_ldap('l') #Single Localita
        self.dominioPEC = self._get_from_ldap('dominioPEC') #Single
        self.PECRUPA = self._get_from_ldap('PECRUPA') #Single
        self.tipoAmm = self._get_from_ldap('tipoAmm') #Single
        self.codiceFiscaleAmm = self._get_from_ldap('codiceFiscaleAmm') #Single
        self.acronimo = self._get_from_ldap('acronimo') #Single
        self.description = self._get_from_ldap('description') #Single
        self.contatti = self._get_from_ldap('contatti', single=False) #Multiple
        self.telephoneNumberResp = self._get_from_ldap('telephoneNumberResp') #Single
        self.telephoneNumber = self._get_from_ldap('telephoneNumber') #Single
        self.st = self._get_from_ldap('st') #Single Stato (accreditata/nonaccreditata)

        self.servizi = self._parse_servizi()
        
        self._public_attrs = self._public_attrs + ["dn", "codiceAmm", 'provincia', 'street', 'regione', 'logoAmm',\
            'postalCode', 'sitoIstituzionale', 'nomeResp', 'cognomeResp', 'titoloResp',\
            'mail', 'mailPEC', 'l', 'dominioPEC', 'PECRUPA', 'tipoAmm', 'codiceFiscaleAmm',\
            'acronimo', 'description', 'contatti', 'st', 'telephoneNumberResp', 'telephoneNumber', 'servizi']

class Aoo(IpaObj):
    def _parse_ldap_obj(self):
		self.tipo = "aoo"
        self.aoo = self._get_from_ldap('aoo') #Single
        self.description = self._get_from_ldap('description') #Single
        self.dataIstituzione = self._get_from_ldap('dataIstituzione') #Single
        self.dataSoppressione = self._get_from_ldap('dataSoppressione') #Single
        self.codiceUff = self._get_from_ldap('codiceUff', single=False) #Single
        self.dataSoppressione = self._get_from_ldap('dataSoppressione') #Single
        self.facsimileTelephoneNumber = self._get_from_ldap('facsimileTelephoneNumber') #Single
        self.l = self._get_from_ldap('l') #Single Localita
        self.provincia = self._get_from_ldap('provincia') #Single
        self.street = self._get_from_ldap('street') #Single
        self.regione = self._get_from_ldap('regione') #Single
        self.postalCode = self._get_from_ldap('postalCode') #Single
        self.CAurl = self._get_from_ldap('CAurl') #Single
        self.mail = self._get_from_ldap('mail') #Single
        self.mailPEC = self._get_from_ldap('mailPEC') #Single
        self.nomeResp = self._get_from_ldap('nomeResp') #Single
        self.cognomeResp = self._get_from_ldap('cognomeResp') #Single
        self.mailResp = self._get_from_ldap('mailResp') #Single
        self.mailRespPEC = self._get_from_ldap('mailRespPEC') #Single
        self.telephoneNumberResp = self._get_from_ldap('telephoneNumberResp') #Single
        self.telephoneNumber = self._get_from_ldap('telephoneNumber') #Single
        self.contatti = self._get_from_ldap('contatti', single=False) #Multiple

        self.servizi = self._parse_servizi()
        
        self._public_attrs = self._public_attrs + ['dn', "aoo", 'description', 'dataIstituzione', 'dataSoppressione',\
                'codiceUff', 'dataSoppressione', 'facsimileTelephoneNumber', 'l',\
                'provincia', 'street', 'regione', 'postalCode', 'CAurl', 'mail',\
                'mailPEC', 'nomeResp', 'cognomeResp', 'mailResp', 'mailRespPEC',\
                'telephoneNumberResp', 'telephoneNumber', 'contatti', 'servizi']

class Uo(IpaObj):
    def _parse_ldap_obj(self):
		self.tipo = "ufficio"
        self.description = self._get_from_ldap('description') #Single
        self.CAurl = self._get_from_ldap('CAurl') #Single
        self.mail = self._get_from_ldap('mail') #Single
        self.mailPEC = self._get_from_ldap('mailPEC') #Single
        self.nomeResp = self._get_from_ldap('nomeResp') #Single
        self.cognomeResp = self._get_from_ldap('cognomeResp') #Single
        self.mailResp = self._get_from_ldap('mailResp') #Single
        self.mailRespPEC = self._get_from_ldap('mailRespPEC') #Single
        self.facsimileTelephoneNumber = self._get_from_ldap('facsimileTelephoneNumber') #Single
        self.l = self._get_from_ldap('l') #Single Localita
        self.provincia = self._get_from_ldap('provincia') #Single
        self.street = self._get_from_ldap('street') #Single
        self.regione = self._get_from_ldap('regione') #Single
        self.postalCode = self._get_from_ldap('postalCode') #Single
        self.aooRef = self._get_from_ldap('aooRef') #Single
        self.st = self._get_from_ldap('st') #Single Stato (accreditata/nonaccreditata)
        self.telephoneNumberResp = self._get_from_ldap('telephoneNumberResp') #Single
        self.telephoneNumber = self._get_from_ldap('telephoneNumber') #Single
        self.contatti = self._get_from_ldap('contatti', single=False) #Multiple

        self.servizi = self._parse_servizi()

        self._public_attrs = self._public_attrs + ['dn', 'description','CAurl', 'mail', 'mailPEC', 'nomeResp',\
                'cognomeResp', 'mailResp', 'mailRespPEC', 'facsimileTelephoneNumber',\
                'l', 'provincia', 'street', 'regione', 'postalCode', 'aooRef', \
                'st', 'telephoneNumberResp', 'telephoneNumber', 'contatti']

class MyLDAPObject(ldap.ldapobject.LDAPObject,ldap.resiter.ResultProcessor):
    pass

#TODO: error handling
class IndicePA:
    def __init__(self, indice_pa_uri="ldap://indicepa.gov.it", indice_pa_base="c=it", max_results=50):
        self.indice_pa_base = indice_pa_base
        self.indice_pa_uri = indice_pa_uri
        self.max_results = max_results


    
    #TODO: complete search filter
    #TODO: use asyncronous
    #TODO: use ldap.resiter for realtime entry processing 
    def simple_search(self, search_string):
        
        search_string = ldap.filter.escape_filter_chars(search_string)
        query="(|(nomeS=*" + search_string + "*)\
            (descrizioneS=*" + search_string + "*)\
            (nomeResp=*" + search_string + "*)\
            (cognomeResp=*" + search_string + "*)\
            (titoloResp=*" + search_string + "*)\
            (description=*" + search_string + "*))"
        
        return self._do_search(query)
    
    def search_cod_uff(self, cod_uff):
        query = "(objectclass=ufficio)"
        base = ldap.filter.escape_filter_chars(cod_uff)
        return self._do_search(query, base=base)
    
    def search_cod_aoo(self, cod_aoo):
        query = "(objectclass=aoo)"
        base = ldap.filter.escape_filter_chars(cod_aoo)
        return self._do_search(query, base=base)

    def search_cod_pa(self, cod_pa):
        query = "(objectclass=amministrazione)"
        base = ldap.filter.escape_filter_chars(cod_pa)
        return self._do_search(query, base=base)
	
	def dn_search(self, dn):
        query = "(objectclass=*)"
        base = ldap.filter.escape_filter_chars(dn)
        return self._do_search(query, base=base)

	def advanced_search(self, search_dict={}):
		query_part = ""
		for field in ["Acronimo", "aoo", "aooRef", "c", "CAurl", "codiceAmm", "codiceFiscaleAmm", "codiceUff", "CodiceUnivocoUO", "cognomeResp", "contatti", "dataIstituzione", "dataSoppressione", "dataVerifica", "description", "descrizioneS", "mailPEC", "dominioPEC", "facsimileTelephoneNumber", "fruibS", "l", "logoAmm", "mail", "mailResp", "mailS", "mailSPub", "nomeResp", "nomeS", "o", "ou", "postalCode", "provincia", "regione", "servizioTelematico", "sitoIstituzionale", "st", "street", "telephoneNumber", "telephonenumberResp", "telephonenumberS", "tipoAmm", "titoloResp"]:
			try:
				if len(search_dict[field]) > 0:
					query_part = query_part + "(%s=*%s*)" % (ldap.filter.escape_filter_chars(field), ldap.filter.escape_filter_chars(search_dict[field]))
			except KeyError:
				pass
		if len(search_dict['tipo']) > 0:
			obj_query = ""
			for objectclass in search_dict['tipo']:
				obj_query = obj_query + "(objectclass=%s)" % ldap.filter.escape_filter_chars(objectclass)
			obj_query = "(|" + obj_query + ")"
		else:
			obj_query = "(objectclass=*)"	
		if len(query_part) > 0:
			return self._do_search("(&" + obj_query + "(|" + query_part + "))")
		else:
			return self._do_search(obj_query)
	
    def _do_search(self, query, attrlist=None, base=indice_pa_base, scope=ldap.SCOPE_SUBTREE): 

        self._ldapconn = MyLDAPObject(self.indice_pa_uri)
        msg_id = self._ldapconn.search(base, scope, query, attrlist=attrlist)
        ret = []
		
        i=0
        for res_type,result,res_msgid,res_controls in self._ldapconn.allresults(msg_id):
            if i >= self.max_results:
                self._ldapconn.unbind_s()
                raise ldap.SIZELIMIT_EXCEEDED("Exceeded maximum results")
            for dn, ldap_obj in result:
				if dn == indice_pa_base:
					continue
                if "ufficio" in ldap_obj["objectClass"]:
                    res_obj = Uo(dn, ldap_obj)
                elif "aoo" in ldap_obj["objectClass"]:
                    res_obj = Aoo(dn, ldap_obj)
                elif "amministrazione" in ldap_obj["objectClass"]:
                    res_obj = Pa(dn, ldap_obj)
				else:
					raise Exception("tipo non trovato: %s" % ldap_obj)
                ret.append(res_obj)
            i = i + 1
		if i == 0:
			raise Exception("No entry found")
        self._ldapconn.unbind_s()
        return ret
    

if __name__ == '__main__':
    IPA = IndicePA(max_results=20)

    #r = IPA.simple_search('musso')

    #r = IPA.search_cod_uff('ou=uff01,o=c_f828,c=it')

    r = IPA.search_cod_aoo('aoo=c_f828,o=c_f828,c=it')

    print json.dumps(r, cls=IpaJsonEncoder, indent=4) 

