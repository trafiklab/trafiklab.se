---
title: SL Route-planner v3.1 (Reseplanerare 3.1)
weight: 100
date: 2019-01-14
aliases: 
  - /api/sl-reseplanerare
  - /api/sl-reseplanerare-31
  - /api/sl-reseplanerare-31/documentation
  - /api/sl-reseplanerare-31/console
  - /api/sl-reseplanerare-31/nivaer
  - /node/25593
  - /node/25593/documentation
  - /node/25593/console
  - /node/25593/nivaer
---
<h2> <a>Beskrivning</a></h2>
<p>Med detta API kan du få reseförslag från A till B inom Stockholms län med SLs trafik. I SLs reseplanerare finns även Waxholmsbolagets trafik. APIet kan användas för att beräkna reseförslag mellan valfri kombination av position och/eller stoppställe. APIet returnerar reseförslag från ”bästa matchning” av det som läggs in.</p>

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website. {{% /info %}}

I reseplaneraren finns det fyra olika funktioner som kan anropas:</p>

- Trip: Räknar ut en resa från en startpunkt till en destination. Dessa kan vara stations-id eller 
koordinater baserade på adresser eller ”intressepunkter.
- JourneyDetail: Returnerar detaljerad information om en del av en resa med ett fordon.
Den returnerar en lista på alla stop/stationer inklusive alla ankomst- och avgångstider med realtidsdata(om det finns tillgängligt).<
- Reconstruction: Används för att återskapa en kopia av en Trip med hjälp av ett rekonstruktionskontext. Resultatet 
  kommer att vara en fullständig kopia givet att underliggande data inte har ändrats.<
- GisRoute: Tjänsten används för att få detaljerad information om färdväg.
- XSD: Returnerar en xsd för ovanstående service-svar.
  
Reseplaneraren anropas med en GET-request per tjänst med UTF-8 url-kodade GET-parametrar.

## Förändringar sedan tidigare version

<p>En ändring har genomförts som kan påverka implementerande applikationer.<br />
För version 3.1 av reseplaneraren så har svarsformatet avseende crd-elementen i den polyline som beskriver detaljerad färdväg ändrats. Punkterna representeras i denna version av double-tal jämfört med version 3.0 som representerade dem som heltal.<br />
</p>
<p><span>>Tidigare version (3.0): <em>&lt;crd&gt;17973032&lt;/crd&gt;&lt;crd&gt;59360501&lt;/crd&gt;&lt;crd&gt;9&lt;/crd&gt; &lt;crd&gt;18&lt;/crd&gt;</em></p>
<p><br />
<span>>Travelplanner 3.1: <em>&lt;crd&gt;17.973032&lt;/crd&gt;&lt;crd&gt;59.360501&lt;/crd&gt;&lt;crd&gt;9.0E-6&lt;/crd&gt;&lt;crd&gt;1.8E-5&lt;/crd&gt;</em></p>
<h2>URL</h2>

- Trip: `api.sl.se/api2/TravelplannerV3_1/trip.<FORMAT>?key=<DIN API NYCKEL>&parametrar`
- Journey detail: `api.sl.se/api2/TravelplannerV3_1/journeydetail.<FORMAT>?key=<DIN API NYCKEL>&<referensparameter>`
- Recontruction: `api.sl.se/api2/TravelplannerV3_1/Reconstruction.<FORMAT>?key=<DIN API NYCKEL>&<referensparameter>`
- XSD: `api.sl.se/api2/TravelplannerV3_1/xsd.xml?key=<DIN API NYCKEL>`

## Format
Json eller Xml enligt ändelse till serviceanropet.

## Trip

<h3> <a> Parametrar</a></h3><table>
    <tbody>
    <tr>
        <td>
            <p><strong>Namn</strong></p>
        </td>
        <td>
            <p><strong>Beskrivning</strong></p>
        </td>
        <td>
            <p><strong>Kommentar</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Lang</p>
        </td>
        <td>
            <p>Språk (en/sv/de)</p>
        </td>
        <td>
            <p>Språk i svar, default de.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originId</p>
        </td>
        <td>
            <p>Internt id för startpunkt,</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originExtId</p>
        </td>
        <td>
            <p>Startpunkt, id</p>
        </td>
        <td>
            <p>Kan antingen vara siteid eller ett alias, site eller akronym.<br/> Exempel: 300109001, 9001, TCE</p>
            <p>En startpunkt måste anges med ett av originId, originExtId eller
                orgiginCoordLat/originCoordLong</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originCoordLat</p>
        </td>
        <td>
            <p>Latitud för startpunkt</p>
        </td>
        <td>
            <p>Måste anges tillsammans med <em>originCoordLong</em>.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originCoordLong</p>
        </td>
        <td>
            <p>Longitud för startpunkt</p>
        </td>
        <td>
            <p>Måste anges tillsammans med <em>originCoordLat</em>.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destId</p>
        </td>
        <td>
            <p>Intent id för destination.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destExtId</p>
        </td>
        <td>
            <p>Destination, id.</p>
        </td>
        <td>
            <p>Kan antingen vara siteid eller ett alias, site eller akronym.<br/> Exempel: 300109001, 9001, TCE.</p>
            <p>En destination måste anges med ett av originId, originExtId eller
                orgiginCoordLat/originCoordLong</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destCoordLat</p>
        </td>
        <td>
            <p>Latitud för destination</p>
        </td>
        <td>
            <p>Måste anges tillsammans med <em>destinationCoordLong</em><u>.</u></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destCoordLong</p>
        </td>
        <td>
            <p>Longitud för destination</p>
        </td>
        <td>
            <p>Måste anges tillsammans med destinationCoordLat</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Via</p>
        </td>
        <td>
            <p>Lista av specification av stationer att passera.</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Separeras av ; i följande format:</p>
            <p>viaId|vänttid|status|produkter</p>
            <p>-viaId, internt eller extert id på hållplats/station att passera</p>
            <p>-vänttid, minuter att stanna på passerad hållplats/station (valfritt)</p>
            <p>-status, ett av EXR (av- och påstigning krävs), NER (påstigning krävs ej), NXR
                (avstigning krävs ej), NEXR (av och påstigning krävs ej). Valfritt, EXT är
                default.</p>
            <p>- produkter, trafikslag för via, se Produkt.</p>
            <p>Ex1. via två hållplatser, 9001;9117</p>
            <p>Ex2, via två hållpatser med 15 respektive 10 minuters väntetid, 9001|15;9117|10</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>viaId</p>
        </td>
        <td>
            <p>Id för station att passera</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Enskilt id för en hållplats/station att resa via, ex 9001.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>viaWaitTime</p>
        </td>
        <td>
            <p>Vänttid för passerad station</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Antal minuter som ska spenderas på via-station angiven med <em>viaId</em>.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Avoid</p>
        </td>
        <td>
            <p>Lista av stationer att undvika att resa via.</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Separeras av ; i följande format:</p>
            <p>avoidId|avoidStatus</p>
            <p>-avoidId, internt eller externt id för hållplats/ station att undvika,</p>
            <p>- avoidStatus, ett av NPAVO (passera ej), NCAVO (byt ej vid). Valfritt.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>avoidID</p>
        </td>
        <td>
            <p>Id för station att undvika</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Internt eller externt id för hållplats/station att undvika för byten</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>changeTimePercent</p>
        </td>
        <td>
            <p>Utökad bytestid, procentuell</p>
            <p>(100-500)</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Procentuell utökning av ursprungligt beräknad tid för att hantera ett byte. Ex, 200
                dubblar tiden som systemet kommer använda för att resenären ska hinna med ett byte.
                Default 100.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>minChangeTime</p>
        </td>
        <td>
            <p>Minsta bytestid (min)</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Minsta antal minuter som ska användas vid byten.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>maxChangeTime</p>
        </td>
        <td>
            <p>Högsta bytestid</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Flest antal minuter som ska användas vid byten.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>addChangeTime</p>
        </td>
        <td>
            <p>Utökad bytestid</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Antal minuter som läggs till beräknad bytestid.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>maxChange</p>
        </td>
        <td>
            <p>Max antal byten (0-11)</p>
        </td>
        <td>
            <p>Högst antal byten på föreslagna resor.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Date</p>
        </td>
        <td>
            <p>Datum</p>
            <p>åååå-MM-DD</p>
        </td>
        <td>
            <p>Valfritt.</p>
            <p>Datum för resa. Default är dagens datum (servertid)</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Time</p>
        </td>
        <td>
            <p>Klockslag</p>
            <p>TT:MM</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Klockslag för resa. Default är aktuellt klockslag (servertid)</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>searchForArrival</p>
        </td>
        <td>
            <p>0 eller 1</p>
        </td>
        <td>
            <p>Valfritt.</p>
            <p>Om 1 används angivna <em>date</em> och <em>time </em>för ankomsttid istället för avgångstid.
            </p>
        </td>
    </tr>
    <tr>
        <td>
            <p>numF</p>
        </td>
        <td>
            <p>0-6</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Min antal resor efter angiven starttid, default 4.</p>
            <p><em>numF</em> och <em>numB</em> tillsammans kan ej överstiga 6.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>numB</p>
        </td>
        <td>
            <p>0-6</p>
        </td>
        <td>
            <p>Valfritt.</p>
            <p>Min antal resor före angiven starttid, default 1.</p>
            <p><em>numF</em> och <em>numB</em> tillsammans kan ej överstiga 6.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Products</p>
        </td>
        <td>
            <p>Trafikslag, heltal</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Kombinationsvärde av önskade trafikslag om inte alla ska användas vid utsökning av
                resor.</p>
            <p>Bitmask enligt följande:</p>
            <p>Pendeltåg (1)</p>
            <p>Tunnelbana (2)</p>
            <p>Lokalbana/spårvagn (4)</p>
            <p>Buss (8)</p>
            <p>Ej i bruk (16)</p>
            <p>Ej i bruk (32)</p>
            <p>Båt typ (64)</p>
            <p>Närtrafik (128)</p>
            <p>Värdes anges som heltalsvärdet av den kombinerade bitmasken, ex Buss och båt, 8+64 =
                72</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Lines</p>
        </td>
        <td>
            <p>Inkluderade filtrering av linjer.</p>
        </td>
        <td>
            <p>Linje eller linjer, separerade med kommatecken som ska användas för att filtrera resultat,
                utropstecken används för exkludering av linjer.</p>
            <p>Ex:<br/> lines=55,122 (endast linje 55 och 122)<br/> lines=!19 (Ej linje 19)</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Context</p>
        </td>
        <td>
            <p>Tidigare eller senare resor</p>
        </td>
        <td>
            <p>Valfritt.</p>
            <p>Parameter som anger startpunkt för att söka senare eller tidigare resor. Värdet fås
                av resultatvärdet srcF eller srcB i ett anrop till trip-tjänsten. Se 2.4.2</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Poly</p>
        </td>
        <td>
            <p>0 eller 1</p>
        </td>
        <td>
            <p>Valfritt.</p>
            <p>Anger om detaljerade färdvägar ska beräknas för resultaten. För beskrivning av
                polyline se 2.4.5. Default 0.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Passlist</p>
        </td>
        <td>
            <p>0 eller 1</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Anger om hållplatser/stationer som passeras på resan ska hämtas. Default 0.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originWalk</p>
        </td>
        <td>
            <p>0 eller 1 + detaljering</p>
        </td>
        <td>
            <p>Valfritt, Default 1</p>
            <p>Anger om en resa ska kunna inledas med en gångsträcka. För detaljering av avstånd
                kan min och max antal metrar och anges som 1,[minavstånd],[maxavstånd],[hastighet],[fågelväg]</p>
            <p>Hastighet anges som följande:<br/> &lt; 100: snabbare</p>
            <p>= 100: normalt (default)</p>
            <p>&gt; 100: lågsammare</p>
            <p>Fågelväg:<br/> 1= på<br/> 0= av</p>
            <p>Ex. 1,0,1000,0,1 Tillåt snabb gång men maximalt 1000 meter med fågelväg.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destWalk</p>
        </td>
        <td>
            <p>0 eller 1 + detaljering</p>
        </td>
        <td>
            <p>Valfritt.</p>
            <p>Som <em>originWalk</em> fast för destination.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originBike</p>
        </td>
        <td></td>
        <td>
            <p>Valfritt.</p>
            <p>Som <em>originWalk</em></p>
            <p>Kommentar:<br/> För att få ut korrekt resultat så behöver man inaktivera sökning
                med gång, dvs sätta parametern originWalk=0</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destBike</p>
        </td>
        <td></td>
        <td>
            <p>Valfritt.</p>
            <p>Som <em>originWalk</em></p>
            <p>Kommentar:<br/> För att få ut korrekt resultat så behöver man inaktivera sökning
                med gång, dvs sätta parametern destWalk=0</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originCar</p>
        </td>
        <td></td>
        <td>
            <p>Används ej i dagsläget</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destCar</p>
        </td>
        <td></td>
        <td>
            <p>Används ej i dagsläget</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originTaxi</p>
        </td>
        <td></td>
        <td>
            <p>Används ej i dagsläget</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destTaxi</p>
        </td>
        <td></td>
        <td>
            <p>Används ej i dagsläget</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>originPark</p>
        </td>
        <td></td>
        <td>
            <p>Används ej i dagsläget<br/> Möjliggör &ldquo;Parkera och åk&rdquo; I början
                av en resa.<br/> För att finjustera avståndet till nästa station, se <em>originWalk</em>
            </p>
        </td>
    </tr>
    <tr>
        <td>
            <p>destPark</p>
        </td>
        <td></td>
        <td>
            <p>Används ej i dagsläget<br/> Möjliggör &ldquo;Parkera och åk&rdquo; I slutet av
                en resa.<br/> För att finjustera avståndet till nästa station, se <em>originWalk</em>
            </p>
        </td>
    </tr>
    </tbody>
