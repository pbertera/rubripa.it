## Web API

**rubriPA** espone delle Web API [REST](http://en.wikipedia.org/wiki/Representational_state_transfer) che permettono la ricerca nel database.
Tutte le API cengono chiamate via il metodo [HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) GET.

In caso di errore la response HTTP conterrà il codice di errore, mentre il corpo della response conterrà il messaggio d'errore serializzato in [JSON](http://www.json.org/)

************************************************************************

* **/simple-search** ricerca di una chiave singola all'interno di indicePA
* **/advanced-search** ricerca completa
* **/uff-search** ricerca di un ufficio
* **/aoo-search** ricerca di un'area organizzativa omogenea
* **/pa-search** ricerca di una Pubblica Amministrazione
* **/dn-search** ricerca di una entità tramite il **dn**

************************************************************************

#### /simple-search

* **metodo HTTP**: GET
* **parametri**: q
* **ritorno**: il risultato della ricerca serializzato JSON
* **esempio**: [/simple-search?q=musso](/simple-search?q=musso)

#### /advanced-search
* **metodo HTTP**: GET
* **parametri**: per ora vedi il form [/advanced-search-form.html](/advanced-search.html)
* **ritorno**: il risultato della ricerca serializzato JSON
* **esempio**: [/advanced-search?description=musso&tipo=amministrazione](/advanced-search?description=musso&tipo=amministrazione)

#### /uff-search
* **metodo HTTP**: GET
* **parametri**: coduff
* **ritorno**: Questo metodo effettua una ricerca su IndicePA di tutti gli oggetti di tipo **ufficio** con [dn](http://www.zytrax.com/books/ldap/apa/dn-rdn.html "dn") uguale al parametro **coduff**
* **esempio**: [/uff-search?coduff=ou=uff01,o=c_f828,c=it](/uff-search?coduff=ou=uff01,o=c_f828,c=it)

#### /aoo-search
* **metodo HTTP**: GET
* **parametri**: codaoo
* **ritorno**: Questo metodo effettua una ricerca su IndicePA di tutti gli oggetti di tipo **aoo** con [dn](http://www.zytrax.com/books/ldap/apa/dn-rdn.html "dn") uguale al parametro **codaoo**
* **esempio**: [/aoo-search?codaoo=aoo=c_f828,o=c_f828,c=it](/aoo-search?codaoo=aoo=c_f828,o=c_f828,c=it)

#### /pa-search
* **metodo HTTP**: GET
* **parametri**: codpa
* **ritorno**: Questo metodo effettua una ricerca su IndicePA di tutti gli oggetti di tipo **pa** con [dn](http://www.zytrax.com/books/ldap/apa/dn-rdn.html "dn") uguale al parametro **codpa**
* **esempio**: [/pa-search?codpa=o=c_c801,c=it](/pa-search?codpa=o=c_c801,c=it)

#### /dn-search
* **metodo HTTP**: GET
* **parametri**: dn
* **ritorno**: Questo metodo effettua una ricerca su IndicePA di tutti gli con [dn](http://www.zytrax.com/books/ldap/apa/dn-rdn.html "dn") uguale al parametro **dn**
* **esempio**: [/dn-search?dn=o=c_c801,c=it](/dn-search?dn=o=c_c801,c=it)
