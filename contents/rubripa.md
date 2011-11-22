<!--
<div id="submenu">
 <ul>
  <li><a href="">rubriPa</a></li>
  <li><a href="">Documentazione</a></li>
  <li><a href="">Installazione</a></li>
 </ul>
</div>
-->
## rubriPA

### Collega le tue applicazioni con le PA

Tramite le Web API di **rubriPA** permetti facilmente alle tue applicazioni
di interagire con le Pubbliche Amministrazioni italiane.

#### I servizi offerti da rubriPA:

-   Accesso ai dati delle PA tramite [Web API][] REST e dati
    serializzati JSON
-   Una [comoda interfaccia web][] per ricercare le PA ed esprimere commenti sui social networks.
-   Accesso diretto ai numeri di telefono delle PA tramite [Telefoni VoIP snom][]

#### Prossimamente:

-   Un proxy LDAP verso IndicePA per poter utilizzare IndicePA come una
    **Rubrica aziendale** <span class="inprogress">(Work in
    progress…)</span>
-   Un servizio di failover nel caso (frequente) di down di [IndicePA](http://indicepa.gov.it)
    <span class="inprogress">(Work in progress...)</span>

  [Web API]: /api.html
  [comoda interfaccia web]: /search-menu.html
  [Telefoni VoIP snom]: /rubripa4snom.html

--------------------------------------------

## Documentazione

**rubriPA** è utilizzabile come servizio direttamente accedento alle [API](/api.html) pubbliche, oppure 
è possibile installarlo su di un proprio server. E' consigliato installarlo localmente per utilizzi di produzione,
magari replicando il database di indicePA.

### Installazione

- **Requisiti**: rubriPA è scritto in linguaggio [python](http://www.python.org) (>=2.6), utilizza un database LDAP (è necessario [python-ldap](http://www.python-ldap.org) >= 2.0.11) e utilizza [python-markdown2](https://github.com/trentm/python-markdown2). rubriPA utilizza [web.py](http://www.webpy.org) come web framework.

- **Download**: Puoi scaricare l'ultima versione rubriPA dalle pagine github del progetto: [https://github.com/pbertera/rubripa.it/tags](https://github.com/pbertera/rubripa.it/tags)

- **Installazione**: dopo aver scaricato ed estratto rubripa puoi lanciare direttamente l'eseguibile *application.py*, di default rimarrà in ascolto sulla porta http 8080, per accedere a rubripa non dovrai fare altro che puntare il browser su: http://localhost:8080
**TODO:** Installazione con apache o lighttpd

- **Replica del database LDAP**: TODO.

### Roadmap

- Documentare la configurazone relativa ai telefoni snom (30%)
- Pubblicare documentazione relativa all'installazione dell'applicazione, alla replica di indicepa e problematiche legate ad LDAP (10%)
- Creare delle API di piu' alto livello (0%)
- Documentare e pubblicare il codice di rubripa4snom (0%)
- Creare una pagina con esempi d'uso (0%)
- Aprire una mailing list di supporto (0%)
- Aggiungere FAQ (30%)
- Completare la pagina Info (50%)