</table>
<h3>Sökning efter tidigare eller senare resor</h3>
<p>I resultat från trip kommer två utdataparametrar, scrB och scrF, som kan användas för att söka
    tidigare (scrB) eller senare (scrF) avgångar. Detta görs genom att skicka in samma sökning till trip
    med parametern <em>context</em> satt till värdet av den av de två som vill användas.</p>
<h3>Anmärkningar</h3>
<p>I sökresultaten finns olika typer av anmärkningar.</p>
<p>Fasta anmärkningar är inlagda som &rdquo;notes&rdquo;. Fasta anmärkningar är anmärkningar
    kopplade till avgången i tidtabellen, som tex förhandsbokning på telefon.</p>
<p>Störningsmeddelanden ligger inlagda som &rdquo;Messages&rdquo;.</p>
<h3>Priser</h3>
<p>Priser för en resa kommer i &rdquo;TariffResult&rdquo;, priserna är angivna som heltal i ören.
    Exempelvis:</p>

```xml

<TariffResult>
    <fareSetItem name="ONEWAY" desc="SL">
        <fareItem name="Reskassa" desc="Helt pris" cur="SEK" price="3100"/>
        <fareItem name="övriga försäljningsställen" desc="Helt pris" cur="SEK" price="4400"/>
        <fareItem name="Konduktör på Spårväg City" desc="Helt pris" cur="SEK" price="6200"/>
        <fareItem name="Reskassa" desc="Reducerat pris" cur="SEK" price="2100"/>
        <fareItem name="övriga försäljningsställen" desc="Reducerat pris" cur="SEK" price="3000"/>
        <fareItem name="Konduktör på Spårväg City" desc="Reducerat pris" cur="SEK" price="4100"/>
    </fareSetItem>
</TariffResult>
```

<h3>Detaljerade färdvägar</h3>
<p><a>Trip och journeyDetail kan leverera en detaljerad färdväg för resultatet i &rdquo;Polyline&rdquo;,
    exempelvis:</a></p>

```xml
<Polyline type="WGS84" delta="true" dim="2" crdEncS="NNNNNN">
    <crd>18.06199</crd>
    <crd>59.332455</crd>
    <crd>2.7E-5</crd>
    <crd>-9.0E-6</crd>
    <crd>-1.8E-5</crd>
    <crd>9.0E-6</crd>
</Polyline>
```

<p>Koordinatlistan består av en startlongitud och latitud, och följande differenser från föregående
    punkt. Dvs i exemplet ovan en linje bestående av punkterna (longitud, latitud):<br/> (18.061711,59.331331),(
    18.062017, 59.332446),( 18.061999, 59.332455)</p>
<h3>Realtid</h3>
<p>Realtid finns för nuvarande för bussar, pendeltåg, tvärbanan och roslagsbanan.</p>
<p>Realtiden är en prognos, dvs, den är ungefärlig.</p>
<p>Om det finns realtid så anges detta i separata fält. För realtidstider i reseförslaget så
    läggs &rdquo;rtTime&rdquo; och &rdquo;rtDate&rdquo; till i svaret. De gamla fälten &rdquo;time&rdquo; och
    &rdquo;date&rdquo; är kvar så att man vet vad det ändrats från/till.</p>
<p>I denna version av api:et är realtid inte parameterstyrt utan levereras alltid om data finns
    tillgängligt.</p>
<h3>Svarsformat</h3>
<p>API:et kan returnera både xml och json.<br/> Json-innehållet är automatiskt konverterat från
    xml enligt följande regler:</p>
