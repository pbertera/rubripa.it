import web
import app.helpers.htmlrenders

web.config.debug = True

indice_pa_uri = "ldap://indicepa.gov.it"
indice_pa_base = "c=it"
indice_pa_max_res = 1000

pages = [ 
		{"name": "Home", "link": "/", "content_file": "contents/home.md"},
		{"name": "Cerca", "link": "/search-menu.html", "content_file": "contents/search-menu.md"},
		{"name": "rubriPa", "link": "/rubripa.html", "content_file": "contents/rubripa.md"},
		{"name": "rubriPa4snom", "link": "/rubripa4snom.html", "content_file": "contents/rubripa4snom.md"},
		{"name": "API", "link": "/api.html", "content_file": "contents/api.md"},
		{"name": "Faq", "link": "/faq.html", "content_file": "contents/faq.md"},
		{"name": "Info", "link": "/info.html", "content_file": "contents/info.md"},
	]

static_dir = "public"

custom_pages = [
	# Search forms  
    ('/simple-search-form\.html', 'app.controllers.searchforms.HtmlSimpleSearchForm'),
    ('/advanced-search-form\.html',   'app.controllers.searchforms.HtmlAdvancedSearchForm'),
    ('/dn-search-form\.html',     'app.controllers.searchforms.HtmlDnSearchForm'),

    # Search results
    ('/simple-search\.html',        'app.controllers.search.HtmlSimpleSearch'),
    ('/advanced-search\.html',      'app.controllers.search.HtmlAdvancedSearch'),
    ('/dn-search\.html',         'app.controllers.search.HtmlDnSearch'),

    # html renders 
    ('/uff-search\.html',         'app.controllers.search.HtmlUffSearch'),
    ('/aoo-search\.html',         'app.controllers.search.HtmlAooSearch'),
    ('/pa-search\.html',          'app.controllers.search.HtmlPaSearch'),

    # API
    ('/dn-search',           'app.controllers.search.DnSearch'),
    ('/advanced-search',     'app.controllers.search.AdvancedSearch'),
    ('/simple-search',   'app.controllers.search.SimpleSearch'),
    ('/uff-search',      'app.controllers.search.UffSearch'),
    ('/aoo-search',      'app.controllers.search.AooSearch'),
    ('/pa-search',       'app.controllers.search.PaSearch')
]

htmlview = web.template.render('app/views', cache=False, base="layout", globals={'htmlrenders': app.helpers.htmlrenders, 'ctx': web.ctx, 'allpages':pages})
