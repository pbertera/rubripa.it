import web
import app.helpers.htmlrenders

web.config.debug = True

indice_pa_uri = "ldap://indicepa.gov.it"
indice_pa_base = "c=it"
indice_pa_max_res = 1000

blog_markdown="contents/blog.md"
home_markdown="contents/home.md"
rubripa_markdown="contents/rubripa.md"
rubripa4snom_markdown="contents/rubripa4snom.md"
api_markdown="contents/api.md"
faq_markdown="contents/faq.md"
info_markdown="contents/info.md"

# TODO configure pages via this dict:
# TODO dynamic routing ??
# pages = {
#		"Home": {"link": "/home.html", "content": "contents/home.md"},
#		"rubripa": {"link": "/rubripa.html", "content": "contents/ipa4.md"},
#		"rubripa4snom": {"link": "/ipa4snom.html", "content": "contents/ipa4snom.md"},
#		"API": {"link": "/api.html", "content": "contents/api.md"},
#		"Faq": {"link": "/faq.html", "content": "contents/faq.md"},
#	
#	}
pages = [ 
		{"name": "Home", "link": "/"},
		{"name": "Cerca", "link": "/search-menu.html"},
		{"name": "rubriPa", "link": "/rubripa.html"},
		{"name": "rubriPa4snom", "link": "/rubripa4snom.html"},
		{"name": "API", "link": "/api.html"},
		{"name": "Faq", "link": "/faq.html"},
		{"name": "Info", "link": "/info.html"},
	]

htmlview = web.template.render('app/views', cache=False, base="layout", globals={'htmlrenders': app.helpers.htmlrenders, 'ctx': web.ctx, 'allpages':pages})