<ul>
    <li>Elementnamn blir objektegenskaper</li>
    <li>Text (PCDATA) blir en objektegenskap med namnet "$"<br/> &lt;a&gt;foo&lt;/a&gt; blir { "a": { "$" : "foo" } }
    </li>
    <li>Nestlade element blir nestlade egenskaper:<br/>
        &lt;a&gt;&lt;b&gt;foo&lt;/b&gt;&lt;c&gt;foo&lt;/c&gt;&lt;/a&gt;<br/> blir<br/> { "a": { "b" : { "$": "foo" },
        "c": { "$": "foo"} } }
    </li>
    <li>Om det finns multipla element med samma namn så översätts det till en json array ex:<br/> &lt;a&gt;&lt;b&gt;foo1&lt;/b&gt;&lt;b&gt;foo2&lt;/b&gt;&lt;/a&gt;<br/>
        blir<br/> { "a": { "b" : [{"$": foo1" }, {"$": "foo2" }] } }
    </li>
    <li>Attributnamn blir objektegenskaper<br/> &lt;a atb="foo1"&gt;foo2&lt;/a&gt;<br/> blir<br/> { "a": { "atb" :
        "foo1", "$" : "foo2" } }
    </li>
</ul>

<h3>Svarsstruktur</h3>
<p>I nedan tabell beskrivs den xml struktur som finns. Vissa uppenbara attribut är inte med då det blir väldigt
    mycket annars, som t.ex. Lat och Lon för att ge en lättare överblick av det som är mindre självklart.<br/>
    För mer information om olika attribut och element så finns också xsd&rsquo;n hafasRestTrip.xsd.</p>
<p><strong>Exempel förklaring av nedan struktur i tabellen:</strong><br/> element1/element2 =&gt; element2 är
    ett underelement till element1.<br/> element1.attribut1 =&gt; attribut1 är ett attribut till element1.</p>
<table>
    <tbody>
    <tr>
        <td>
            <p>Element</p>
        </td>
        <td>
            <p>Notes</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Error</em></p>
        </td>
        <td>
            <p>Element som innehåller felbeskrivning</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Complex type <em>Polyline</em></p>
        </td>
        <td>
            <p>Detaljerad färdväg, om poly=1 angivits.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element Product</p>
            <p>Complex type <em>ProductType</em></p>
        </td>
        <td>
            <p>Produktkontext, möjliggör åtkomst till intern data.</p>
            <p>Ex.</p>
            <p>&lt;Product name=" " admin="<strong>100017</strong>" operatorCode="<strong>SL</strong>"
                operator="<strong>Storstockholms Lokaltrafik</strong>" num="<strong>11297</strong>"
                line="<strong>17</strong>" catOutS="<strong>MET</strong>" catOutL="<strong>TUNNELBANA </strong>"
                catOut="<strong>METRO </strong>" catIn="<strong>MET</strong>" catCode="<strong>1</strong>"/&gt;</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>JourneyDetailRef</em></p>
        </td>
        <td>
            <p>Referens till journey detail för ett detta leg-elementet.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Simple type <em>PrognosisType</em></p>
        </td>
        <td>
            <p>Innehåller typ av prognos. Om den rapporterades in av extern part, räknades ut, eller rättades
                av systemet.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Stops</em></p>
        </td>
        <td>
            <p>En lista av journey stops/stations, om passlist=1 angivits.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Complex type <em>StopType</em></p>
        </td>
        <td>
            <p>Elementet stop innehåller namnet, route index, latitude, longitude, departure time/date, arrival
                time/date, track, realtidsdata för ankomst och avgång sampt track.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Messages</em></p>
        </td>
        <td>
            <p>Innehåller en lista av meddelanden för denna trip.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Names</em></p>
        </td>
        <td>
            <p>Lists av journey names</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>JourneyStatus</em></p>
        </td>
        <td>
            <p>Innehåller status för Journey.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>TripList</em></p>
        </td>
        <td>
            <p>Rotelement, innehåller en lista på alla Trips vid anrop till trip. Om ett större fel har
                inträffat under anrop så innehåller attributen errorCode och errortext
                felbeskrivning.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Trip</em></p>
        </td>
        <td>
            <p>Trip-objektet innehåller en lista med Leg-objekt med den uträknade resan.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>LegList</em></p>
        </td>
        <td>
            <p>Innehåller alla Leg-element för en Trip.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Leg</em></p>
        </td>
        <td>
            <p>Leg-objektet är en del av en resa. Det kan vara antingen en gångväg, cykel eller bilväg
                eller oftast en resa med bus, tåg, eller annat typ av transportmedel.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Origin</em></p>
        </td>
        <td>
            <p>Innehåller namn, typ, rout index, realtidsdata för startpunkten för denna resa.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>Destination</em></p>
        </td>
        <td>
            <p>Innehåller namn, typ, rout index, realtidsdata för destinationen för denna resa.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Element <em>GisRef</em></p>
        </td>
        <td>
            <p>Referens till en specifik route i ett Leg-element.</p>
        </td>
    </tr>
    </tbody>
</table>
<h3>Genererad exempeldata</h3>

```xml
<?xml version="1.0" encoding="utf-8"?>
<Trip alternative="false" valid="true" idx="1" tripId="tripId1" ctxRecon="ctxRecon1" duration="P396DT1H1M1S"
      return="false" ecoUrl="ecoUrl1" checksum="checksum1" xmlns="hafas_rest">
    <Messages>
        <Message id="id1" externalId="externalId1" act="true" pub="pub1" head="head1" lead="lead1" text="text1"
                 tckr="tckr1" company="company1" category="category1" priority="1" products="1" icon="icon1"
                 routeIdxFrom="1" routeIdxTo="1" sTime="sTime1" sDate="sDate1" eTime="eTime1" eDate="eDate1"
                 altStart="altStart1" altEnd="altEnd1">
            <affectedProduct name="name1" num="num1" line="line1" catOut="catOut1" catIn="catIn1" catCode="catCode1"
                             catOutS="catOutS1" catOutL="catOutL1" operatorCode="operatorCode1" operator="operator1"
                             admin="admin1"/>
            <affectedProduct name="name2" num="num2" line="line2" catOut="catOut2" catIn="catIn2" catCode="catCode2"
                             catOutS="catOutS2" catOutL="catOutL2" operatorCode="operatorCode2" operator="operator2"
                             admin="admin2"/>
            <affectedProduct name="name3" num="num3" line="line3" catOut="catOut3" catIn="catIn3" catCode="catCode3"
                             catOutS="catOutS3" catOutL="catOutL3" operatorCode="operatorCode3" operator="operator3"
                             admin="admin3"/>
        </Message>
        <Message id="id2" externalId="externalId2" act="false" pub="pub2" head="head2" lead="lead2" text="text2"
                 tckr="tckr2" company="company2" category="category2" priority="-2147483647" products="-2147483647"
                 icon="icon2" routeIdxFrom="-2147483647" routeIdxTo="-2147483647" sTime="sTime2" sDate="sDate2"
                 eTime="eTime2" eDate="eDate2" altStart="altStart2" altEnd="altEnd2">
            <affectedProduct name="name4" num="num4" line="line4" catOut="catOut4" catIn="catIn4" catCode="catCode4"
                             catOutS="catOutS4" catOutL="catOutL4" operatorCode="operatorCode4" operator="operator4"
                             admin="admin4"/>
            <affectedProduct name="name5" num="num5" line="line5" catOut="catOut5" catIn="catIn5" catCode="catCode5"
                             catOutS="catOutS5" catOutL="catOutL5" operatorCode="operatorCode5" operator="operator5"
                             admin="admin5"/>
            <affectedProduct name="name6" num="num6" line="line6" catOut="catOut6" catIn="catIn6" catCode="catCode6"
                             catOutS="catOutS6" catOutL="catOutL6" operatorCode="operatorCode6" operator="operator6"
                             admin="admin6"/>
        </Message>
        <Message id="id3" externalId="externalId3" act="true" pub="pub3" head="head3" lead="lead3" text="text3"
                 tckr="tckr3" company="company3" category="category3" priority="2147483647" products="2147483647"
                 icon="icon3" routeIdxFrom="2147483647" routeIdxTo="2147483647" sTime="sTime3" sDate="sDate3"
                 eTime="eTime3" eDate="eDate3" altStart="altStart3" altEnd="altEnd3">
            <affectedProduct name="name7" num="num7" line="line7" catOut="catOut7" catIn="catIn7" catCode="catCode7"
                             catOutS="catOutS7" catOutL="catOutL7" operatorCode="operatorCode7" operator="operator7"
                             admin="admin7"/>
            <affectedProduct name="name8" num="num8" line="line8" catOut="catOut8" catIn="catIn8" catCode="catCode8"
                             catOutS="catOutS8" catOutL="catOutL8" operatorCode="operatorCode8" operator="operator8"
                             admin="admin8"/>
            <affectedProduct name="name9" num="num9" line="line9" catOut="catOut9" catIn="catIn9" catCode="catCode9"
                             catOutS="catOutS9" catOutL="catOutL9" operatorCode="operatorCode9" operator="operator9"
                             admin="admin9"/>
        </Message>
    </Messages>
    <Eco co2="0.0" part="0.0" partV="0.0" nmhc="0.0" nox="0.0" prime="0.0" so2="0.0"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin1" planningPeriodEnd="planningPeriodEnd1" sDaysR="sDaysR1"
                 sDaysI="sDaysI1" sDaysB="sDaysB1" routeIdxFrom="1" routeIdxTo="1"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin2" planningPeriodEnd="planningPeriodEnd2" sDaysR="sDaysR2"
                 sDaysI="sDaysI2" sDaysB="sDaysB2" routeIdxFrom="-2147483647" routeIdxTo="-2147483647"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin3" planningPeriodEnd="planningPeriodEnd3" sDaysR="sDaysR3"
                 sDaysI="sDaysI3" sDaysB="sDaysB3" routeIdxFrom="2147483647" routeIdxTo="2147483647"/>
    <LegList>
        <Leg idx="anySimpleType" name="name1" number="number1" category="category1" type="type1" cancelled="false"
             partCancelled="false" reachable="true" direction="direction1" duration="P396DT1H1M1S" dist="1">
            <Origin name="name1" type="ST" id="id1" extId="extId1" lon="1" lat="1" routeIdx="1"
                    prognosisType="PROGNOSED" time="time1" date="date1" tz="0" track="track1" rtTime="rtTime1"
                    rtDate="rtDate1" rtTz="0" rtTrack="rtTrack1" hasMainMast="true" mainMastId="mainMastId1"
                    mainMastExtId="mainMastExtId1">
                <Notes>
                    <Note key="key1" type="U" priority="1" routeIdxFrom="1" routeIdxTo="1">Note1</Note>
                    <Note key="key2" type="A" priority="-2147483647" routeIdxFrom="-2147483647"
                          routeIdxTo="-2147483647">Note2
                    </Note>
                    <Note key="key3" type="I" priority="2147483647" routeIdxFrom="2147483647" routeIdxTo="2147483647">
                        Note3
                    </Note>
                </Notes>
            </Origin>
            <Destination name="name1" type="ST" id="id1" extId="extId1" lon="1" lat="1" routeIdx="1"
                         prognosisType="PROGNOSED" time="time1" date="date1" tz="0" track="track1" rtTime="rtTime1"
                         rtDate="rtDate1" rtTz="0" rtTrack="rtTrack1" hasMainMast="true" mainMastId="mainMastId1"
                         mainMastExtId="mainMastExtId1"/>
            <JourneyDetailRef ref="ref1"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref1"/>
            <GisRoute dist="1" durS="P396DT1H1M1S" durR="P396DT1H1M1S" durST="P396DT1H1M1S" durW2C="P396DT1H1M1S"
                      durW2D="P396DT1H1M1S" dirTxt="dirTxt1" dirGeo="1">
                <seg name="name1" rType="U" rNum="rNum1" man="NO" manTx="manTx1" dirTx="dirTx1" ori="U" polyS="1"
                     polyE="1" dist="1"/>
                <seg name="name2" rType="M" rNum="rNum2" man="FR" manTx="manTx2" dirTx="dirTx2" ori="N"
                     polyS="-2147483647" polyE="-2147483647" dist="-2147483647"/>
                <seg name="name3" rType="H" rNum="rNum3" man="TO" manTx="manTx3" dirTx="dirTx3" ori="S"
                     polyS="2147483647" polyE="2147483647" dist="2147483647"/>
                <polyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                          crdEncS="crdEncS1">
                    <crd>1</crd>
                    <crd>-2147483647</crd>
                    <crd>2147483647</crd>
                </polyline>
                <altPolyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                             crdEncS="crdEncS1">
                    <crd>1</crd>
                    <crd>-2147483647</crd>
                    <crd>2147483647</crd>
                </altPolyline>
                <altPolyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                             crdEncS="crdEncS2">
                    <crd>0</crd>
                    <crd>2</crd>
                    <crd>-2147483646</crd>
                </altPolyline>
                <altPolyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3"
                             crdEncZ="crdEncZ3" crdEncS="crdEncS3">
                    <crd>2147483646</crd>
                    <crd>-1</crd>
                    <crd>3</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>P</JourneyStatus>
            <Product name="name1" num="num1" line="line1" catOut="catOut1" catIn="catIn1" catCode="catCode1"
                     catOutS="catOutS1" catOutL="catOutL1" operatorCode="operatorCode1" operator="operator1"
                     admin="admin1"/>
            <Polyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                      crdEncS="crdEncS1">
                <crd>1</crd>
                <crd>-2147483647</crd>
                <crd>2147483647</crd>
            </Polyline>
            <Stops>
                <Stop name="name1" id="id1" extId="extId1" routeIdx="1" lon="1" lat="1" arrPrognosisType="PROGNOSED"
                      depPrognosisType="PROGNOSED" depTime="depTime1" depDate="depDate1" depTz="0" arrTime="arrTime1"
                      arrDate="arrDate1" arrTz="0" passingTime="passingTime1" passingDate="passingDate1" passingTz="0"
                      arrTrack="arrTrack1" depTrack="depTrack1" rtDepTime="rtDepTime1" rtDepDate="rtDepDate1"
                      rtDepTz="0" rtArrTime="rtArrTime1" rtArrDate="rtArrDate1" rtArrTz="0" rtArrTrack="rtArrTrack1"
                      rtDepTrack="rtDepTrack1" rtPassingTime="rtPassingTime1" rtPassingDate="rtPassingDate1"
                      rtPassingTz="0" cancelled="false" hasMainMast="true" mainMastId="mainMastId1"
                      mainMastExtId="mainMastExtId1"/>
                <Stop name="name2" id="id2" extId="extId2" routeIdx="-2147483647" lon="-79228162514264337593543950335"
                      lat="-79228162514264337593543950335" arrPrognosisType="MANUAL" depPrognosisType="MANUAL"
                      depTime="depTime2" depDate="depDate2" depTz="1" arrTime="arrTime2" arrDate="arrDate2" arrTz="1"
                      passingTime="passingTime2" passingDate="passingDate2" passingTz="1" arrTrack="arrTrack2"
                      depTrack="depTrack2" rtDepTime="rtDepTime2" rtDepDate="rtDepDate2" rtDepTz="1"
                      rtArrTime="rtArrTime2" rtArrDate="rtArrDate2" rtArrTz="1" rtArrTrack="rtArrTrack2"
                      rtDepTrack="rtDepTrack2" rtPassingTime="rtPassingTime2" rtPassingDate="rtPassingDate2"
                      rtPassingTz="1" cancelled="true" hasMainMast="false" mainMastId="mainMastId2"
                      mainMastExtId="mainMastExtId2"/>
                <Stop name="name3" id="id3" extId="extId3" routeIdx="2147483647" lon="79228162514264337593543950335"
                      lat="79228162514264337593543950335" arrPrognosisType="REPORTED" depPrognosisType="REPORTED"
                      depTime="depTime3" depDate="depDate3" depTz="-2147483647" arrTime="arrTime3" arrDate="arrDate3"
                      arrTz="-2147483647" passingTime="passingTime3" passingDate="passingDate3" passingTz="-2147483647"
                      arrTrack="arrTrack3" depTrack="depTrack3" rtDepTime="rtDepTime3" rtDepDate="rtDepDate3"
                      rtDepTz="-2147483647" rtArrTime="rtArrTime3" rtArrDate="rtArrDate3" rtArrTz="-2147483647"
                      rtArrTrack="rtArrTrack3" rtDepTrack="rtDepTrack3" rtPassingTime="rtPassingTime3"
                      rtPassingDate="rtPassingDate3" rtPassingTz="-2147483647" cancelled="false" hasMainMast="true"
                      mainMastId="mainMastId3" mainMastExtId="mainMastExtId3"/>
            </Stops>
        </Leg>
        <Leg idx="anySimpleType" name="name2" number="number2" category="category2" type="type2" cancelled="true"
             partCancelled="true" reachable="true" direction="direction2" duration="-P10675199DT2H48M5.477S"
             dist="-2147483647">
            <Origin name="name2" type="ADR" id="id2" extId="extId2" lon="-79228162514264337593543950335"
                    lat="-79228162514264337593543950335" routeIdx="-2147483647" prognosisType="MANUAL" time="time2"
                    date="date2" tz="1" track="track2" rtTime="rtTime2" rtDate="rtDate2" rtTz="1" rtTrack="rtTrack2"
                    hasMainMast="false" mainMastId="mainMastId2" mainMastExtId="mainMastExtId2">
                <Notes>
                    <Note key="key4" type="R" priority="0" routeIdxFrom="0" routeIdxTo="0">Note4</Note>
                    <Note key="key5" type="H" priority="2" routeIdxFrom="2" routeIdxTo="2">Note5</Note>
                    <Note key="key6" type="U" priority="-2147483646" routeIdxFrom="-2147483646"
                          routeIdxTo="-2147483646">Note6
                    </Note>
                </Notes>
            </Origin>
            <Destination name="name2" type="ADR" id="id2" extId="extId2" lon="-79228162514264337593543950335"
                         lat="-79228162514264337593543950335" routeIdx="-2147483647" prognosisType="MANUAL" time="time2"
                         date="date2" tz="1" track="track2" rtTime="rtTime2" rtDate="rtDate2" rtTz="1"
                         rtTrack="rtTrack2" hasMainMast="false" mainMastId="mainMastId2"
                         mainMastExtId="mainMastExtId2"/>
            <JourneyDetailRef ref="ref2"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref2"/>
            <GisRoute dist="-2147483647" durS="-P10675199DT2H48M5.477S" durR="-P10675199DT2H48M5.477S"
                      durST="-P10675199DT2H48M5.477S" durW2C="-P10675199DT2H48M5.477S" durW2D="-P10675199DT2H48M5.477S"
                      dirTxt="dirTxt2" dirGeo="-2147483647">
                <seg name="name4" rType="T" rNum="rNum4" man="ON" manTx="manTx4" dirTx="dirTx4" ori="E" polyS="0"
                     polyE="0" dist="0"/>
                <seg name="name5" rType="T4L" rNum="rNum5" man="LE" manTx="manTx5" dirTx="dirTx5" ori="W" polyS="2"
                     polyE="2" dist="2"/>
                <seg name="name6" rType="T2L" rNum="rNum6" man="RI" manTx="manTx6" dirTx="dirTx6" ori="NE"
                     polyS="-2147483646" polyE="-2147483646" dist="-2147483646"/>
                <polyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                          crdEncS="crdEncS2">
                    <crd>0</crd>
                    <crd>2</crd>
                    <crd>-2147483646</crd>
                </polyline>
                <altPolyline name="name4" delta="false" dim="2147483647" type="HAFASGEO" crdEncYX="crdEncYX4"
                             crdEncZ="crdEncZ4" crdEncS="crdEncS4">
                    <crd>-2147483645</crd>
                    <crd>2147483645</crd>
                    <crd>-2</crd>
                </altPolyline>
                <altPolyline name="name5" delta="true" dim="0" type="WGS84" crdEncYX="crdEncYX5" crdEncZ="crdEncZ5"
                             crdEncS="crdEncS5">
                    <crd>4</crd>
                    <crd>-2147483644</crd>
                    <crd>2147483644</crd>
                </altPolyline>
                <altPolyline name="name6" delta="false" dim="2" type="PLANAR" crdEncYX="crdEncYX6" crdEncZ="crdEncZ6"
                             crdEncS="crdEncS6">
                    <crd>-3</crd>
                    <crd>5</crd>
                    <crd>-2147483643</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>R</JourneyStatus>
            <Product name="name2" num="num2" line="line2" catOut="catOut2" catIn="catIn2" catCode="catCode2"
                     catOutS="catOutS2" catOutL="catOutL2" operatorCode="operatorCode2" operator="operator2"
                     admin="admin2"/>
            <Polyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                      crdEncS="crdEncS2">
                <crd>0</crd>
                <crd>2</crd>
                <crd>-2147483646</crd>
            </Polyline>
            <Stops>
                <Stop name="name4" id="id4" extId="extId4" routeIdx="0" lon="0.9" lat="0.9" arrPrognosisType="CORRECTED"
                      depPrognosisType="CORRECTED" depTime="depTime4" depDate="depDate4" depTz="2147483647"
                      arrTime="arrTime4" arrDate="arrDate4" arrTz="2147483647" passingTime="passingTime4"
                      passingDate="passingDate4" passingTz="2147483647" arrTrack="arrTrack4" depTrack="depTrack4"
                      rtDepTime="rtDepTime4" rtDepDate="rtDepDate4" rtDepTz="2147483647" rtArrTime="rtArrTime4"
                      rtArrDate="rtArrDate4" rtArrTz="2147483647" rtArrTrack="rtArrTrack4" rtDepTrack="rtDepTrack4"
                      rtPassingTime="rtPassingTime4" rtPassingDate="rtPassingDate4" rtPassingTz="2147483647"
                      cancelled="true" hasMainMast="false" mainMastId="mainMastId4" mainMastExtId="mainMastExtId4"/>
                <Stop name="name5" id="id5" extId="extId5" routeIdx="2" lon="1.1" lat="1.1"
                      arrPrognosisType="CALCULATED" depPrognosisType="CALCULATED" depTime="depTime5" depDate="depDate5"
                      depTz="0" arrTime="arrTime5" arrDate="arrDate5" arrTz="0" passingTime="passingTime5"
                      passingDate="passingDate5" passingTz="0" arrTrack="arrTrack5" depTrack="depTrack5"
                      rtDepTime="rtDepTime5" rtDepDate="rtDepDate5" rtDepTz="0" rtArrTime="rtArrTime5"
                      rtArrDate="rtArrDate5" rtArrTz="0" rtArrTrack="rtArrTrack5" rtDepTrack="rtDepTrack5"
                      rtPassingTime="rtPassingTime5" rtPassingDate="rtPassingDate5" rtPassingTz="0" cancelled="false"
                      hasMainMast="true" mainMastId="mainMastId5" mainMastExtId="mainMastExtId5"/>
                <Stop name="name6" id="id6" extId="extId6" routeIdx="-2147483646" lon="-79228162514264337593543950335"
                      lat="-79228162514264337593543950335" arrPrognosisType="PROGNOSED" depPrognosisType="PROGNOSED"
                      depTime="depTime6" depDate="depDate6" depTz="2" arrTime="arrTime6" arrDate="arrDate6" arrTz="2"
                      passingTime="passingTime6" passingDate="passingDate6" passingTz="2" arrTrack="arrTrack6"
                      depTrack="depTrack6" rtDepTime="rtDepTime6" rtDepDate="rtDepDate6" rtDepTz="2"
                      rtArrTime="rtArrTime6" rtArrDate="rtArrDate6" rtArrTz="2" rtArrTrack="rtArrTrack6"
                      rtDepTrack="rtDepTrack6" rtPassingTime="rtPassingTime6" rtPassingDate="rtPassingDate6"
                      rtPassingTz="2" cancelled="true" hasMainMast="false" mainMastId="mainMastId6"
                      mainMastExtId="mainMastExtId6"/>
            </Stops>
        </Leg>
        <Leg idx="anySimpleType" name="name3" number="number3" category="category3" type="type3" cancelled="false"
             partCancelled="false" reachable="false" direction="direction3" duration="P10675199DT2H48M5.477S"
             dist="2147483647">
            <Origin name="name3" type="POI" id="id3" extId="extId3" lon="79228162514264337593543950335"
                    lat="79228162514264337593543950335" routeIdx="2147483647" prognosisType="REPORTED" time="time3"
                    date="date3" tz="-2147483647" track="track3" rtTime="rtTime3" rtDate="rtDate3" rtTz="-2147483647"
                    rtTrack="rtTrack3" hasMainMast="true" mainMastId="mainMastId3" mainMastExtId="mainMastExtId3">
                <Notes>
                    <Note key="key7" type="A" priority="2147483646" routeIdxFrom="2147483646" routeIdxTo="2147483646">
                        Note7
                    </Note>
                    <Note key="key8" type="I" priority="-1" routeIdxFrom="-1" routeIdxTo="-1">Note8</Note>
                    <Note key="key9" type="R" priority="3" routeIdxFrom="3" routeIdxTo="3">Note9</Note>
                </Notes>
            </Origin>
            <Destination name="name3" type="POI" id="id3" extId="extId3" lon="79228162514264337593543950335"
                         lat="79228162514264337593543950335" routeIdx="2147483647" prognosisType="REPORTED" time="time3"
                         date="date3" tz="-2147483647" track="track3" rtTime="rtTime3" rtDate="rtDate3"
                         rtTz="-2147483647" rtTrack="rtTrack3" hasMainMast="true" mainMastId="mainMastId3"
                         mainMastExtId="mainMastExtId3"/>
            <JourneyDetailRef ref="ref3"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref3"/>
            <GisRoute dist="2147483647" durS="P10675199DT2H48M5.477S" durR="P10675199DT2H48M5.477S"
                      durST="P10675199DT2H48M5.477S" durW2C="P10675199DT2H48M5.477S" durW2D="P10675199DT2H48M5.477S"
                      dirTxt="dirTxt3" dirGeo="2147483647">
                <seg name="name7" rType="TR" rNum="rNum7" man="KL" manTx="manTx7" dirTx="dirTx7" ori="SE"
                     polyS="2147483646" polyE="2147483646" dist="2147483646"/>
                <seg name="name8" rType="NT" rNum="rNum8" man="KR" manTx="manTx8" dirTx="dirTx8" ori="NW" polyS="-1"
                     polyE="-1" dist="-1"/>
                <seg name="name9" rType="CT" rNum="rNum9" man="HL" manTx="manTx9" dirTx="dirTx9" ori="SW" polyS="3"
                     polyE="3" dist="3"/>
                <polyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3"
                          crdEncZ="crdEncZ3" crdEncS="crdEncS3">
                    <crd>2147483646</crd>
                    <crd>-1</crd>
                    <crd>3</crd>
                </polyline>
                <altPolyline name="name7" delta="true" dim="-2147483646" type="HAFASGEO" crdEncYX="crdEncYX7"
                             crdEncZ="crdEncZ7" crdEncS="crdEncS7">
                    <crd>2147483643</crd>
                    <crd>-4</crd>
                    <crd>6</crd>
                </altPolyline>
                <altPolyline name="name8" delta="false" dim="2147483646" type="WGS84" crdEncYX="crdEncYX8"
                             crdEncZ="crdEncZ8" crdEncS="crdEncS8">
                    <crd>-2147483642</crd>
                    <crd>2147483642</crd>
                    <crd>-5</crd>
                </altPolyline>
                <altPolyline name="name9" delta="true" dim="-1" type="PLANAR" crdEncYX="crdEncYX9" crdEncZ="crdEncZ9"
                             crdEncS="crdEncS9">
                    <crd>7</crd>
                    <crd>-2147483641</crd>
                    <crd>2147483641</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>A</JourneyStatus>
            <Product name="name3" num="num3" line="line3" catOut="catOut3" catIn="catIn3" catCode="catCode3"
                     catOutS="catOutS3" catOutL="catOutL3" operatorCode="operatorCode3" operator="operator3"
                     admin="admin3"/>
            <Polyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3" crdEncZ="crdEncZ3"
                      crdEncS="crdEncS3">
                <crd>2147483646</crd>
                <crd>-1</crd>
                <crd>3</crd>
            </Polyline>
            <Stops>
                <Stop name="name7" id="id7" extId="extId7" routeIdx="2147483646" lon="79228162514264337593543950335"
                      lat="79228162514264337593543950335" arrPrognosisType="MANUAL" depPrognosisType="MANUAL"
                      depTime="depTime7" depDate="depDate7" depTz="-2147483646" arrTime="arrTime7" arrDate="arrDate7"
                      arrTz="-2147483646" passingTime="passingTime7" passingDate="passingDate7" passingTz="-2147483646"
                      arrTrack="arrTrack7" depTrack="depTrack7" rtDepTime="rtDepTime7" rtDepDate="rtDepDate7"
                      rtDepTz="-2147483646" rtArrTime="rtArrTime7" rtArrDate="rtArrDate7" rtArrTz="-2147483646"
                      rtArrTrack="rtArrTrack7" rtDepTrack="rtDepTrack7" rtPassingTime="rtPassingTime7"
                      rtPassingDate="rtPassingDate7" rtPassingTz="-2147483646" cancelled="false" hasMainMast="true"
                      mainMastId="mainMastId7" mainMastExtId="mainMastExtId7"/>
                <Stop name="name8" id="id8" extId="extId8" routeIdx="-1" lon="0.8" lat="0.8" arrPrognosisType="REPORTED"
                      depPrognosisType="REPORTED" depTime="depTime8" depDate="depDate8" depTz="2147483646"
                      arrTime="arrTime8" arrDate="arrDate8" arrTz="2147483646" passingTime="passingTime8"
                      passingDate="passingDate8" passingTz="2147483646" arrTrack="arrTrack8" depTrack="depTrack8"
                      rtDepTime="rtDepTime8" rtDepDate="rtDepDate8" rtDepTz="2147483646" rtArrTime="rtArrTime8"
                      rtArrDate="rtArrDate8" rtArrTz="2147483646" rtArrTrack="rtArrTrack8" rtDepTrack="rtDepTrack8"
                      rtPassingTime="rtPassingTime8" rtPassingDate="rtPassingDate8" rtPassingTz="2147483646"
                      cancelled="true" hasMainMast="false" mainMastId="mainMastId8" mainMastExtId="mainMastExtId8"/>
                <Stop name="name9" id="id9" extId="extId9" routeIdx="3" lon="1.2" lat="1.2" arrPrognosisType="CORRECTED"
                      depPrognosisType="CORRECTED" depTime="depTime9" depDate="depDate9" depTz="-1" arrTime="arrTime9"
                      arrDate="arrDate9" arrTz="-1" passingTime="passingTime9" passingDate="passingDate9" passingTz="-1"
                      arrTrack="arrTrack9" depTrack="depTrack9" rtDepTime="rtDepTime9" rtDepDate="rtDepDate9"
                      rtDepTz="-1" rtArrTime="rtArrTime9" rtArrDate="rtArrDate9" rtArrTz="-1" rtArrTrack="rtArrTrack9"
                      rtDepTrack="rtDepTrack9" rtPassingTime="rtPassingTime9" rtPassingDate="rtPassingDate9"
                      rtPassingTz="-1" cancelled="false" hasMainMast="true" mainMastId="mainMastId9"
                      mainMastExtId="mainMastExtId9"/>
            </Stops>
        </Leg>
    </LegList>
    <TariffResult>
        <fareSetItem name="name1" desc="desc1">
            <ticketParam name="name1" value="value1"/>
            <ticketParam name="name2" value="value2"/>
            <ticketParam name="name3" value="value3"/>
            <fareItem name="name1" desc="desc1" price="0" cur="cur1" shpCtx="shpCtx1">
                <ticket name="name1" desc="desc1" price="0" cur="cur1" shpCtx="shpCtx1">
                    <ticketParam name="name1" value="value1"/>
                    <ticketParam name="name2" value="value2"/>
                    <ticketParam name="name3" value="value3"/>
                </ticket>
                <ticket name="name2" desc="desc2" price="1" cur="cur2" shpCtx="shpCtx2">
                    <ticketParam name="name4" value="value4"/>
                    <ticketParam name="name5" value="value5"/>
                    <ticketParam name="name6" value="value6"/>
                </ticket>
                <ticket name="name3" desc="desc3" price="-2147483647" cur="cur3" shpCtx="shpCtx3">
                    <ticketParam name="name7" value="value7"/>
                    <ticketParam name="name8" value="value8"/>
                    <ticketParam name="name9" value="value9"/>
                </ticket>
            </fareItem>
            <fareItem name="name2" desc="desc2" price="1" cur="cur2" shpCtx="shpCtx2">
                <ticket name="name4" desc="desc4" price="2147483647" cur="cur4" shpCtx="shpCtx4">
                    <ticketParam name="name10" value="value10"/>
                    <ticketParam name="name11" value="value11"/>
                    <ticketParam name="name12" value="value12"/>
                </ticket>
                <ticket name="name5" desc="desc5" price="0" cur="cur5" shpCtx="shpCtx5">
                    <ticketParam name="name13" value="value13"/>
                    <ticketParam name="name14" value="value14"/>
                    <ticketParam name="name15" value="value15"/>
                </ticket>
                <ticket name="name6" desc="desc6" price="2" cur="cur6" shpCtx="shpCtx6">
                    <ticketParam name="name16" value="value16"/>
                    <ticketParam name="name17" value="value17"/>
                    <ticketParam name="name18" value="value18"/>
                </ticket>
            </fareItem>
            <fareItem name="name3" desc="desc3" price="-2147483647" cur="cur3" shpCtx="shpCtx3">
                <ticket name="name7" desc="desc7" price="-2147483646" cur="cur7" shpCtx="shpCtx7">
                    <ticketParam name="name19" value="value19"/>
                    <ticketParam name="name20" value="value20"/>
                    <ticketParam name="name21" value="value21"/>
                </ticket>
                <ticket name="name8" desc="desc8" price="2147483646" cur="cur8" shpCtx="shpCtx8">
                    <ticketParam name="name22" value="value22"/>
                    <ticketParam name="name23" value="value23"/>
                    <ticketParam name="name24" value="value24"/>
                </ticket>
                <ticket name="name9" desc="desc9" price="-1" cur="cur9" shpCtx="shpCtx9">
                    <ticketParam name="name25" value="value25"/>
                    <ticketParam name="name26" value="value26"/>
                    <ticketParam name="name27" value="value27"/>
                </ticket>
            </fareItem>
        </fareSetItem>
        <fareSetItem name="name2" desc="desc2">
            <ticketParam name="name4" value="value4"/>
            <ticketParam name="name5" value="value5"/>
            <ticketParam name="name6" value="value6"/>
            <fareItem name="name4" desc="desc4" price="2147483647" cur="cur4" shpCtx="shpCtx4">
                <ticket name="name10" desc="desc10" price="3" cur="cur10" shpCtx="shpCtx10">
                    <ticketParam name="name28" value="value28"/>
                    <ticketParam name="name29" value="value29"/>
                    <ticketParam name="name30" value="value30"/>
                </ticket>
                <ticket name="name11" desc="desc11" price="-2147483645" cur="cur11" shpCtx="shpCtx11">
                    <ticketParam name="name31" value="value31"/>
                    <ticketParam name="name32" value="value32"/>
                    <ticketParam name="name33" value="value33"/>
                </ticket>
                <ticket name="name12" desc="desc12" price="2147483645" cur="cur12" shpCtx="shpCtx12">
                    <ticketParam name="name34" value="value34"/>
                    <ticketParam name="name35" value="value35"/>
                    <ticketParam name="name36" value="value36"/>
                </ticket>
            </fareItem>
            <fareItem name="name5" desc="desc5" price="0" cur="cur5" shpCtx="shpCtx5">
                <ticket name="name13" desc="desc13" price="-2" cur="cur13" shpCtx="shpCtx13">
                    <ticketParam name="name37" value="value37"/>
                    <ticketParam name="name38" value="value38"/>
                    <ticketParam name="name39" value="value39"/>
                </ticket>
                <ticket name="name14" desc="desc14" price="4" cur="cur14" shpCtx="shpCtx14">
                    <ticketParam name="name40" value="value40"/>
                    <ticketParam name="name41" value="value41"/>
                    <ticketParam name="name42" value="value42"/>
                </ticket>
                <ticket name="name15" desc="desc15" price="-2147483644" cur="cur15" shpCtx="shpCtx15">
                    <ticketParam name="name43" value="value43"/>
                    <ticketParam name="name44" value="value44"/>
                    <ticketParam name="name45" value="value45"/>
                </ticket>
            </fareItem>
            <fareItem name="name6" desc="desc6" price="2" cur="cur6" shpCtx="shpCtx6">
                <ticket name="name16" desc="desc16" price="2147483644" cur="cur16" shpCtx="shpCtx16">
                    <ticketParam name="name46" value="value46"/>
                    <ticketParam name="name47" value="value47"/>
                    <ticketParam name="name48" value="value48"/>
                </ticket>
                <ticket name="name17" desc="desc17" price="-3" cur="cur17" shpCtx="shpCtx17">
                    <ticketParam name="name49" value="value49"/>
                    <ticketParam name="name50" value="value50"/>
                    <ticketParam name="name51" value="value51"/>
                </ticket>
                <ticket name="name18" desc="desc18" price="5" cur="cur18" shpCtx="shpCtx18">
                    <ticketParam name="name52" value="value52"/>
                    <ticketParam name="name53" value="value53"/>
                    <ticketParam name="name54" value="value54"/>
                </ticket>
            </fareItem>
        </fareSetItem>
        <fareSetItem name="name3" desc="desc3">
            <ticketParam name="name7" value="value7"/>
            <ticketParam name="name8" value="value8"/>
            <ticketParam name="name9" value="value9"/>
            <fareItem name="name7" desc="desc7" price="-2147483646" cur="cur7" shpCtx="shpCtx7">
                <ticket name="name19" desc="desc19" price="-2147483643" cur="cur19" shpCtx="shpCtx19">
                    <ticketParam name="name55" value="value55"/>
                    <ticketParam name="name56" value="value56"/>
                    <ticketParam name="name57" value="value57"/>
                </ticket>
                <ticket name="name20" desc="desc20" price="2147483643" cur="cur20" shpCtx="shpCtx20">
                    <ticketParam name="name58" value="value58"/>
                    <ticketParam name="name59" value="value59"/>
                    <ticketParam name="name60" value="value60"/>
                </ticket>
                <ticket name="name21" desc="desc21" price="-4" cur="cur21" shpCtx="shpCtx21">
                    <ticketParam name="name61" value="value61"/>
                    <ticketParam name="name62" value="value62"/>
                    <ticketParam name="name63" value="value63"/>
                </ticket>
            </fareItem>
            <fareItem name="name8" desc="desc8" price="2147483646" cur="cur8" shpCtx="shpCtx8">
                <ticket name="name22" desc="desc22" price="6" cur="cur22" shpCtx="shpCtx22">
                    <ticketParam name="name64" value="value64"/>
                    <ticketParam name="name65" value="value65"/>
                    <ticketParam name="name66" value="value66"/>
                </ticket>
                <ticket name="name23" desc="desc23" price="-2147483642" cur="cur23" shpCtx="shpCtx23">
                    <ticketParam name="name67" value="value67"/>
                    <ticketParam name="name68" value="value68"/>
                    <ticketParam name="name69" value="value69"/>
                </ticket>
                <ticket name="name24" desc="desc24" price="2147483642" cur="cur24" shpCtx="shpCtx24">
                    <ticketParam name="name70" value="value70"/>
                    <ticketParam name="name71" value="value71"/>
                    <ticketParam name="name72" value="value72"/>
                </ticket>
            </fareItem>
            <fareItem name="name9" desc="desc9" price="-1" cur="cur9" shpCtx="shpCtx9">
                <ticket name="name25" desc="desc25" price="-5" cur="cur25" shpCtx="shpCtx25">
                    <ticketParam name="name73" value="value73"/>
                    <ticketParam name="name74" value="value74"/>
                    <ticketParam name="name75" value="value75"/>
                </ticket>
                <ticket name="name26" desc="desc26" price="7" cur="cur26" shpCtx="shpCtx26">
                    <ticketParam name="name76" value="value76"/>
                    <ticketParam name="name77" value="value77"/>
                    <ticketParam name="name78" value="value78"/>
                </ticket>
                <ticket name="name27" desc="desc27" price="-2147483641" cur="cur27" shpCtx="shpCtx27">
                    <ticketParam name="name79" value="value79"/>
                    <ticketParam name="name80" value="value80"/>
                    <ticketParam name="name81" value="value81"/>
                </ticket>
            </fareItem>
        </fareSetItem>
    </TariffResult>
</Trip>
```

## JourneyDetail

<p>Journeydetail används för att få detaljerad information kring en resa/delresa (<em>Leg</em>)</p>
<p>Detta bygger på att man först anropat trip. (Se 2.4)</p>
<p>I svaret från trip får man en referens, t.ex.</p>

```xml
<JourneyDetailRef ref="1|3598|0|74|13062017">
```
<p>Denna referens använder man när man ska anropa Journeydetail för den specifika resan. Hela linjesträckningen
    för angiven resa returneras, önskar man bara information om hållplatser i den del av resa som en sökning
    med trip ger rekomenderas att sätta passlist=1 i trip. Detta är en utökning från api-version
    2.</p>
<h3>Parametrar</h3>
<table>
    <tbody>
    <tr>
        <td>
            <p><strong>Namn</strong></p>
        </td>
        <td>
            <p><strong>Beskrivning</strong></p>
        </td>
        <td>
            <p><strong>Kommentar </strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>id</p>
        </td>
        <td>
            <p>Referensen från Trip, se ovan</p>
        </td>
        <td>
            <p>It may be necessary to escape the | character by its URL encoding %7C.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>date</p>
        </td>
        <td>
            <p>åååå-MM-DD</p>
        </td>
        <td>
            <p>Valfritt</p>
            <p>Ger motsvarande resa annan dag, om möjligt</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>poly</p>
        </td>
        <td>
            <p>0 eller 1</p>
        </td>
        <td>
            <p>Valfritt.</p>
            <p>Anger om detaljerade färdvägar ska beräknas för resultaten. För beskrivning av
                polyline se 2.4.5. Default 0.</p>
        </td>
    </tr>
    </tbody>
</table>

Exempel:

```text
api.sl.se/api2/TravelplannerV3_1/journeydetail.&lt;FORMAT&gt;?key=&lt;DIN API NYCKEL&gt;&amp;id=1|3598|0|74|13062017
```

<h3>Realtid</h3>
<p>Om det finns realtid så anges detta i separata extra fält. För realtidstider i journeyDetail så
    läggs &rdquo;rtArrTime&rdquo;, &rdquo;rtArrDate&rdquo;, &rdquo;rtDepTime&rdquo; och &rdquo;rtDepDate&rdquo;
    till i svaret. De gamla fälten &rdquo;arrTime&rdquo;, &rdquo;arrDate&rdquo;, &rdquo;depTime&rdquo; och &rdquo;depDate&rdquo;
    är kvar så att man vet vad det ändrats från/till.</p>
<h3>Svarsstruktur</h3>
<p>I nedan tabell beskrivs den xml struktur som finns. Vissa uppenbara attribut är inte med då det blir väldigt
    mycket annars, som t.ex. Lat och Lon för att ge en lättare överblick av det som är mindre självklart.</p>
<p><strong>Exempel förklaring av nedan struktur i tabellen:</strong><br/> element1/element2 =&gt; element2 är
    ett underelement till element1.<br/> element1.attribut1 =&gt; attribut1 är ett attribut till element1.</p>
<table>
    <tbody>
    <tr>
        <td>
            <p><strong>Namn</strong></p>
        </td>
        <td>
            <p><strong>Datatyp</strong></p>
        </td>
        <td>
            <p><strong>Beskrivning</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>JourneyDetail</p>
        </td>
        <td>
            <p>Element</p>
        </td>
        <td>
            <p>Rootelement.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>JourneyDetail/Notes</p>
        </td>
        <td>
            <p>Element</p>
        </td>
        <td>
            <p>Innehåller noteringar att visas för resan.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>JourneyDetail/Stops</p>
        </td>
        <td>
            <p>Lista av element</p>
        </td>
        <td>
            <p>Lista på hållplatser för den här resan.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Stops/Stop</p>
        </td>
        <td>
            <p>Element</p>
        </td>
        <td>
            <p>Stop innehåller namn på hållplats, route index, latitud, longitud, avgångens
                datum och tid, ankomstens datum och tid.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Stop.id</p>
        </td>
        <td>
            <p>Attribute</p>
        </td>
        <td>
            <p>Id för angiven plats i hållplatslistan. Kan användas för vidare resa från den
                punkten.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Stop.routeIdx</p>
        </td>
        <td>
            <p>Attribute</p>
        </td>
        <td>
            <p>Denna används i samband med routeIdx som finns i Trip svaret i en sökning, för att veta
                vilken del av listan som är aktuell för resan.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>JourneyDetail/Directions</p>
        </td>
        <td>
            <p>Lista av element</p>
        </td>
        <td>
            <p>Lista på riktingar</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Directions/Direction</p>
        </td>
        <td>
            <p>Element</p>
        </td>
        <td>
            <p>Riktningsinformation.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>JourneyDetail/Types</p>
        </td>
        <td>
            <p>Lista av element</p>
        </td>
        <td>
            <p>Lista av restyper.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>JourneyDetail/Names</p>
        </td>
        <td>
            <p>Lista av element</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Names/Name</p>
        </td>
        <td>
            <p>Element</p>
        </td>
        <td>
            <p>Innehåller resans namn.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>JourneyDetail/Messages</p>
        </td>
        <td>
            <p>Lista av element</p>
        </td>
        <td>
            <p>Innehåller en lista med realtidsmeddelanden att visa.</p>
        </td>
    </tr>
    <tr>
        <td>
            <p>Polyline</p>
        </td>
        <td>
            <p>Element</p>
        </td>
        <td>
            <p>Detaljerad färdväg, om poly=1 angivits.</p>
        </td>
    </tr>
    </tbody>
</table>

## GisRoute

<p><br />
Tjänsten används för att få detaljerad information om färdväg.<br />
Eftersom Trip inte returnerar polyline för gångväg och cykel så används detta framför allt för att rita ut cykel och gångväg på karta.<br />
<br />
I svaret från trip fås en delresa:</p>

```xml

<Leg type="WALK" idx="1" dist="464" duration="PT6M" name="">
    <Origin id="A=1@O=Stockholm City@X=18059500@Y=59331143@U=74@L=400105313@" extId="400105313" name="Stockholm City"
            type="ST" lon="18.0595" lat="59.331143" hasMainMast="true"
            mainMastId="A=1@O=Centralen (Stockholm)@X=18057657@Y=59331134@U=74@L=300101002@" mainMastExtId="300101002"
            date="2019-02-12" time="08:45:00"/>
    <Destination id="A=2@O=Stockholm, Drottninggatan 22@l=@X=18065001@Y=59330415@u=0@"
                 name="Stockholm, Drottninggatan 22" type="ADR" lon="18.065001" lat="59.330415" date="2019-02-12"
                 time="08:51:00"/>
    <GisRef ref="G|1|G@F|A=1@O=Stockholm City@X=18059500@Y=59331143@U=74@L=400105313@|A=2@O=Stockholm, Drottninggatan 22@l=@X=18065001@Y=59330415@u=0@|12022019|84500|85100|ft|ft@0@1000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§bt@0@2000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§tt@0@5000@120@-1@100@1@2500@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§|"/>
</Leg>
```

<p>Värdet i ref i objektet GisRef är det som används som input till gisroute</p>
<h3> <a>Parametrar</a></h3>
<table border="0" cellpadding="0" cellspacing="0" >
	<tbody>
		<tr>
			<td>
			<p><b>Namn </b></p>
			</td>
			<td>
			<p><b>Beskrivning</b></p>
			</td>
			<td>
			<p><b>Description </b></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ctx </p>
			</td>
			<td>

			</td>
			<td>
			<p>Värdet i ctxRecon som fås i svaret från trip. </p>
			</td>
		</tr>
		<tr>
			<td>
			<p>lang </p>
			</td>
			<td>
			<p>sv = svenska<br />
			en = engelska </p>
			</td>
			<td>
			<p> </p>
			</td>
		</tr>
		<tr>
			<td>
			<p>poly</p>
			</td>
			<td>
			<p>0 eller 1 </p>
			</td>
			<td>
			<p>Valfritt.</p>
			<p>Anger om detaljerade färdvägar ska beräknas för resultaten. Default 0.</p>

</td>
</tr>
</tbody>
</table>

<p>Exempel:<br />
<br />

```text
http://api.sl.se/api2/TravelplannerV3_1/gisroute.&lt;FORMAT&gt;?key=&lt;DIN APINYCKEL&gt;&amp;ctx=G|1|G@F|A=1@O=Stockholm%20City@X=18059500@Y=59331143@U=74@L=400105313@|A=2@O=Stockholm,%20Drottninggatan%2022@l=@X=18065001@Y=59330415@u=0@|12022019|84500|85100|ft|ft@0@1000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7bt@0@2000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7tt@0@5000@120@-1@100@1@2500@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7%7C&amp;lang=sv&amp;poly=1
```

<h3> <a><span>>Svarsstruktur</a><span>></h3>
<p>Svaret från gisroute är detsamma som för resultatet från trip, med skillnad att det bara är en resa med i resultatet. Det tillkommer även ett objekt för att beskriva färdvägen, GisRoute:</p>

```xml

<GisRoute dist="189" durS="PT2M">
    <seg dist="22" man="ST" manTx="Fortsätt på Renstiernas gata" name="Renstiernas gata" ori="N" polyE="10" polyS="7"
         rType="CT"/>
    <seg man="TO" manTx="Ankomst på Renstiernas gata"/>
    <polyline type="WGS84" dim="3" crdEncS="NNNNNHMNNNN" crdEncZ="???????????" delta="true">
        <crd>18.080803</crd>
        <crd>59.315164</crd>
        <crd>0.0</crd>
        <crd>3.45E-4</crd>
        <crd>4.1E-5</crd>
        <crd>0.0</crd>
        <crd>-2.7E-5</crd>
        <crd>6.1E-5</crd>
        <crd>0.0</crd>
        <crd>9.0E-5</crd>
        <crd>1.1E-5</crd>
        <crd>0.0</crd>
        <crd>2.5E-5</crd>
        <crd>2.7E-5</crd>
        <crd>0.0</crd>
        <crd>9.9E-5</crd>
        <crd>4.0E-6</crd>
        <crd>0.0</crd>
        <crd>1.7E-4</crd>
        <crd>1.5E-5</crd>
        <crd>0.0</crd>
        <crd>0.001985</crd>
        <crd>2.48E-4</crd>
        <crd>0.0</crd>
        <crd>8.8E-5</crd>
        <crd>1.1E-5</crd>
        <crd>0.0</crd>
        <crd>4.0E-5</crd>
        <crd>3.5E-5</crd>
        <crd>0.0</crd>
        <crd>-4.9E-5</crd>
        <crd>1.05E-4</crd>
        <crd>0.0</crd>
    </polyline>
</GisRoute>
```

<p>Segmenten beskriver delar ur resan och polyline beskriver coordinater på samma sätt som dokumenteras i Trip.</p>

<h2>Reconstruction</h2>
<p>För att återskapa en resa framsökt via tjäsnten trip kan tjänsten reconstruction användas (exempelvis för delningsfunktion eller liknande)</p>
<p>I svaret från trip fås:<br />

```xml
<Trip idx="0"ctxRecon="T$A=1@O=T-Centralen@L=400101052@a=128@$A=1@O=Slussen@L=400101012@a=128@$201706140859$201706140902$ $"checksum="774B67E9_4"tripId="C-0"duration="PT3M">
```

<p>Värdet i ctxRecon är det som används som input till reconstruction</p>
<h3> <a>Parametrar</a></h3>
<table>
	<tbody>
		<tr>
			<td>
			<p><b>Namn </b></p>
			</td>
			<td>
			<p><b>Beskrivning</b></p>
			</td>
			<td>
			<p><b>Description </b></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ctx </p>
			</td>
			<td>

			</td>
			<td>
			<p>Värdet i ctxRecon som fås i svaret från trip. </p>
			</td>
		</tr>
		<tr>
			<td>
			<p>poly </p>
			</td>
			<td>
			<p>0 eller 1 </p>
			</td>
			<td>
			<p>Valfritt.</p>
			<p>Anger om detaljerade färdvägar ska beräknas för resultaten.

</td>
</tr>
<tr>
<td>
<p>date </p>
</td>
<td>
<p>Datum </p>
			<p>ÅÅÅÅ-MM-DD </p>
</td>
<td>
<p>Valfritt</p>
			<p>Försöker rekonstruera en resa på specificerat datum, om möjligt.  </p>
</td>
</tr>
</tbody>
</table>

<p><span>>Exempel:</p>

```text
api.sl.se/api2/TravelplannerV3_1/reconstruction.<FORMAT>?key=<DIN API NYCKEL>&amp;ctx=T%24A%3D1%40O%3DT-Centralen%40L%3D400101052%40a%3D128%40%24A%3D1%40O%3DSlussen%40L%3D400101012%40a%3D128%40%24201706140859%24201706140902%24%20%24
```
<h3>Svarsstruktur</h3>
<p>Svaret från reconstruction är detsamma som för resultatet från trip, med skillnad att det bara är en resa med i resultatet.</p>
<h2> <a>XSD</a></h2>
<p>Returnerar en xsd innehållandes definioner för alla de ingående delarna av svarsstrukturerna för tjänsterna i SL Reseplanerare 3.</p>
<h3> <a>Parametrar</a></h3>
<p>Inga specifika parametrar används för denna tjänst</p>

<p>Exempel:</p>

```text
api.sl.se/api2/TravelplannerV3_1/xsd.xml?key=<DIN API NYCKEL>.xsd
```

<h2>TTI – Time table info</h2>
<p>Time table info service visar för vilken tidsperiod det finns tidtabellsdata tillgängligt i reseplaneraren. Informationen kan t ex användas för att markera sökbar tidsperiod i en kalender.</p>
<h3>Parametrar</h3>
<p>Inga specifika parametrar används för denna tjänst</p>
<p>Exempel:</p>

```text
api.sl.se/api2/TravelplannerV3_1/tti?key=<DIN API NYCKEL>
```

<h3><span>>Svarsstruktur</h3>
<p>Svaret innehåller information om mellan vilka datum som sökning är giltig, i nedanstående fall är datumintervallet 2016-12-11 till 2018-12-08.</p>

```xml

<TimetableInfoList serverVersion="1.7.6" dialectVersion="1.23" requestId="1507536412387"
                   begin="2016-12-11" end="2018-12-08">
    <TimetableInfo ident="7mtpu" date="2017-10-05" time="10:50:08"/>
    <TimetableInfo ident="65wha" date="2017-09-26" time="07:30:36"/>
    <TimetableInfo ident="6jpdq" date="2017-09-14" time="07:50:04"/>
    <TimetableInfo ident="2x6uq" date="2017-07-06" time="09:19:28"/>
</TimetableInfoList>
```

<h2> <a>Felmeddelanden</a></h2>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Statuskod</strong></p>
			</td>
			<td>
			<p><strong>Meddelande</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1001</p>
			</td>
			<td>
			<p><span>problem with request: Key is undefined</p>
			<p>Nyckel har ej skickats med.</p>
</td>
</tr>
<tr>
<td>
<p>1002</p>
</td>
<td>
<p><span>problem with request: Key is invalid</p>
			<p><span>Nyckel är ogiltig</p>
</td>
</tr>
<tr>
<td>
<p>1003</p>
</td>
<td>
<p><span>Invalid api</p>
			<p><span>Ogiltigt api</p>
</td>
</tr>
<tr>
<td>
<p>1004</p>
</td>
<td>
<p><span></p>
			<p><span>problem with request: This api is currently not available for keys with priority above 2</p>
</td>
</tr>
<tr>
<td>
<p>1005</p>
</td>
<td>
<p>Nyckel finns, men ej för detta api</p>
			<p><span>problem with request: Invalid api for key</p>
</td>
</tr>
<tr>
<td>
<p>1006</p>
</td>
<td>
<p>To many requests per minute</p>
			<p>För många anrop per minut, för den profil som används</p>
</td>
</tr>
<tr>
<td>
<p>1007</p>
</td>
<td>
<p>To many requests per month</p>
			<p>För många anrop per månad, för den profil som används</p>
</td>
</tr>
</tbody>
</table>
<h2>Skillnader jämfört med TravelPlannerV3</h2>
<p>Xsd:n är uppdaterad, men förutom nedanstående ändring så påverkas inte de befintliga funktionerna.</p>
<p>Ändringar:</p>
<p>Formatet på koordinater i polyline i Trip-anropet har ändrats. Numera beskrivs de med double-värden och 
differensvärden anges med exponent.
</p>
